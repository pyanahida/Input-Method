#!/usr/bin/env python3

"""
Encoding: UTF-8
---
Control Input Method
Transform official abbreviation name into ASCII Control char
---
Author: AWGZYXDCZS
License: MIT
GitHub: https://github.com/pyanahida/Input-Method/blob/main/control.py
"""

# =====CONSTANT=====

CONTROLS = {
    "NUL": "\u0000",
    "SOH": "\u0001",
    "STX": "\u0002",
    "ETX": "\u0003",
    "EOT": "\u0004",
    "ENQ": "\u0005",
    "ACK": "\u0006",
    "BEL": "\u0007",
    "BS": "\u0008",
    "HT": "\u0009",
    "LF": "\u000A",
    "VT": "\u000B",
    "FF": "\u000C",
    "CR": "\u000D",
    "SO": "\u000E",
    "SI": "\u000F",
    "DLE": "\u0010",
    "DC1": "\u0011",
    "DC2": "\u0012",
    "DC3": "\u0013",
    "DC4": "\u0014",
    "NAK": "\u0015",
    "SYN": "\u0016",
    "ETB": "\u0017",
    "CAN": "\u0018",
    "EM": "\u0019",
    "SUB": "\u001A",
    "ESC": "\u001B",
    "FS": "\u001C",
    "GS": "\u001D",
    "RS": "\u001E",
    "US": "\u001F",
    "DEL": "\u007F"
}

# =====Main Loop=====

def main():
    x = input("> ")
    if x == "exit": return True # Exit
    
    parse = x.upper().split(" ")
    result = ""
    for i in parse:
        # Name
        if i in CONTROL:
            result += CONTROL[i]
        else:
            result += "?"
    print(result)
    return False

# =====Main=====
info = """Style: XX XX XX
Example: NUL LF RS VT CR
Accept uppercase and lowercase
"""

if __name__ == "__main__":
    print(info)
    while True:
        e = main()
        if e: break
