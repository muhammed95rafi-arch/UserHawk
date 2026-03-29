#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║         UserHawk - Username Hunter      ║
║     Made by Muhammed | OSINT Tool       ║
╚══════════════════════════════════════════╝
"""

import urllib.request
import urllib.error
import sys
import time
import threading
from datetime import datetime

# ─── ANSI Colors ───────────────────────────────────────────────
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
BOLD    = "\033[1m"
RESET   = "\033[0m"
MAGENTA = "\033[95m"
BLUE    = "\033[94m"

# ─── Platform Definitions ──────────────────────────────────────
PLATFORMS = {
    "GitHub": {
        "url": "https://github.com/{}",
        "not_found_text": "Not Found",
    },
    "GitLab": {
        "url": "https://gitlab.com/{}",
        "not_found_text": "not found",
    },
    "Twitter/X": {
        "url": "https://twitter.com/{}",
        "not_found_text": "This account doesn't exist",
    },
    "Instagram": {
        "url": "https://www.instagram.com/{}/",
        "not_found_text": "Sorry, this page",
    },
    "TikTok": {
        "url": "https://www.tiktok.com/@{}",
        "not_found_text": "Couldn't find this account",
    },
    "Reddit": {
        "url": "https://www.reddit.com/user/{}",
        "not_found_text": "Sorry, nobody on Reddit goes by that name",
    },
    "LinkedIn": {
        "url": "https://www.linkedin.com/in/{}",
        "not_found_text": "Page not found",
    },
    "HackerOne": {
        "url": "https://hackerone.com/{}",
        "not_found_text": "Page not found",
    },
}

# ─── Banner ────────────────────────────────────────────────────
def print_banner():
    print(f"""
{CYAN}{BOLD}
 ██╗   ██╗███████╗███████╗██████╗ ██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗
 ██║   ██║██╔════╝██╔════╝██╔══██╗██║  ██║██╔══██╗██║    ██║██║ ██╔╝
 ██║   ██║███████╗█████╗  ██████╔╝███████║███████║██║ █╗ ██║█████╔╝ 
 ██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══██║██╔══██║██║███╗██║██╔═██╗ 
 ╚██████╔╝███████║███████╗██║  ██║██║  ██║██║  ██║╚███╔███╔╝██║  ██╗
  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
{RESET}
{YELLOW}        [ Username Enumeration Tool ] [ v1.0 ]{RESET}
{MAGENTA}        [ Platforms: GitHub, GitLab, Twitter, Instagram,{RESET}
{MAGENTA}          TikTok, Reddit, LinkedIn, HackerOne ]{RESET}
    """)

# ─── Check Single Platform ─────────────────────────────────────
def check_platform(platform, info, username, results):
    url = info["url"].format(username)
    not_found_text = info["not_found_text"]

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/122.0.0.0 Safari/537.36"
                )
            }
        )
        response = urllib.request.urlopen(req, timeout=10)
        html = response.read().decode("utf-8", errors="ignore")

        if not_found_text.lower() in html.lower():
            status = "NOT_FOUND"
        else:
            status = "FOUND"

    except urllib.error.HTTPError as e:
        if e.code in [404, 410]:
            status = "NOT_FOUND"
        elif e.code in [403, 429, 999]:
            status = "PROTECTED"
        else:
            status = "ERROR"
    except urllib.error.URLError:
        status = "ERROR"
    except Exception:
        status = "ERROR"

    results[platform] = {"status": status, "url": url}

    # Print result immediately (thread-safe print)
    if status == "FOUND":
        print(f"  {GREEN}[✓] FOUND    {RESET}{BOLD}{platform:<15}{RESET} → {CYAN}{url}{RESET}")
    elif status == "NOT_FOUND":
        print(f"  {RED}[✗] NOT FOUND{RESET} {platform:<15}")
    elif status == "PROTECTED":
        print(f"  {YELLOW}[~] PROTECTED{RESET} {platform:<15} → {url}")
    else:
        print(f"  {MAGENTA}[?] ERROR    {RESET} {platform:<15}")

# ─── Main Hunt Function ────────────────────────────────────────
def hunt(username):
    print(f"\n{BOLD}{YELLOW}[*] Target Username : {CYAN}{username}{RESET}")
    print(f"{BOLD}{YELLOW}[*] Scanning {len(PLATFORMS)} platforms...{RESET}")
    print(f"{BOLD}{YELLOW}[*] Time        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    print(f"\n{BOLD}{'─'*55}{RESET}\n")

    results = {}
    threads = []

    for platform, info in PLATFORMS.items():
        t = threading.Thread(
            target=check_platform,
            args=(platform, info, username, results)
        )
        threads.append(t)
        t.start()
        time.sleep(0.1)  # slight stagger to avoid rate limits

    for t in threads:
        t.join()

    # ─── Summary ───────────────────────────────────────────────
    found     = [p for p, r in results.items() if r["status"] == "FOUND"]
    not_found = [p for p, r in results.items() if r["status"] == "NOT_FOUND"]
    protected = [p for p, r in results.items() if r["status"] == "PROTECTED"]
    errors    = [p for p, r in results.items() if r["status"] == "ERROR"]

    print(f"\n{BOLD}{'─'*55}{RESET}")
    print(f"\n{BOLD}[SUMMARY] Username: {CYAN}{username}{RESET}")
    print(f"  {GREEN}Found     : {len(found)}{RESET}")
    print(f"  {RED}Not Found : {len(not_found)}{RESET}")
    print(f"  {YELLOW}Protected : {len(protected)}{RESET}")
    print(f"  {MAGENTA}Errors    : {len(errors)}{RESET}")

    if found:
        print(f"\n{GREEN}{BOLD}[+] Active Profiles:{RESET}")
        for p in found:
            print(f"    → {CYAN}{results[p]['url']}{RESET}")

    print()

# ─── Entry Point ───────────────────────────────────────────────
def main():
    print_banner()

    if len(sys.argv) < 2:
        print(f"{YELLOW}Usage:{RESET}  python3 userhawk.py <username>")
        print(f"{YELLOW}Example:{RESET} python3 userhawk.py muhammed95rafi")
        sys.exit(1)

    username = sys.argv[1].strip()

    if not username:
        print(f"{RED}[!] Username cannot be empty!{RESET}")
        sys.exit(1)

    hunt(username)

if __name__ == "__main__":
    main()
