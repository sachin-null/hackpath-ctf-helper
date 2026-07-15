# 🔓 HackPath CTF Helper v2

> **13-in-1 CTF solving toolkit for ethical hackers & beginners**
> Created by **Sachin Ser** | HackPath

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://python.org)
[![Version](https://img.shields.io/badge/Version-2.0-green?style=flat-square)](https://github.com/sachin-null/hackpath-ctf-helper)
[![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Kali-orange?style=flat-square)](https://github.com/sachin-null)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![HackPath](https://img.shields.io/badge/HackPath-CEH%20v12-red?style=flat-square)](https://github.com/sachin-null/hackpath)

---

```
  ██████╗████████╗███████╗
 ██╔════╝╚══██╔══╝██╔════╝
 ██║        ██║   █████╗
 ██║        ██║   ██╔══╝
 ╚██████╗   ██║   ██║
  ╚═════╝   ╚═╝   ╚═╝
 ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗
 ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
 ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
 ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
 ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
 ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                    v2  |  by Sachin Ser | HackPath
```

---

## 📌 What's New in v2?

| v1 | v2 |
|----|----|
| 10 tools | **13 tools** |
| Basic Base64 | Base64 + URL-safe + Auto detect |
| Simple Hex | Hex + Spaced + 0x format |
| Basic Hash | Hash + **Identify** + Improved crack |
| Caesar only | Caesar + **ROT13/47/18** |
| Basic XOR | XOR + **Hex XOR** + Brute force |
| — | **Number System Converter** (NEW) |
| — | **String Tools** + **Flag Finder** (NEW) |
| Basic hints | **Full CTF Cheatsheet** (NEW) |

---

## ⚡ All 13 Tools

| # | Tool | Features |
|---|------|---------|
| 1 | 🔤 **Base64** | Encode · Decode · URL-safe · Auto detect |
| 2 | 🔢 **Hex** | Encode · Decode · Spaced · 0x format |
| 3 | #️⃣ **Hash** | Generate (MD5/SHA1/SHA256/SHA512) · Crack · Identify |
| 4 | 🔄 **Caesar/ROT** | Encrypt · Decrypt · Brute force all 25 shifts |
| 5 | 🔗 **URL Encode** | Encode · Decode · Plus format |
| 6 | 💻 **Binary** | Text↔Binary · Dec/Hex/Oct converter |
| 7 | ⊕ **XOR** | Key XOR · Hex XOR · Single byte brute force |
| 8 | 🧵 **String Analyzer** | Auto-detect encoding · Frequency analysis |
| 9 | 📡 **Morse Code** | Encode · Decode |
| 10 | 🔢 **Number Converter** | Dec · Hex · Binary · Octal · ASCII |
| 11 | 🔁 **ROT13/47/18** | All three ROT variants |
| 12 | 💡 **CTF Hints** | Full cheatsheet (Crypto/Web/Forensics/Stego) |
| 13 | 🔍 **String Tools** | Reverse · ASCII values · 🚩 Flag finder |

---

## 📲 Install & Run

### Termux (Android)
```bash
pkg install python git -y
git clone https://github.com/sachin-null/hackpath-ctf-helper
cd hackpath-ctf-helper
python3 ctf_helper.py
```

### Kali Linux / Linux
```bash
git clone https://github.com/sachin-null/hackpath-ctf-helper
cd hackpath-ctf-helper
python3 ctf_helper.py
```

### One Line (Termux)
```bash
pkg install python git -y && git clone https://github.com/sachin-null/hackpath-ctf-helper && cd hackpath-ctf-helper && python3 ctf_helper.py
```

---

## 🖥️ Menu Preview

```
  TOOLS MENU

  [1]  Base64 Encode/Decode
  [2]  Hex Encode/Decode
  [3]  Hash (Generate + Crack + Identify)
  [4]  Caesar / ROT Brute Force
  [5]  URL Encode/Decode
  [6]  Binary Converter
  [7]  XOR Tool (Brute Force)
  [8]  String Analyzer (Auto Detect)
  [9]  Morse Code
  [10] Number System Converter
  [11] ROT13 / ROT47 / ROT18
  [12] CTF Hints Cheatsheet 💡
  [13] String Tools (Reverse/ASCII/Flag)
  [0]  Exit

  HackPath CTF >
```

---

## 🎯 CTF Platforms Supported

| Platform | URL |
|----------|-----|
| 🏁 picoCTF | picoctf.org |
| 🔐 HackTheBox | hackthebox.com |
| 🎯 TryHackMe | tryhackme.com |
| ⚡ CTFtime | ctftime.org |
| 🌐 OverTheWire | overthewire.org |

---

## 💡 CTF Hints Included

- 🔤 **Encoding tricks** — Base64, Hex, Binary, URL, ROT
- #️⃣ **Hash identification** — MD5/SHA/NTLM/bcrypt
- 🖼️ **Steganography** — steghide, binwalk, exiftool, zsteg
- 📁 **File magic bytes** — PNG, JPEG, ZIP, PDF, ELF
- 💉 **SQL Injection** — common payloads, sqlmap
- 🌐 **Web CTF** — XSS, cookies, robots.txt, .git
- 🔐 **Crypto tricks** — Vigenere, Affine, RSA
- 🔍 **Forensics** — volatility, Wireshark, foremost

---

## 📦 Requirements

```
✅ Python 3.x only
✅ Zero extra packages
✅ Works offline
✅ Termux / Kali / Ubuntu / Windows
```

---

## 📁 Files

```
hackpath-ctf-helper/
├── ctf_helper.py   ← Main tool (v2)
├── README.md       ← This file
└── LICENSE         ← MIT License
```

---

## 🔄 Changelog

### v2.0
- Added Number System Converter (Tool 10)
- Added ROT13/47/18 (Tool 11)
- Improved CTF Hints Cheatsheet (Tool 12)
- Added String Tools + Flag Finder (Tool 13)
- Base64 URL-safe support
- Hash identification feature
- XOR hex string support
- Improved auto-detection in String Analyzer

### v1.0
- Initial release with 10 tools

---

## ⚠️ Disclaimer

> Educational and authorized use only.
> The author is not responsible for any misuse.

---

## 👤 Created by

**Sachin Ser** | [HackPath](https://github.com/sachin-null)

[![GitHub](https://img.shields.io/badge/GitHub-sachin--null-black?style=flat-square&logo=github)](https://github.com/sachin-null)
[![Instagram](https://img.shields.io/badge/Instagram-sachin__ser-E1306C?style=flat-square&logo=instagram)](https://instagram.com/sachin_ser)

---

## 🔗 More HackPath Tools

| Tool | Repo | Description |
|------|------|-------------|
| 🔐 PassGen | [hackpath-passgen](https://github.com/sachin-null/hackpath-passgen) | Password generator |
| 📋 Wordlist Maker | [hackpath-wordlist-maker](https://github.com/sachin-null/hackpath-wordlist-maker) | Targeted wordlist |
| 🌐 OSINT Tool | [hackpath-osint](https://github.com/sachin-null/hackpath-osint) | IP/Domain/Port recon |
| 📱 Phone Analyzer | [hackpath-phone-analyzer](https://github.com/sachin-null/hackpath-phone-analyzer) | Phone number analysis |

---

<div align="center">

**⭐ Star this repo if it helped you!**

`Made with ❤️ by Sachin Ser | HackPath`

*Stay Curious. Keep Hacking. Explore the Hidden Reality.*

</div>
