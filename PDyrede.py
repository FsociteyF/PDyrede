#!/usr/bin/env python3

import os
import qrcode

def banner():
    print("""
  ____  ____       ____          _      
 |  _ \|  _ \ _   _|  _ \ ___  __| | ___ 
 | |_) | | | | | | | |_) / _ \/ _` |/ _ \\
 |  __/| |_| | |_| |  _ <  __/ (_| |  __/
 |_|   |____/ \__, |_| \_\___|\__,_|\___|
              |___/                     
    """)
    print("Simple QR Code Generator - fsocitey")

def generate_qr(url, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"\n[+] QR Code saved as {os.path.abspath(filename)}\n")

def main():
    banner()
    link = input("[*] Enter the URL to generate QR Code" \
    " ضع الرابط لحقنه في البار كود:  ").strip()
    if not link:
        print("[-] You must enter a URL!")
        return

    filename = input("[*] Enter filename to save (default: qrcode.png)" \
    " ضع اسم للبار كود:  ").strip()
    if not filename:
        filename = "qrcode.png"
    
    generate_qr(link, filename)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Exiting...")

