#!/usr/bin/env python3
import struct
import sys
from Cryptodome.Cipher import AES
import zlib

# XOR key for initial header decryption
KEY_XOR = b"\xBA\xCD\xBC\xFE\xD6\xCA\xDD\xD3\xBA\xB9\xA3\xAB\xBF\xCB\xB5\xBE"

# Known AES keys for different firmware variants
LIST_KEY_AES = {
    "0x850000": b"\xE5\xBF\x66\x8F\x7D\x8C\xDB\x8D\x38\x1F\xAB\x79\x77\xBB\x72\x76\x5D\x2D\x2F\xF2\xC9\xB4\xF7\x1A\xDE\xC1\xF5\x74\x3E\x42\xD0\x8E",
    "0x850001": b"\x91\x8D\xA7\xB3\x26\x69\x0E\x52\x71\x94\x2D\x6C\xCD\x1C\xD6\x82\x1D\xD9\x25\x51\x5E\x98\x8D\xD4\x0D\x98\x75\xF1\xDA\xD0\xB1\x3D",
    "0x850100": b"\x51\xE8\x46\xD7\x0B\x8E\x23\xDA\xCE\x16\x09\x46\x3A\xF2\xB2\xF1\x4A\x21\x57\x40\x9F\x49\x31\xBD\x50\xE4\x40\xFF\x76\xA6\x0A\x4D",
    "0x850101": b"\x81\xEC\xAE\xB2\x0C\x6F\x8D\xE0\xFD\xE3\xD4\xAF\xB4\xAC\xE9\x0A\x9C\xB0\xE5\x9D\x19\xD3\xB7\xB7\x00\x34\xA4\x24\x3C\xF3\x97\x54"
}

def hexdump(data, length=256):
    for offset in range(0, min(len(data), length), 16):
        chunk = data[offset:offset+16]
        hex_bytes = " ".join(f"{b:02x}" for b in chunk)
        ascii_bytes = "".join((chr(b) if 32 <= b < 127 else ".") for b in chunk)
        print(f"{offset:08x}  {hex_bytes:<48}  |{ascii_bytes}|")

def firm_dec_hikv0(cipher_text, key_xor):
    plain_text = bytearray()
    length = len(cipher_text)
    for i in range(length):
        key_byte = key_xor[((i >> 4) + i) & 0xF]
        plain_text.append(cipher_text[i] ^ key_byte)
    return bytes(plain_text)

def firm_dec_aes(cipher_text, key):
    aes_ecb = AES.new(key, AES.MODE_ECB)
    if len(cipher_text) % 16 != 0:
        cipher_text = cipher_text[:len(cipher_text) - (len(cipher_text) % 16)]
    return aes_ecb.decrypt(cipher_text)

def cal_crc32(data):
    return zlib.crc32(data) & 0xFFFFFFFF

def firm_key_aes(select_key, length):
    KEY = LIST_KEY_AES[select_key]
    KEY_GEN = bytearray()
    for i in range(length):
        key_char = KEY[i]
        v5 = ((i*i) & 0xFF) + ((key_char*key_char) & 0xFF) + ((key_char % length) & 0xFF) + ((key_char * length * i) & 0xFF)
        KEY_GEN.append((v5 & 0xFF) ^ key_char)
    return bytes(KEY_GEN)

def decrypt_file_from_h2(fp, header_plain, key_gen_file, h1_size, name):
    """Search H2 for filename and decrypt"""
    idx = header_plain.find(name.encode())
    if idx == -1:
        print(f"{name} not found in header")
        return

    posi = idx + 8*4
    offset = struct.unpack("<I", header_plain[posi: posi+4])[0] + h1_size
    length = struct.unpack("<I", header_plain[posi+4: posi+8])[0]
    print(f"Decrypting {name}: offset={hex(offset)}, length={length}")

    fp.seek(offset)
    chunk_size = 16 * 1024
    remaining = length
    with open(name, "wb") as out:
        while remaining > 0:
            read_len = min(chunk_size, remaining)
            chunk = fp.read(read_len)
            if not chunk:
                break
            out.write(firm_dec_aes(chunk, key_gen_file))
            remaining -= len(chunk)
    print(f"{name} written successfully.")

def detect_h2_key(fp, h1_size, h2_size):
    """Try all known AES keys to find correct H2 decryption"""
    fp.seek(h1_size)
    sample = fp.read(min(0x100, h2_size))
    for key_name, key_bytes in LIST_KEY_AES.items():
        key_gen = firm_key_aes(key_name, 32)
        decrypted = firm_dec_aes(sample, key_gen)
        if b"02KH" in decrypted or b"03KH" in decrypted:
            print(f"Detected H2 key: {key_name}")
            return key_name, key_gen
    print("Unknown firmware variant, using default key 0x850000")
    default_key = "0x850000"
    return default_key, firm_key_aes(default_key, 32)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} firmware_file")
        sys.exit(1)

    fw_file = sys.argv[1]
    with open(fw_file, "rb") as fp:
        # Read header1
        ctext = fp.read(0x10)
        header_plain = firm_dec_hikv0(ctext, KEY_XOR)
        h1_size = struct.unpack("<I", header_plain[0x08:0x0c])[0]
        print(f"h1_size: {h1_size} (0x{h1_size:x})")

        fp.seek(0)
        header_plain = firm_dec_hikv0(fp.read(h1_size), KEY_XOR)

        # Read H2 size
        fp.seek(h1_size)
        h2_size_bytes = fp.read(0x10)
        if len(h2_size_bytes) < 0x10:
            print("Firmware too small or corrupted")
            sys.exit(1)

        header_plain += firm_dec_hikv0(h2_size_bytes, KEY_XOR)
        h2_size = struct.unpack("<I", header_plain[0x74:0x78])[0]
        print(f"h2_size: {h2_size} (0x{h2_size:x})")

        # Detect AES key dynamically
        key_name, key_gen_h2 = detect_h2_key(fp, h1_size, h2_size)

        # Decrypt H2 in chunks
        fp.seek(h1_size + 0x10)
        header2_encrypted_len = h2_size - 0x10
        header2_plain = bytearray()
        chunk_size = 16 * 1024
        remaining = header2_encrypted_len
        while remaining > 0:
            read_len = min(chunk_size, remaining)
            chunk = fp.read(read_len)
            if not chunk:
                break
            header2_plain.extend(firm_dec_aes(chunk, key_gen_h2))
            remaining -= len(chunk)

        full_header_plain = header_plain[:h1_size+0x10] + header2_plain

        # Checksum
        checksum_start = 0x78
        checksum_len = 0x700 - 0xc
        computed_crc = cal_crc32(full_header_plain[checksum_start:checksum_start+checksum_len])
        expected_crc = struct.unpack("<I", full_header_plain[0x70:0x74])[0]
        print(f"checksum expected={hex(expected_crc)}, computed={hex(computed_crc)}")
        if computed_crc != expected_crc:
            print("Decrypt H2 Checksum mismatch!")

        hexdump(full_header_plain[:256])

        # File AES key
        key_gen_file = firm_key_aes("0x850001", 32)

        # Decrypt internal files
        for fname in ["_cfgUpgClass", "LiteOS.bin", "ipc_db.jffs2"]:
            decrypt_file_from_h2(fp, full_header_plain, key_gen_file, h1_size, fname)


if __name__ == "__main__":
    main()

