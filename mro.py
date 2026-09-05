#!/usr/bin/env python3

"""
Encoding: UTF-8
---
Mro Input Method
Transform official romanized name into Mro char
Source of romanized name: [zi.tools](https://zi.tools/ab/16A40)
---
Author: AWGZYXDCZS
License: MIT
GitHub: https://github.com/pyanahida/Input-Method/blob/main/mro.py
"""

# =====CONSTANT=====

# Offset            +0x16A00
# Mro Alphabet      (40 - 5E)
MRO = "𖩀𖩁𖩂𖩃𖩄𖩅𖩆𖩇𖩈𖩉𖩊𖩋𖩌𖩍𖩎𖩏𖩐𖩑𖩒𖩓𖩔𖩕𖩖𖩗𖩘𖩙𖩚𖩛𖩜𖩝𖩞"
# Mro Number table  (60 - 69)
NUMBER = "𖩠𖩡𖩢𖩣𖩤𖩥𖩦𖩧𖩨𖩩"
# Mro Punctuation   (6E & 6F)
PUNCTUATION = {
    "DANDA": "𖩮",
    "DOUBLE_DANDA": "𖩯"
}

# Generate Dict
NAME = dict(zip([
"TA",
"NGI",
"YO",
"MIM",
"BA",
"DA",
"A",
"PHI",
"KHAI",
"HAO",
"DAI",
"CHU",
"KEAAE",
"OL",
"MAEM",
"NIN",
"PA",
"OO",
"O",
"RO",
"SHI",
"THEA",
"EA",
"WA",
"E",
"KO",
"LAN",
"LA",
"HAI",
"RI",
"TEK"
],MRO))

# =====Main Loop=====

def main():
    x = input("> ")
    if x == "exit": return True # Exit
    
    parse = x.upper().split(" ")
    result = ""
    for i in parse:
        # Name
        if i in NAME:
            result += NAME[i]
        # Number
        elif len(i) == 1:
            if '0' <= i <= '9':
                result += NUMBER[int(i)]
        # Punctuation
        elif i in PUNCTUATION:
            result += PUNCTUATION[i]
        # Replace unknown char
        else:
            result += "\uFFFD"
    print(result)
    return False

# =====Main=====
info = """Style: XX XX XX
Example: TA NGI BA DANDA
Accept uppercase and lowercase
"""

if __name__ == "__main__":
    print(info)
    while True:
        e = main()
        if e: break
