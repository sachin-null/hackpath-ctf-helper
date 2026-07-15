#!/usr/bin/env python3
# ============================================================
#   HACKPATH CTF HELPER v2
#   Created by: Sachin Ser | HackPath
#   Works on: Termux | Linux | Kali
#   Run: python3 ctf_helper.py
#   No extra install needed — Pure Python!
#   GitHub: github.com/sachin-null/hackpath-ctf-helper
# ============================================================

import os, sys, base64, binascii, hashlib
import urllib.parse, string, re, math

class C:
    R='\033[91m'; G='\033[92m'; Y='\033[93m'
    B='\033[94m'; M='\033[95m'; CY='\033[96m'
    W='\033[97m'; DIM='\033[2m'; X='\033[0m'
    BOLD='\033[1m'; UL='\033[4m'

def clear(): os.system('clear' if os.name!='nt' else 'cls')

def banner():
    clear()
    print(f"""{C.G}{C.BOLD}
   __________________   __  __________    ____ __________     
  / ____/_  __/ ____/  / / / / ____/ /   / __ \/ ____/__  \    
 / /     / / / /_     / /_/ / __/ / /   / /_/ / __/ / /_/ /    
/ /___  / / / __/    / __  / /___/ /___/ ____/ /___/ _, _/     
\____/ /_/ /_/      /_/ /_/_____/_____/_/   /_____/_/ |_|      
                                                               
{C.X}
{C.Y} 
 │  {C.G}CTF HELPER v2{C.Y}  ·  {C.CY}by Sachin Ser{C.Y}            
 │  {C.DIM}HackPath | Termux · Linux · Kali{C.Y}          
 │  {C.R}⚠ Educational / Authorized use only!{C.Y}       
 {C.X}
""")

def sep(t=""):
    if t: print(f"\n{C.CY}{'═'*14} {C.Y}{t}{C.CY} {'═'*14}{C.X}")
    else: print(f"{C.DIM}{'─'*52}{C.X}")

def ok(m):   print(f"{C.G}[+] {m}{C.X}")
def err(m):  print(f"{C.R}[-] {m}{C.X}")
def inf(m):  print(f"{C.CY}[*] {m}{C.X}")
def res(k,v):print(f"  {C.Y}{k:<20}{C.X}: {C.W}{v}{C.X}")

def pause(): input(f"\n{C.DIM}Press Enter...{C.X}")

def get_input(prompt):
    return input(f"{C.G}  {prompt} > {C.X}").strip()

# ══════════════════════════════════════════
#   1. BASE64
# ══════════════════════════════════════════
def base64_tool():
    sep("BASE64")
    print(f"  {C.G}[1]{C.X} Encode  {C.G}[2]{C.X} Decode  {C.G}[3]{C.X} Auto detect")
    ch = get_input("Choice")
    text = get_input("Input")
    if not text: err("Empty!"); pause(); return

    if ch == '1':
        result = base64.b64encode(text.encode()).decode()
        ok(f"Encoded: {C.W}{result}")
        # Also URL-safe
        url_safe = base64.urlsafe_b64encode(text.encode()).decode()
        res("URL-safe B64", url_safe)

    elif ch == '2':
        try:
            # Try standard
            result = base64.b64decode(text).decode(errors='replace')
            ok(f"Decoded: {C.W}{result}")
        except:
            try:
                result = base64.urlsafe_b64decode(text).decode(errors='replace')
                ok(f"URL-safe decoded: {C.W}{result}")
            except:
                err("Invalid base64!")

    elif ch == '3':
        # Auto detect
        if re.match(r'^[A-Za-z0-9+/]+=*$', text):
            try:
                dec = base64.b64decode(text).decode(errors='replace')
                ok(f"Looks like Base64!")
                res("Decoded", dec)
            except:
                inf("Not valid base64")
        else:
            enc = base64.b64encode(text.encode()).decode()
            ok("Encoded to Base64:")
            res("Result", enc)
    pause()

# ══════════════════════════════════════════
#   2. HEX
# ══════════════════════════════════════════
def hex_tool():
    sep("HEX ENCODE / DECODE")
    print(f"  {C.G}[1]{C.X} Text→Hex  {C.G}[2]{C.X} Hex→Text  {C.G}[3]{C.X} Hex→Bytes")
    ch = get_input("Choice")
    text = get_input("Input")
    if not text: err("Empty!"); pause(); return

    if ch == '1':
        hex_out = text.encode().hex()
        ok("Hex output:")
        res("Hex", hex_out)
        res("Hex (spaced)", ' '.join(hex_out[i:i+2] for i in range(0,len(hex_out),2)))
        res("Hex (0x)", '0x'+' 0x'.join(hex_out[i:i+2] for i in range(0,len(hex_out),2)))

    elif ch == '2':
        try:
            clean = text.replace(' ','').replace('0x','').replace(',','').replace('\n','')
            result = bytes.fromhex(clean).decode(errors='replace')
            ok(f"Decoded: {C.W}{result}")
        except:
            err("Invalid hex!")

    elif ch == '3':
        try:
            clean = text.replace(' ','').replace('0x','')
            b = bytes.fromhex(clean)
            ok("Bytes:")
            res("Raw bytes", str(b))
            res("Integers", str(list(b)))
        except:
            err("Invalid hex!")
    pause()

# ══════════════════════════════════════════
#   3. HASH
# ══════════════════════════════════════════
def hash_tool():
    sep("HASH TOOLS")
    print(f"  {C.G}[1]{C.X} Generate hash")
    print(f"  {C.G}[2]{C.X} Crack hash (wordlist)")
    print(f"  {C.G}[3]{C.X} Identify hash type")
    ch = get_input("Choice")

    if ch == '1':
        text = get_input("Text to hash")
        if not text: err("Empty!"); pause(); return
        sep("HASH RESULTS")
        algos = [
            ('MD5',    hashlib.md5),
            ('SHA1',   hashlib.sha1),
            ('SHA224', hashlib.sha224),
            ('SHA256', hashlib.sha256),
            ('SHA384', hashlib.sha384),
            ('SHA512', hashlib.sha512),
        ]
        for name, algo in algos:
            h = algo(text.encode()).hexdigest()
            res(name, h)

    elif ch == '2':
        target = get_input("Hash to crack")
        wfile  = get_input("Wordlist file (or press Enter for common passwords)")
        if not target: err("Empty!"); pause(); return

        wordlist = []
        if wfile and os.path.exists(wfile):
            with open(wfile,'r',errors='ignore') as f:
                wordlist = [l.strip() for l in f if l.strip()]
            inf(f"Loaded {len(wordlist):,} words from {wfile}")
        else:
            # Common passwords built-in
            wordlist = [
                'password','123456','password123','admin','root',
                'letmein','qwerty','abc123','monkey','1234567890',
                'pass','test','user','login','welcome','hello',
                'dragon','master','superman','batman','iloveyou',
                'sunshine','princess','football','shadow','12345',
                '123456789','password1','1234','111111','123123',
                'admin123','root123','toor','pass123','test123',
                'hackme','hacker','hack','ctf','flag','secret',
                'sachin','hackpath','sachin123','sachin@123',
            ]
            inf(f"Using {len(wordlist)} common passwords")

        inf(f"Cracking: {target}")
        target_lower = target.lower()
        found = False

        algos = [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512]
        algo_names = ['MD5','SHA1','SHA256','SHA512']

        for word in wordlist:
            for algo, aname in zip(algos, algo_names):
                h = algo(word.encode()).hexdigest()
                if h.lower() == target_lower:
                    ok(f"CRACKED! {C.G}{word}{C.X} [{aname}]")
                    found = True
                    break
            if found: break

        if not found:
            err(f"Not found in {len(wordlist):,} words")
            inf("Try: john --wordlist=rockyou.txt hash.txt")

    elif ch == '3':
        h = get_input("Hash to identify")
        length = len(h.replace(' ',''))
        sep("HASH IDENTIFICATION")
        types = {
            32: ['MD5','NTLM'],
            40: ['SHA1','MySQL5'],
            56: ['SHA224'],
            64: ['SHA256','Keccak-256'],
            96: ['SHA384'],
            128:['SHA512','Keccak-512'],
            13: ['DES (crypt)'],
            34: ['MD5 (Unix)'],
        }
        if length in types:
            ok(f"Possible types: {C.Y}{', '.join(types[length])}")
        else:
            inf(f"Unknown length: {length}")
        res("Length", str(length))
        res("Charset", "hex" if all(c in '0123456789abcdefABCDEF' for c in h) else "mixed")
    pause()

# ══════════════════════════════════════════
#   4. CAESAR / ROT
# ══════════════════════════════════════════
def caesar_tool():
    sep("CAESAR / ROT CIPHER")
    print(f"  {C.G}[1]{C.X} Brute force all shifts")
    print(f"  {C.G}[2]{C.X} Encrypt with shift")
    print(f"  {C.G}[3]{C.X} Decrypt with known shift")
    ch = get_input("Choice")
    text = get_input("Input text")
    if not text: err("Empty!"); pause(); return

    def caesar(t, shift):
        result = ''
        for c in t:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                result += chr((ord(c)-base+shift)%26+base)
            else:
                result += c
        return result

    if ch == '1':
        sep("ALL 25 SHIFTS")
        for i in range(1, 26):
            dec = caesar(text, i)
            print(f"  {C.Y}ROT{i:<3}{C.X}: {C.W}{dec}{C.X}")

    elif ch == '2':
        shift = int(get_input("Shift (1-25)") or "13")
        result = caesar(text, shift)
        ok(f"Encrypted (ROT{shift}): {C.W}{result}")

    elif ch == '3':
        shift = int(get_input("Known shift") or "13")
        result = caesar(text, shift)
        ok(f"Decrypted: {C.W}{result}")
    pause()

# ══════════════════════════════════════════
#   5. URL ENCODE
# ══════════════════════════════════════════
def url_tool():
    sep("URL ENCODE / DECODE")
    print(f"  {C.G}[1]{C.X} Encode  {C.G}[2]{C.X} Decode  {C.G}[3]{C.X} Both")
    ch = get_input("Choice")
    text = get_input("Input")
    if not text: err("Empty!"); pause(); return

    if ch == '1':
        enc = urllib.parse.quote(text)
        enc_plus = urllib.parse.quote_plus(text)
        ok("URL Encoded:")
        res("Standard (%)", enc)
        res("Plus (+)", enc_plus)

    elif ch == '2':
        dec = urllib.parse.unquote(text)
        dec_plus = urllib.parse.unquote_plus(text)
        ok("URL Decoded:")
        res("Standard", dec)
        res("Plus", dec_plus)

    elif ch == '3':
        ok("Encoded:")
        res("%XX", urllib.parse.quote(text))
        ok("Decoded (treating as URL):")
        res("Result", urllib.parse.unquote(text))
    pause()

# ══════════════════════════════════════════
#   6. BINARY
# ══════════════════════════════════════════
def binary_tool():
    sep("BINARY CONVERTER")
    print(f"  {C.G}[1]{C.X} Text→Binary  {C.G}[2]{C.X} Binary→Text")
    print(f"  {C.G}[3]{C.X} Decimal→Binary  {C.G}[4]{C.X} Binary→Decimal")
    ch = get_input("Choice")
    text = get_input("Input")
    if not text: err("Empty!"); pause(); return

    if ch == '1':
        bins = ' '.join(format(ord(c),'08b') for c in text)
        ok(f"Binary: {C.W}{bins}")

    elif ch == '2':
        try:
            clean = text.replace(' ','')
            chars = [clean[i:i+8] for i in range(0,len(clean),8)]
            result = ''.join(chr(int(b,2)) for b in chars if len(b)==8)
            ok(f"Text: {C.W}{result}")
        except:
            err("Invalid binary!")

    elif ch == '3':
        try:
            n = int(text)
            ok(f"Binary: {C.W}{bin(n)[2:]}")
            res("Hex", hex(n))
            res("Octal", oct(n))
        except:
            err("Invalid number!")

    elif ch == '4':
        try:
            result = int(text.replace(' ',''), 2)
            ok(f"Decimal: {C.W}{result}")
            res("Hex", hex(result))
            res("Char", chr(result) if result < 128 else 'N/A')
        except:
            err("Invalid binary!")
    pause()

# ══════════════════════════════════════════
#   7. XOR
# ══════════════════════════════════════════
def xor_tool():
    sep("XOR TOOL")
    print(f"  {C.G}[1]{C.X} XOR with key (text)")
    print(f"  {C.G}[2]{C.X} XOR brute force (single byte)")
    print(f"  {C.G}[3]{C.X} XOR hex strings")
    ch = get_input("Choice")

    if ch == '1':
        text = get_input("Text")
        key  = get_input("Key")
        if not text or not key: err("Empty!"); pause(); return
        result = ''.join(chr(ord(t)^ord(k)) for t,k in
                         zip(text, key*(len(text)//len(key)+1)))
        ok(f"XOR result: {C.W}{result}")
        res("Hex", result.encode().hex())

    elif ch == '2':
        text = get_input("Hex encoded ciphertext")
        if not text: err("Empty!"); pause(); return
        try:
            data = bytes.fromhex(text.replace(' ',''))
        except:
            data = text.encode()

        sep("XOR BRUTE FORCE")
        for key in range(1, 256):
            result = bytes(b^key for b in data)
            try:
                decoded = result.decode('ascii')
                if all(32<=ord(c)<127 for c in decoded):
                    print(f"  {C.Y}Key={key:<4} 0x{key:02x}{C.X}: {C.W}{decoded[:60]}{C.X}")
            except:
                pass

    elif ch == '3':
        h1 = get_input("Hex string 1")
        h2 = get_input("Hex string 2")
        try:
            b1 = bytes.fromhex(h1.replace(' ',''))
            b2 = bytes.fromhex(h2.replace(' ',''))
            xored = bytes(a^b for a,b in zip(b1,b2))
            ok(f"XOR result hex: {C.W}{xored.hex()}")
            try:
                ok(f"As text: {C.W}{xored.decode('ascii',errors='replace')}")
            except: pass
        except:
            err("Invalid hex!")
    pause()

# ══════════════════════════════════════════
#   8. STRING ANALYZER
# ══════════════════════════════════════════
def string_analyzer():
    sep("STRING ANALYZER")
    text = get_input("Paste string to analyze")
    if not text: err("Empty!"); pause(); return

    sep("ANALYSIS")
    res("Length", str(len(text)))
    res("Char types", f"Letters:{sum(c.isalpha() for c in text)} "
                     f"Digits:{sum(c.isdigit() for c in text)} "
                     f"Spaces:{sum(c.isspace() for c in text)}")

    # Detect encoding
    detections = []

    # Base64
    if re.match(r'^[A-Za-z0-9+/]+=*$', text) and len(text)%4==0:
        detections.append("✅ Looks like Base64")
        try:
            dec = base64.b64decode(text).decode(errors='replace')
            res("Base64 decoded", dec[:80])
        except: pass

    # Hex
    if re.match(r'^[0-9a-fA-F\s]+$', text) and len(text.replace(' ',''))%2==0:
        detections.append("✅ Looks like Hex")
        try:
            dec = bytes.fromhex(text.replace(' ','')).decode(errors='replace')
            res("Hex decoded", dec[:80])
        except: pass

    # Binary
    if re.match(r'^[01\s]+$', text):
        detections.append("✅ Looks like Binary")

    # URL encoded
    if '%' in text:
        detections.append("✅ Looks like URL encoded")
        res("URL decoded", urllib.parse.unquote(text)[:80])

    # ROT13 guess
    if text.isalpha():
        detections.append("ℹ️  All alpha — try Caesar/ROT")

    # Hash detection
    hash_lengths = {32:'MD5',40:'SHA1',64:'SHA256',128:'SHA512'}
    clean = text.replace(' ','')
    if len(clean) in hash_lengths and re.match(r'^[0-9a-fA-F]+$',clean):
        detections.append(f"✅ Looks like {hash_lengths[len(clean)]} hash")

    # Morse
    if all(c in '.-/ \t' for c in text):
        detections.append("✅ Looks like Morse code")

    sep("DETECTIONS")
    if detections:
        for d in detections:
            print(f"  {C.G}{d}{C.X}")
    else:
        inf("No common encoding detected — might be custom cipher")

    # Frequency analysis
    sep("FREQUENCY")
    freq = {}
    for c in text.lower():
        if c.isalpha():
            freq[c] = freq.get(c,0)+1
    if freq:
        sorted_freq = sorted(freq.items(), key=lambda x:-x[1])[:8]
        res("Top chars", '  '.join(f"{k}:{v}" for k,v in sorted_freq))
    pause()

# ══════════════════════════════════════════
#   9. MORSE CODE
# ══════════════════════════════════════════
def morse_tool():
    sep("MORSE CODE")
    MORSE = {
        'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
        'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
        'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
        '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
        '6':'-....','7':'--...','8':'---..','9':'----.',
        '.':'.-.-.-',',':'--..--','?':'..--..','!':'-.-.--',' ':'/'
    }
    REV = {v:k for k,v in MORSE.items()}

    print(f"  {C.G}[1]{C.X} Text→Morse  {C.G}[2]{C.X} Morse→Text")
    ch = get_input("Choice")
    text = get_input("Input")
    if not text: err("Empty!"); pause(); return

    if ch == '1':
        encoded = ' '.join(MORSE.get(c.upper(),'?') for c in text)
        ok(f"Morse: {C.W}{encoded}")

    elif ch == '2':
        words = text.split(' / ')
        result = ''
        for word in words:
            for code in word.split():
                result += REV.get(code,'?')
            result += ' '
        ok(f"Decoded: {C.W}{result.strip()}")
    pause()

# ══════════════════════════════════════════
#   10. NUMBER SYSTEM CONVERTER
# ══════════════════════════════════════════
def number_converter():
    sep("NUMBER SYSTEM CONVERTER")
    print(f"  {C.G}[1]{C.X} Decimal  {C.G}[2]{C.X} Hex  {C.G}[3]{C.X} Binary  {C.G}[4]{C.X} Octal")
    ch = get_input("Input base")
    num = get_input("Number")
    if not num: err("Empty!"); pause(); return

    try:
        bases = {'1':10,'2':16,'3':2,'4':8}
        base = bases.get(ch, 10)
        n = int(num.replace('0x','').replace('0b','').replace('0o',''), base)

        sep("ALL BASES")
        res("Decimal (10)", str(n))
        res("Hexadecimal (16)", hex(n))
        res("Binary (2)", bin(n))
        res("Octal (8)", oct(n))
        if 0 <= n <= 127:
            res("ASCII char", chr(n))
        if 0 <= n <= 0x10FFFF:
            try: res("Unicode", chr(n))
            except: pass
    except:
        err("Invalid input!")
    pause()

# ══════════════════════════════════════════
#   11. ROT47 / ROT13
# ══════════════════════════════════════════
def rot_tool():
    sep("ROT ENCODINGS")
    print(f"  {C.G}[1]{C.X} ROT13   {C.G}[2]{C.X} ROT47   {C.G}[3]{C.X} ROT18")
    ch = get_input("Choice")
    text = get_input("Input")
    if not text: err("Empty!"); pause(); return

    if ch == '1':
        result = ''
        for c in text:
            if 'A'<=c<='Z': result+=chr((ord(c)-65+13)%26+65)
            elif 'a'<=c<='z': result+=chr((ord(c)-97+13)%26+97)
            else: result+=c
        ok(f"ROT13: {C.W}{result}")

    elif ch == '2':
        result = ''
        for c in text:
            if 33<=ord(c)<=126:
                result+=chr((ord(c)-33+47)%94+33)
            else: result+=c
        ok(f"ROT47: {C.W}{result}")

    elif ch == '3':
        # ROT18 = ROT13 + ROT5 (letters+digits)
        result = ''
        for c in text:
            if 'A'<=c<='Z': result+=chr((ord(c)-65+13)%26+65)
            elif 'a'<=c<='z': result+=chr((ord(c)-97+13)%26+97)
            elif '0'<=c<='9': result+=chr((ord(c)-48+5)%10+48)
            else: result+=c
        ok(f"ROT18: {C.W}{result}")
    pause()

# ══════════════════════════════════════════
#   12. CTF HINTS CHEATSHEET
# ══════════════════════════════════════════
def ctf_hints():
    sep("CTF HINTS CHEATSHEET")
    hints = [
        (f"{C.Y}ENCODING TRICKS{C.X}", [
            "Base64 ends with = or ==",
            "Hex: only 0-9 and a-f chars",
            "Binary: only 0s and 1s",
            "URL encode: %XX format",
            "ROT13: shift letters by 13",
            "ROT47: shift ASCII 33-126 by 47",
        ]),
        (f"{C.CY}HASH IDENTIFICATION{C.X}", [
            "MD5: 32 hex chars",
            "SHA1: 40 hex chars",
            "SHA256: 64 hex chars",
            "SHA512: 128 hex chars",
            "bcrypt: starts with $2b$",
            "NTLM: 32 hex (Windows)",
        ]),
        (f"{C.G}STEGANOGRAPHY{C.X}", [
            "steghide extract -sf image.jpg",
            "binwalk -e file  (extract hidden files)",
            "strings file     (find readable strings)",
            "exiftool image   (check metadata)",
            "zsteg image.png  (PNG steganography)",
        ]),
        (f"{C.M}FILE MAGIC{C.X}", [
            "PNG: 89 50 4E 47 0D 0A 1A 0A",
            "JPEG: FF D8 FF",
            "ZIP: 50 4B 03 04",
            "PDF: 25 50 44 46",
            "ELF: 7F 45 4C 46",
            "file <filename>  (detect type)",
            "xxd file | head  (view hex)",
        ]),
        (f"{C.R}SQL INJECTION{C.X}", [
            "' OR '1'='1",
            "' OR 1=1--",
            "admin'--",
            "' UNION SELECT null,null--",
            "sqlmap -u URL --dbs",
        ]),
        (f"{C.B}WEB CTF{C.X}", [
            "View page source: Ctrl+U",
            "Check robots.txt",
            "Check /admin, /.git",
            "Burp Suite intercept",
            "Cookie manipulation",
            "XSS: <script>alert(1)</script>",
        ]),
        (f"{C.Y}CRYPTO TRICKS{C.X}", [
            "Vigenere: use dcode.fr",
            "Affine: y=ax+b (mod 26)",
            "RSA small e: cube root attack",
            "XOR known plaintext attack",
            "Frequency analysis for substitution",
        ]),
        (f"{C.CY}FORENSICS{C.X}", [
            "volatility (memory forensics)",
            "Wireshark (packet analysis)",
            "foremost (file carving)",
            "photorec (recover files)",
            "tcpdump -r capture.pcap",
        ]),
    ]
    for title, items in hints:
        print(f"\n  {title}")
        for item in items:
            print(f"  {C.DIM}  •{C.X} {C.W}{item}{C.X}")
    print(f"\n  {C.DIM}by Sachin Ser | HackPath{C.X}")
    pause()

# ══════════════════════════════════════════
#   13. STRING TOOLS
# ══════════════════════════════════════════
def string_tools():
    sep("STRING TOOLS")
    print(f"  {C.G}[1]{C.X} Reverse string")
    print(f"  {C.G}[2]{C.X} Count characters")
    print(f"  {C.G}[3]{C.X} ASCII values")
    print(f"  {C.G}[4]{C.X} Find flag pattern")
    ch = get_input("Choice")
    text = get_input("Input")
    if not text: err("Empty!"); pause(); return

    if ch == '1':
        ok(f"Reversed: {C.W}{text[::-1]}")

    elif ch == '2':
        res("Total chars", str(len(text)))
        res("Letters", str(sum(c.isalpha() for c in text)))
        res("Digits", str(sum(c.isdigit() for c in text)))
        res("Spaces", str(sum(c.isspace() for c in text)))
        res("Special", str(sum(not c.isalnum() and not c.isspace() for c in text)))

    elif ch == '3':
        ascii_vals = [str(ord(c)) for c in text]
        ok(f"ASCII: {C.W}{' '.join(ascii_vals)}")
        from_ascii = ''.join(chr(int(x)) for x in text.split() if x.isdigit())
        if from_ascii:
            ok(f"From ASCII: {C.W}{from_ascii}")

    elif ch == '4':
        # Common CTF flag patterns
        patterns = [
            r'[A-Z]{2,8}\{[^\}]+\}',  # FLAG{...}
            r'[a-z]{2,8}\{[^\}]+\}',  # flag{...}
            r'CTF\{[^\}]+\}',
            r'flag\{[^\}]+\}',
            r'htb\{[^\}]+\}',
            r'picoCTF\{[^\}]+\}',
        ]
        found = []
        for p in patterns:
            matches = re.findall(p, text, re.IGNORECASE)
            found.extend(matches)
        if found:
            ok("Flags found:")
            for f in found:
                print(f"  {C.G}🚩 {C.W}{f}{C.X}")
        else:
            inf("No flag pattern found")
    pause()

# ══════════════════════════════════════════
#   MAIN MENU
# ══════════════════════════════════════════
def main():
    while True:
        banner()
        print(f"""  {C.BOLD}TOOLS MENU{C.X}

  {C.G}[1]{C.X}  Base64 Encode/Decode
  {C.G}[2]{C.X}  Hex Encode/Decode
  {C.G}[3]{C.X}  Hash (Generate + Crack + Identify)
  {C.G}[4]{C.X}  Caesar / ROT Brute Force
  {C.G}[5]{C.X}  URL Encode/Decode
  {C.G}[6]{C.X}  Binary Converter
  {C.G}[7]{C.X}  XOR Tool (Brute Force)
  {C.G}[8]{C.X}  String Analyzer (Auto Detect)
  {C.G}[9]{C.X}  Morse Code
  {C.G}[10]{C.X} Number System Converter
  {C.G}[11]{C.X} ROT13 / ROT47 / ROT18
  {C.G}[12]{C.X} CTF Hints Cheatsheet 💡
  {C.G}[13]{C.X} String Tools (Reverse/ASCII/Flag)
  {C.R}[0]{C.X}  Exit

{C.DIM}  python3 ctf_helper.py | HackPath v2{C.X}
""")
        ch = input(f"{C.G}HackPath CTF > {C.X}").strip()

        menu = {
            '1':base64_tool,'2':hex_tool,'3':hash_tool,
            '4':caesar_tool,'5':url_tool,'6':binary_tool,
            '7':xor_tool,'8':string_analyzer,'9':morse_tool,
            '10':number_converter,'11':rot_tool,
            '12':ctf_hints,'13':string_tools,
        }

        if ch in menu:
            menu[ch]()
        elif ch == '0':
            print(f"\n{C.G}HackPath CTF Helper v2 — Bye! 👋{C.X}\n")
            sys.exit(0)
        else:
            print(f"{C.R}Invalid!{C.X}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.G}Bye! 👋{C.X}\n")
        sys.exit(0)
