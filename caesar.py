"""Caesar cipher: encode and decode text by shifting letters."""

import argparse

ALPHABET_SIZE = 26


def shift_char(char: str, shift: int) -> str:
    """Shift one letter by `shift` places. Non-letters are returned unchanged."""
    if "A" <= char <= "Z":
        base = ord("A")
    elif "a" <= char <= "z":
        base = ord("a")
    else:
        return char
    return chr((ord(char) - base + shift) % ALPHABET_SIZE + base)


def encrypt(text: str, shift: int) -> str:
    """Encrypt text by shifting every letter forward."""
    return "".join(shift_char(c, shift) for c in text)


def decrypt(text: str, shift: int) -> str:
    """Decrypt text by shifting every letter backward."""
    return encrypt(text, -shift)


def main() -> None:
    parser = argparse.ArgumentParser(description="Caesar cipher encoder/decoder")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="what to do")
    parser.add_argument("text", help="the text to process (use quotes)")
    parser.add_argument("-s", "--shift", type=int, default=3, help="shift amount (default: 3)")
    args = parser.parse_args()

    if args.mode == "encrypt":
        print(encrypt(args.text, args.shift))
    else:
        print(decrypt(args.text, args.shift))


if __name__ == "__main__":
    main()
