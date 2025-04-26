# StegoPy

🔒🔍 **StegoPy** is a simple Python command-line tool for AES-based image steganography. Hide and extract text messages inside PNG images using `steganocryptopy`.

---

## 🚀 Repository Name Suggestion

I recommend naming your GitHub repo: **`stegopy`**

---

## 📦 Installation

1. Clone the repo:

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install steganocryptopy
   ```

---

## 🛠️ Usage

### 1. Generate AES Key

```bash
python stego_tool.py generate-key --key mykey.key
```

- `--key` (optional): path to save AES key (default: `key.key`).

### 2. Encrypt (Hide) Message

```bash
python stego_tool.py encrypt \
  --key mykey.key \
  --in-image cover.png \
  --in-text message.txt \
  --out-image secret.png
```

- `--in-image`: cover PNG image.
- `--in-text`: plaintext message file.
- `--out-image` (optional): output stego-image (default: `image_secret.png`).

### 3. Decrypt (Extract) Message

```bash
python stego_tool.py decrypt \
  --key mykey.key \
  --in-image secret.png
```

- `--in-image`: stego-image containing hidden text.

---

## ✨ Features

- **Key Generation**: AES-256 key file creation.
- **Encryption**: AES-encrypt and hide text inside a PNG image.
- **Decryption**: Extract and AES-decrypt hidden text.

---

