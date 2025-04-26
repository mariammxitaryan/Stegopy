import argparse
import os
import sys
from steganocryptopy.steganography import Steganography

# ┌───────────────────────────────┐
# │        Key Generation         │
# │ Generates an AES key file to  │
# │ be used for encrypt/decrypt   │
# └───────────────────────────────┘
def generate_key(key_path: str, passphrase: str = "") -> None:
    """Generate and save a new AES key to 'key_path'."""
    if os.path.exists(key_path):
        print(f"Key file '{key_path}' already exists. Skipping generation.")
        return
    Steganography.generate_key(key_path)
    print(f"Key generated and saved to '{key_path}'")

# ┌───────────────────────────────┐
# │       Message Encryption      │
# │ Encrypts plaintext from a     │
# │ file and embeds it in an      │
# │ image, producing a stego-image│
# └───────────────────────────────┘
def encrypt_message(key_path: str, in_image: str, in_text: str, out_image: str) -> None:
    """Encrypt and hide text from 'in_text' into 'in_image'."""
    for path in (key_path, in_image, in_text):
        if not os.path.isfile(path):
            print(f"Error: File not found - {path}")
            sys.exit(1)
    secret_img = Steganography.encrypt(key_path, in_image, in_text)
    secret_img.save(out_image)
    print(f"Encrypted image saved to '{out_image}'")

# ┌───────────────────────────────┐
# │      Message Decryption       │
# │ Extracts and decrypts hidden  │
# │ text from a stego-image back  │
# │ into readable plaintext       │
# └───────────────────────────────┘
def decrypt_message(key_path: str, in_image: str) -> None:
    """Extract and decrypt hidden text from 'in_image'."""
    for path in (key_path, in_image):
        if not os.path.isfile(path):
            print(f"Error: File not found - {path}")
            sys.exit(1)
    try:
        message = Steganography.decrypt(key_path, in_image)
        print("Decrypted message:")
        print(message)
    except Exception as e:
        print(f"Decryption failed: {e}")
        sys.exit(1)

# ┌───────────────────────────────┐
# │      Argument Parsing         │
# │ Configures CLI options for    │
# │ key-gen, encrypt, and decrypt │
# └───────────────────────────────┘
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Steganography tool: encrypt/decrypt text in images"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # generate-key
    gk = subparsers.add_parser("generate-key", help="Generate a new AES key")
    gk.add_argument("--key", default="key.key", help="Path to save the key file")
    gk.add_argument("--passphrase", help="(unused) Optional passphrase")

    # encrypt
    enc = subparsers.add_parser("encrypt", help="Encrypt and hide text in image")
    enc.add_argument("--key", default="key.key", help="Path to AES key file")
    enc.add_argument("--in-image", required=True, help="Path to cover image")
    enc.add_argument("--in-text", required=True, help="Path to plaintext message file")
    enc.add_argument("--out-image", default="image_secret.png", help="Output stego-image file")

    # decrypt
    dec = subparsers.add_parser("decrypt", help="Extract and decrypt text from stego-image")
    dec.add_argument("--key", default="key.key", help="Path to AES key file")
    dec.add_argument("--in-image", required=True, help="Path to stego-image")

    return parser.parse_args()

# ┌───────────────────────────────┐
# │            Main               │
# │ Entry point: dispatches based │
# │ on selected CLI command       │
# └───────────────────────────────┘
def main():
    args = parse_arguments()
    if args.command == "generate-key":
        generate_key(args.key)
    elif args.command == "encrypt":
        encrypt_message(args.key, args.in_image, args.in_text, args.out_image)
    elif args.command == "decrypt":
        decrypt_message(args.key, args.in_image)

if __name__ == "__main__":
    main()