# Decrypt Firmware Hikvision

## Decrypt E3S
### File Decypt
- _cfgUpgClass
- ipc_db.jffs2
- LiteOS.bin 
### Download Firmware E3S

http://www.hikvisioneurope.com/portal/?dir=portal/Technical%20Materials/00%20%20Network%20Camera/00%20%20Product%20Firmware/E3S%20platform%281X23G0E%2C1X21%28E%29%29

## Usage
python2 dec_hik.py ./digicap.dav


$ podman run -it python:2.7 bash

 python -m pip install --upgrade pip
```bash
pip install pycrypto
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
Collecting pycrypto
  Downloading pycrypto-2.6.1.tar.gz (446 kB)
     |████████████████████████████████| 446 kB 2.5 MB/s
Building wheels for collected packages: pycrypto
  Building wheel for pycrypto (setup.py) ... done
  Created wheel for pycrypto: filename=pycrypto-2.6.1-cp27-cp27mu-linux_aarch64.whl size=523861 sha256=cde9dd3e387ae57e10656bffdc92dd0aeb816760f46e39680238a946113281f9
  Stored in directory: /root/.cache/pip/wheels/b6/e6/c8/d1eca13628952ceec1d40d96e0a7a1380460d2349ce0b85312
Successfully built pycrypto
Installing collected packages: pycrypto
Successfully installed pycrypto-2.6.1


git clone https://github.com/HaToan/Decrypt-Firmware-Hikvision/
Cloning into 'Decrypt-Firmware-Hikvision'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 5 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (5/5), done.
root@c05d8de22ad2:~# cd Decrypt-Firmware-Hikvision/
root@c05d8de22ad2:~/Decrypt-Firmware-Hikvision# ls
README.md  dec_hik.py  digicap.dav
root@c05d8de22ad2:~/Decrypt-Firmware-Hikvision# python dec_hik.py
['dec_hik.py']
Usage: python2 dec_hik.py pathfile
root@c05d8de22ad2:~/Decrypt-Firmware-Hikvision# python dec_hik.py digicap.dav
['dec_hik.py', 'digicap.dav']
0x0 	30 32 4b 48  12 21 00 00   6c 00 00 00  00 00 00 00  | 02KH.!..l.......
0x10 	a4 bf a0 00  01 00 00 00   ff ff ff ff  ff ff ff ff  | ................
0x20 	ff ff ff ff  ff ff ff ff   ff ff ff ff  31 33 33 30  | ............1330
0x30 	30 33 30 30  31 31 31 31   31 31 31 30  30 31 31 00  | 030011111110011.
0x40 	00 01 00 00  00 00 85 00   31 33 33 30  30 33 30 30  | ........13300300
0x50 	31 31 31 31  31 31 31 30   30 31 31 00  01 00 00 00  | 11111110011.....
0x60 	6c 00 00 00  38 bf a0 00   3b b5 12 50  30 33 4b 48  | l...8...;..P03KH
0x70 	c8 19 3b 0f  00 07 00 00   00 00 00 00  58 4a 5f 59  | ..;.........XJ_Y
0x80 	2e a3 5d 73  15 86 c2 53   a7 67 4a 11  f0 d7 e1 5b  | ..]s...S.gJ....[
0x90 	a1 1f 72 b5  f3 85 c9 79   ce 28 1a a9  aa f2 96 ba  | ..r....y.(......
0xa0 	4a 30 ce 3f  62 e3 04 0c   73 3e 9e e7  2f 71 98 82  | J0.?b...s>../q..
0xb0 	cc a7 fe c4  e5 bb df 3a   f9 ec fd 5c  f7 13 03 8e  | .......:...\....
0xc0 	17 ad f5 28  00 c8 50 a7   84 04 28 dc  02 6e 32 a2  | ...(..P...(..n2.
0xd0 	4f 9d 0d ed  20 e4 c2 a1   f2 de 6e a4  ed 83 ff 4e  | O... .....n....N
0xe0 	1a e9 68 f3  8e 45 10 03   2a c6 30 e1  4e f0 7c b7  | ..h..E..*.0.N.|.
0xf0 	60 29 41 4a  32 3c 9f 4e   1e ba 46 d6  b5 35 59 3f  | `)AJ2<.N..F..5Y?
0x100 	87 62 cb 4f  70 7a 92 9a   47 99 fc 94  65 b0 bb e1  | .b.Opz..G...e...
0x110 	57 f5 1b 91  52 55 43 9a   3a f3 6d f0  62 82 d1 ba  | W...RUC.:.m.b...
0x120 	e8 e6 ae 40  4b 3c 1d f6   0e 48 6e b5  21 98 39 cf  | ...@K<...Hn.!.9.
0x130 	41 00 97 54  88 c4 02 9f   86 53 c9 04  13 1c 88 f0  | A..T.....S......
0x140 	c2 76 00 b1  99 c3 8c 21   c9 34 b4 8d  7f 44 65 d3  | .v.....!.4...De.
0x150 	a5 97 b9 95  58 c2 56 42   f2 1a f3 25  aa ea 59 a9  | ....X.VB...%..Y.
0x160 	f6 2a 45 fb  94 1d fd 39   31 a6 3a 76  69 1b ca f8  | .*E....91.:vi...
0x170 	a1 bf 4a 34  97 cc 72 1f   5c bd 55 f0  2e 7c 7e 28  | ..J4..r.\.U..|~(
0x180 	af f4 92 0e  05 ad f6 ba   c6 0a ec 25  dc 2f 1f e3  | ...........%./..
0x190 	0e fd 01 69  6d 56 45 f4   94 10 bd bc  35 39 be 60  | ...imVE.....59.`
0x1a0 	a7 01 00 11  d4 9a 00 fe   a8 04 6b 01  74 3a 02 6a  | ..........k.t:.j
0x1b0 	29 fd d3 0e  00 01 01 76   29 dd 26 41  60 da 38 c7  | )......v).&A`.8.
0x1c0 	68 50 00 dd  be 05 45 01   12 3e 47 01  98 00 06 b2  | hP....E..>G.....
0x1d0 	78 b1 b6 0a  d4 09 00 44   be 00 00 20  f7 14 b0 bf  | x......D... ....
0x1e0 	14 02 85 cd  97 00 3d 00   9c 48 1b 1a  a0 92 a4 1a  | ......=..H......
0x1f0 	ea 00 27 43  62 86 05 b4   ab 84 56 6f  20 b9 00 6c  | ..'Cb.....Vo ..l
0x200 	bd 58 17 48  e2 56 15 04   b6 87 fb f3  8c 80 a7 b7  | .X.H.V..........
0x210 	c5 28 01 04  32 eb c5 33   01 63 ed 01  7c 8c 1e 57  | .(..2..3.c..|..W
0x220 	bd 9b 08 5d  01 f1 8b 8e   c9 e3 ab 00  7c 64 8a 65  | ...]........|d.e
0x230 	14 05 19 e5  bf de 15 c8   00 ac ec 07  1d dc ef ef  | ................
0x240 	a8 e3 9b 9f  51 2d 07 05   6a 43 ee e6  da 1f fe 2d  | ....Q-..jC.....-
0x250 	10 cc 06 01  a3 c6 14 01   02 57 b9 50  02 f1 bd c4  | .........W.P....
0x260 	d9 fc f3 20  20 cf 22 24   37 6c b9 00  03 00 00 00  | ...  ."$7l......
0x270 	01 00 00 00  02 00 00 00   01 00 00 00  0a 09 df 07  | ................
0x280 	73 ce fd 91  38 bf a0 00   67 e7 02 00  52 00 05 05  | s...8...g...R...
0x290 	00 00 00 00  00 00 00 00   2e 7c 7e 28  af f4 92 0e  | .........|~(....
0x2a0 	05 ad f6 ba  c6 0a ec 25   dc 2f 1f e3  0e fd 01 69  | .......%./.....i
0x2b0 	6d 56 45 f4  94 10 bd bc   35 39 be 60  a7 01 00 11  | mVE.....59.`....
0x2c0 	d4 9a 00 fe  a8 04 6b 01   74 3a 02 6a  29 fd d3 0e  | ......k.t:.j)...
0x2d0 	00 01 01 76  29 dd 26 41   60 da 38 c7  68 50 00 dd  | ...v).&A`.8.hP..
0x2e0 	be 05 45 01  12 3e 47 01   98 00 06 b2  78 b1 b6 0a  | ..E..>G.....x...
0x2f0 	d4 09 00 44  be 00 00 20   f7 14 b0 bf  14 02 85 cd  | ...D... ........
0x300 	97 00 3d 00  9c 48 1b 1a   a0 92 a4 1a  ea 00 27 43  | ..=..H........'C
0x310 	62 86 05 b4  ab 84 56 6f   20 b9 00 6c  bd 58 17 48  | b.....Vo ..l.X.H
0x320 	e2 56 15 04  b6 87 fb f3   8c 80 a7 b7  c5 28 01 04  | .V...........(..
0x330 	32 eb c5 33  01 63 ed 01   7c 8c 1e 57  bd 9b 08 5d  | 2..3.c..|..W...]
0x340 	01 f1 8b 8e  c9 e3 ab 00   7c 64 8a 65  14 05 19 e5  | ........|d.e....
0x350 	bf de 15 c8  00 ac ec 07   1d dc ef ef  a8 e3 9b 9f  | ................
0x360 	51 2d 07 05  6a 43 ee e6   da 1f fe 2d  10 cc 06 01  | Q-..jC.....-....
0x370 	a3 c6 14 01  02 57 b9 50   02 f1 bd c4  d9 fc f3 20  | .....W.P.......
0x380 	20 cf 22 24  37 6c b9 00   04 0c 4c 3b  52 66 00 2b  |  ."$7l....L;Rf.+
0x390 	f1 a1 05 5d  95 01 23 f6   62 1e dc 17  1a 76 32 7a  | ...]..#.b....v2z
0x3a0 	60 0c 05 0e  e5 01 e4 7e   ab 12 13 d4  a3 7d 09 e9  | `......~.....}..
0x3b0 	13 77 f9 01  08 4a 08 e3   00 92 32 d0  ea 05 01 dd  | .w...J....2.....
0x3c0 	c8 ef 81 f3  00 35 00 ba   95 00 e0 6d  02 47 42 69  | .....5.....m.GBi
0x3d0 	50 50 38 71  0f 00 ef de   39 2c 03 06  b6 42 84 79  | PP8q....9,...B.y
0x3e0 	04 17 e6 6f  bf 03 8b 00   1a 75 a5 5f  61 fb 62 81  | ...o.....u._a.b.
0x3f0 	d1 1f 0c 93  de 08 53 37   9e 8a 3c ed  38 15 25 69  | ......S7..<.8.%i
0x400 	60 96 ab b6  b2 28 03 1b   81 0f 44 49  72 6f 6f 74  | `....(....DIroot
0x410 	00 2e 7c 7e  28 af f4 92   0e 05 ad f6  ba c6 0a ec  | ..|~(...........
0x420 	25 dc 2f 1f  e3 0e fd 01   69 6d 56 45  f4 94 10 bd  | %./.....imVE....
0x430 	bc 35 39 be  60 a7 01 00   11 d4 9a 00  fe a8 04 6b  | .59.`..........k
0x440 	01 74 3a 02  6a 29 fd d3   0e 00 01 01  31 33 33 30  | .t:.j)......1330
0x450 	30 33 30 30  31 31 31 31   31 31 31 30  30 31 31 00  | 030011111110011.
0x460 	2e 7c 7e 28  af f4 92 0e   05 ad f6 ba  5f 63 66 67  | .|~(........_cfg
0x470 	55 70 67 43  6c 61 73 73   00 f1 07 00  0f cd 17 2c  | UpgClass.......,
0x480 	22 8a 90 f4  e6 1f 6e ce   5a aa eb cc  00 07 00 00  | ".....n.Z.......
0x490 	b8 01 00 00  03 2f 31 6c   1b 20 f0 10  40 f9 13 e5  | ...../1l. ..@...
0x4a0 	c7 b6 f9 45  fa 49 d1 7b   34 46 dd d3  1a 18 e4 e4  | ...E.I.{4F......
0x4b0 	25 01 48 8b  5f 80 7c 6f   42 36 f4 72  ea bf b5 34  | %.H._.|oB6.r...4
0x4c0 	0f 2e ac 10  99 ed 4a 39   93 8c 1a 60  5b 55 b5 3b  | ......J9...`[U.;
0x4d0 	51 20 5f 41  dd 29 98 b3   f1 07 00 0f  cd 17 2c 22  | Q _A.)........,"
0x4e0 	8a 90 f4 e6  1f 6e ce 5a   aa eb cc 6c  b1 95 77 88  | .....n.Z...l..w.
0x4f0 	d2 5c 90 db  b6 12 03 5d   a9 81 19 10  eb 03 8e d5  | .\.....]........
0x500 	f5 00 93 46  5e 24 9a 00   12 8b 53 6f  4c da 08 a0  | ...F^$....SoL...
0x510 	14 41 9c 00  c4 9c 02 2c   13 e5 d6 2c  cb 0f 01 26  | .A.....,...,...&
0x520 	c2 b3 6c 9e  69 05 a0 cc   50 37 15 60  0d 0a 85 fa  | ..l.i...P7.`....
0x530 	b6 4b ce 4d  76 ac 57 78   2f 5a 83 bf  10 50 02 01  | .K.Mv.Wx/Z...P..
0x540 	7e 65 0c db  59 04 6c 11   f0 d8 d5 9d  2c 00 11 09  | ~e..Y.l.....,...
0x550 	f1 38 03 f5  7b ce 01 6b   07 14 bd a8  01 da 00 18  | .8..{..k........
0x560 	08 3d 12 b6  07 0c 7b b9   ae 02 6e 2d  4c 69 74 65  | .=....{...n-Lite
0x570 	4f 53 2e 62  69 6e 00 f1   07 00 0f cd  17 2c 22 8a  | OS.bin.......,".
0x580 	90 f4 e6 1f  6e ce 5a aa   eb cc 6c b1  b8 08 00 00  | ....n.Z...l.....
0x590 	80 b6 5b 00  34 04 5b 3b   57 e6 a6 9d  3b 9c 77 ad  | ..[.4.[;W...;.w.
0x5a0 	0a 79 01 3c  8e fe fa 68   fb 86 14 53  fb 5a 97 b5  | .y.<...h...S.Z..
0x5b0 	4e 06 03 1b  8a fb 46 32   4f 27 e9 1f  a9 e1 88 f7  | N.....F2O'......
0x5c0 	4a 31 a0 d0  93 86 81 d4   5a ea 6d 82  91 b5 09 83  | J1......Z.m.....
0x5d0 	b1 0d 74 df  a7 20 30 ab   f1 07 00 0f  cd 17 2c 22  | ..t.. 0.......,"
0x5e0 	8a 90 f4 e6  1f 6e ce 5a   aa eb cc 6c  b1 95 77 88  | .....n.Z...l..w.
0x5f0 	d2 5c 90 db  b6 12 03 5d   a9 81 19 10  eb 03 8e d5  | .\.....]........
0x600 	f5 00 93 46  5e 24 9a 00   12 8b 53 6f  4c da 08 a0  | ...F^$....SoL...
0x610 	14 41 9c 00  c4 9c 02 2c   13 e5 d6 2c  cb 0f 01 26  | .A.....,...,...&
0x620 	c2 b3 6c 9e  69 05 a0 cc   50 37 15 60  0d 0a 85 fa  | ..l.i...P7.`....
0x630 	b6 4b ce 4d  76 ac 57 78   2f 5a 83 bf  10 50 02 01  | .K.Mv.Wx/Z...P..
0x640 	7e 65 0c db  59 04 6c 11   f0 d8 d5 9d  2c 00 11 09  | ~e..Y.l.....,...
0x650 	f1 38 03 f5  7b ce 01 6b   07 14 bd a8  01 da 00 18  | .8..{..k........
0x660 	08 3d 12 b6  07 0c 7b b9   ae 02 6e 2d  69 70 63 5f  | .=....{...n-ipc_
0x670 	64 62 2e 6a  66 66 73 32   00 2e 7c 7e  28 af f4 92  | db.jffs2..|~(...
0x680 	0e 05 ad f6  ba c6 0a ec   25 dc 2f 1f  38 bf 5b 00  | ........%./.8.[.
0x690 	00 00 45 00  b1 18 d5 43   86 44 b5 37  25 90 70 44  | ..E....C.D.7%.pD
0x6a0 	b3 dc cf 12  88 da f6 d2   5c b4 32 b3  08 a2 4c ab  | ........\.2...L.
0x6b0 	ef fb 53 94  e4 d8 27 9e   ac 45 1b ea  e9 95 1b f9  | ..S...'..E......
0x6c0 	e8 63 7b 30  9d ef bf d5   a1 de bf fb  07 a8 5a 57  | .c{0..........ZW
0x6d0 	60 ad 5f d0  d9 36 a9 2a   2e 7c 7e 28  af f4 92 0e  | `._..6.*.|~(....
0x6e0 	05 ad f6 ba  c6 0a ec 25   dc 2f 1f e3  0e fd 01 69  | .......%./.....i
0x6f0 	6d 56 45 f4  94 10 bd bc   35 39 be 60  a7 01 00 11  | mVE.....59.`....
0x700 	d4 9a 00 fe  a8 04 6b 01   74 3a 02 6a  29 fd d3 0e  | ......k.t:.j)...
0x710 	00 01 01 76  29 dd 26 41   60 da 38 c7  68 50 00 dd  | ...v).&A`.8.hP..
0x720 	be 05 45 01  12 3e 47 01   98 00 06 b2  78 b1 b6 0a  | ..E..>G.....x...
0x730 	d4 09 00 44  be 00 00 20   f7 14 b0 bf  14 02 85 cd  | ...D... ........
0x740 	97 00 3d 00  9c 48 1b 1a   a0 92 a4 1a  ea 00 27 43  | ..=..H........'C
0x750 	62 86 05 b4  ab 84 56 6f   20 b9 00 6c  bd 58 17 48  | b.....Vo ..l.X.H
0x760 	e2 56 15 04  b6 87 fb f3   8c 80 a7 b7  00 00 00 00  | .V..............
('checksum: ', '0xf3b19c8L')
Decrypt H2 Succcess
Offset: 0x76c, length: 0x1b8, checksum: 0x10f0201b
Offset: 0x924, length: 0x5bb680, checksum: 0x9da6e657
Offset: 0x5bbfa4, length: 0x450000, checksum: 0x37b54486
root@c05d8de22ad2:~/Decrypt-Firmware-Hikvision# ls -lart
total 20596
drwx------. 1 root root       54 Dec  9 15:07 ..
-rwxr-xr-x. 1 root root     8244 Dec  9 15:07 dec_hik.py
-rw-r--r--. 1 root root      341 Dec  9 15:07 README.md
-rwxr-xr-x. 1 root root 10534820 Dec  9 15:07 digicap.dav
drwxr-xr-x. 8 root root      163 Dec  9 15:07 .git
-rw-r--r--. 1 root root      432 Dec  9 15:07 _cfgUpgClass
-rw-r--r--. 1 root root  6010496 Dec  9 15:07 LiteOS.bin
drwxr-xr-x. 3 root root      130 Dec  9 15:07 .
-rw-r--r--. 1 root root  4521984 Dec  9 15:07 ipc_db.jffs2
root@c05d8de22ad2:~/Decrypt-Firmware-Hikvision#
```
