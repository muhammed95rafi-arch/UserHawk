# UserHawk 🦅
> Username Enumeration OSINT Tool — Inspired by Sherlock



![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)




![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)




![Platforms](https://img.shields.io/badge/Platforms-8-orange?style=flat-square)



---

## 📌 What is UserHawk?

UserHawk is a fast, lightweight **username enumeration tool** built in Python.  
Given a username, it checks **8 major platforms** and tells you where that account exists.

---

## 🌐 Platforms Supported

| Platform | URL Format |
|----------|-----------|
| GitHub | github.com/{username} |
| GitLab | gitlab.com/{username} |
| Twitter / X | twitter.com/{username} |
| Instagram | instagram.com/{username} |
| TikTok | tiktok.com/@{username} |
| Reddit | reddit.com/user/{username} |
| LinkedIn | linkedin.com/in/{username} |
| HackerOne | hackerone.com/{username} |

---

## ⚡ Features

- 🚀 Multi-threaded scanning — all platforms checked simultaneously
- 🎨 Color-coded terminal output
- 📊 Summary report at the end
- 🔒 Rate limit & protection detection (403/429)
- 📦 Zero dependencies — pure Python 3, no installs needed

---

## 🛠️ Installation

### 🐧 Linux / macOS / Kali / Parrot OS

```bash
git clone https://github.com/muhammed95rafi-arch/UserHawk.git
cd UserHawk
python3 userhawk.py <username>
📱 Termux (Android)
pkg update && pkg install git python -y
git clone https://github.com/muhammed95rafi-arch/UserHawk.git
cd UserHawk
python3 userhawk.py <username>
🪟 Windows
git clone https://github.com/muhammed95rafi-arch/UserHawk.git
cd UserHawk
python userhawk.py <username>
🚀 Usage
python3 userhawk.py <username>
Example:
python3 userhawk.py muhammed95rafi
📸 Output Preview
[✓] FOUND     GitHub          → https://github.com/muhammed95rafi
  [✗] NOT FOUND Instagram
  [~] PROTECTED LinkedIn        → https://linkedin.com/in/muhammed95rafi

[SUMMARY] Username: muhammed95rafi
  Found     : 1
  Not Found : 1
  Protected : 1
🛠️ Requirements
Python 3.x
No external libraries needed
⚠️ Disclaimer
This tool is intended for educational and ethical OSINT purposes only.
Only use it on accounts you own or have permission to investigate.
The author is not responsible for any misuse.
