# Input-Method

## Introduction

An open-source input method for niche languages implemented using Python command line.

## Collection

A collection of lightweight CLI input method engines for various scripts.  
Each script is self‑contained, shares a common interface (`main()` loop, `exit` to quit), and lives in the root directory.

---

## Usage

```bash
python3 <script>.py
# Accept termux
```

Type space‑separated tokens (romanization, digits, or punctuation) and press Enter.  
`exit` quits.

---

## Available Input Methods

| Script | Script Name | Description |
|--------|-------------|-------------|
| `mro.py` | Mro | Official romanization → Mro Unicode. [Details](https://zi.tools/ab/16A40) |

*(More to come – see Contributing)*

---

## Adding a New Input Method

1. Create a new Python file (e.g., `newscript.py`).
2. Define constants and a `main()` function (returns `True` to exit).
3. Follow the style of `mro.py`.
4. Update this table with a one‑line description.

---

## License

MIT
