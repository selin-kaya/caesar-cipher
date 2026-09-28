# Caesar Cipher Tool

A small command-line tool to **encrypt** and **decrypt** text with the
[Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher), written in Python.

## How it works

Each letter is shifted a fixed number of places in the alphabet. With a shift of 3:

```
A B C ... X Y Z
↓ ↓ ↓     ↓ ↓ ↓
D E F ... A B C
```

Upper/lower case is preserved, and spaces, numbers and punctuation are left unchanged.

## Usage

Requires Python 3.8+ (no extra packages).

```bash
python caesar.py encrypt "Hello, World!" --shift 3
# Khoor, Zruog!

python caesar.py decrypt "Khoor, Zruog!" --shift 3
# Hello, World!
```

## Running the tests

```bash
python -m unittest -v
```
