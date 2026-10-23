#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IP Lookup Tool
Developer: Mustaieen
"""

import ipaddress
import requests
import os
import sys

# ── Neon Colors ─────────────────────────────
R  = '\033[91m'   # red
G  = '\033[92m'   # green
Y  = '\033[93m'   # yellow
B  = '\033[94m'   # blue
M  = '\033[95m'   # magenta
C  = '\033[96m'   # cyan
W  = '\033[97m'   # white
BOLD = '\033[1m'  # bold
RS = '\033[0m'    # reset

API_URL = "https://ipwho.is/"

def banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"""{C}{BOLD}
  ╭──────────────────────────────────────────────────────────╮
  │  {Y}██╗██████╗     {C}██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
  │  {Y}██║██╔══██╗    {C}██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
  │  {Y}██║██████╔╝    {C}██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
  │  {Y}██║██╔═══╝     {C}██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
  │  {Y}██║██║         {C}███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
  │  {Y}╚═╝╚═╝         {C}╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
  ╰──────────────────────────────────────────────────────────╯
{RS}""")
    print(f"{M}{BOLD}  ═══════════════════════════════════════════════════════════{RS}")
    print(f"{W}{BOLD}                Developer: {Y}Mustaieen 💥⚡️{RS}")
    print(f"{W}{BOLD}                IP Information & Network Lookup{RS}")
    print(f"{M}{BOLD}  ═══════════════════════════════════════════════════════════{RS}\n")


def get_ip_info(ip):
    try:
        response = requests.get(API_URL + ip, timeout=15)
        response.raise_for_status()
        data = response.json()

        if not data.get("success", False):
            print(f"\n  {R}[!] IP information could not be found.{RS}")
            print(f"  {R}Reason: {data.get('message', 'Unknown error')}{RS}")
            return

        connection = data.get("connection") or {}
        timezone = data.get("timezone") or {}
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        print(f"\n  {C}{BOLD}╭────────────────────────────────────────╮{RS}")
        print(f"  {C}{BOLD}│{RS}  {G}{BOLD}🌐 IP INFORMATION{RS}                      {C}{BOLD}│{RS}")
        print(f"  {C}{BOLD}╰────────────────────────────────────────╯{RS}")
        
        print(f"  {W}🔹 IP Address : {Y}{data.get('ip', 'N/A')}{RS}")
        print(f"  {W}🔹 Type       : {Y}{data.get('type', 'N/A')}{RS}")
        print(f"  {W}🔹 Country    : {Y}{data.get('country', 'N/A')}{RS}")
        print(f"  {W}🔹 Region     : {Y}{data.get('region', 'N/A')}{RS}")
        print(f"  {W}🔹 City       : {Y}{data.get('city', 'N/A')}{RS}")
        print(f"  {W}🔹 Postal     : {Y}{data.get('postal', 'N/A')}{RS}")
        print(f"  {W}🔹 ISP        : {Y}{connection.get('isp', 'N/A')}{RS}")
        print(f"  {W}🔹 Org        : {Y}{connection.get('org', 'N/A')}{RS}")
        print(f"  {W}🔹 ASN        : {Y}{connection.get('asn', 'N/A')}{RS}")
        print(f"  {W}🔹 Timezone   : {Y}{timezone.get('id', 'N/A')}{RS}")

        if latitude is not None and longitude is not None:
            print(f"  {W}🔹 Latitude   : {Y}{latitude}{RS}")
            print(f"  {W}🔹 Longitude  : {Y}{longitude}{RS}")
            print(f"  {W}🔹 Map Link   : {C}https://maps.google.com/?q={latitude},{longitude}{RS}")

        print(f"\n  {M}[i] Location is approximate IP geolocation.{RS}")
        print(f"  {M}[i] This does not reveal live GPS location.{RS}")

    except requests.exceptions.Timeout:
        print(f"\n  {R}[!] Request timed out. Try again.{RS}")
    except requests.exceptions.RequestException as error:
        print(f"\n  {R}[!] Network/API error: {error}{RS}")
    except ValueError:
        print(f"\n  {R}[!] Invalid response received from the API.{RS}")


def main():
    while True:
        banner()
        print(f"  {C}{BOLD}[1]{RS} {W}Look up an IP address{RS}")
        print(f"  {C}{BOLD}[2]{RS} {W}Look up your public IP{RS}")
        print(f"  {C}{BOLD}[0]{RS} {W}Exit{RS}\n")

        choice = input(f"  {C}{BOLD}└─> Select option: {RS}").strip()

        if choice == "0":
            print(f"\n  {G}{BOLD}Goodbye! — Mustaieen 💥⚡️{RS}\n")
            sys.exit(0)

        elif choice == "1":
            ip = input(f"\n  {Y}[?] Enter IP address: {RS}").strip()
            try:
                address = ipaddress.ip_address(ip)
                if not address.is_global:
                    print(f"  {R}[!] Please enter a public, globally routable IP.{RS}")
                else:
                    get_ip_info(str(address))
            except ValueError:
                print(f"  {R}[!] Invalid IP address.{RS}")

        elif choice == "2":
            try:
                response = requests.get("https://api.ipify.org", timeout=10)
                response.raise_for_status()
                ip = response.text.strip()
                print(f"\n  {G}[+] Your public IP: {Y}{ip}{RS}")
                get_ip_info(ip)
            except requests.exceptions.RequestException as error:
                print(f"  {R}[!] Could not retrieve your public IP: {error}{RS}")

        else:
            print(f"  {R}[!] Invalid option.{RS}")

        input(f"\n  {C}Press Enter to continue...{RS}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n  {R}Exiting...{RS}\n")
        sys.exit(0)