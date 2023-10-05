# QR Code Generator

This is a simple Python script that uses the Segno library to generate a QR code for a given URL.

Example with no colors:

<p align="center">
  <img width="300" alt="qr-code-black" src="https://github.com/Alex188dot/QRCodeGenerator/assets/117444853/dc80a1c9-defd-4e3f-a273-a44b736797ed">
</p>

Example with colors (you can insert any hexadecimal color in the fields dark, for the QR code, and light, for the background):

<p align="center">
    <img width="300" alt="qr-code-yellow" src="https://github.com/Alex188dot/QRCodeGenerator/assets/117444853/97672b64-7ded-4b23-8876-b09c9efc5953">
</p>

## Requirements

- Python 3.6 or higher
- Segno 1.3.3 or higher

## Usage

- Install Segno with pip: `pip install segno`
- Run the script with Python: `python QRCodeGenerator.py`
- The script will create a PNG file named "Alessio's_Github.png" (or whatever you set it to) in the current directory, containing the QR code for https://github.com/Alex188dot (or the link you set it to)
- You can scan the QR code with your smartphone or any QR code reader app to access the URL
- You can modify the script to change the URL or the file name as you wish
