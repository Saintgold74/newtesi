#!/usr/bin/env python3
"""
Genera QR Code per accesso rapido al repository GitHub
"""

import qrcode
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

def generate_repository_qr():
    """
    Genera QR code per il repository GIST Framework
    """

    # URL del repository
    repo_url = "https://github.com/gist-framework/gdo-security"

    # Crea QR code con alta correzione errori
    qr = qrcode.QRCode(
        version=1,  # controls size (1 = 21x21)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,
        border=4,
    )

    # Aggiungi dati e ottimizza
    qr.add_data(repo_url)
    qr.make(fit=True)

    # Crea immagine
    img = qr.make_image(fill_color="black", back_color="white")

    # Converti in PIL Image per aggiungere testo
    img = img.convert('RGB')

    # Aggiungi margine e testo sotto
    width, height = img.size
    new_height = height + 100
    new_img = Image.new('RGB', (width, new_height), 'white')
    new_img.paste(img, (0, 0))

    # Aggiungi testo descrittivo
    draw = ImageDraw.Draw(new_img)

    # Font fallback se non disponibile il font specifico
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("arial.ttf", 20)
        font_small = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Testo centrato
    text1 = "GIST Framework"
    text2 = "github.com/gist-framework/gdo-security"

    # Calcola posizione centrale (approssimativa)
    text1_x = (width - len(text1) * 10) // 2
    text2_x = (width - len(text2) * 7) // 2

    draw.text((text1_x, height + 20), text1, fill='black', font=font)
    draw.text((text2_x, height + 50), text2, fill='gray', font=font_small)

    # Salva in formati multipli
    new_img.save('qr_code_repository.png', 'PNG')
    new_img.save('qr_code_repository.pdf', 'PDF')

    print(f"QR Code generato:")
    print(f"   - qr_code_repository.png")
    print(f"   - qr_code_repository.pdf")
    print(f"   URL: {repo_url}")

    # Mostra preview
    plt.figure(figsize=(6, 7))
    plt.imshow(new_img)
    plt.axis('off')
    plt.title('QR Code - GIST Framework Repository', pad=20)
    plt.tight_layout()
    plt.savefig('qr_code_repository_preview.png', dpi=150, bbox_inches='tight')
    plt.show()

def generate_simple_qr():
    """
    Genera versione semplice senza dipendenze extra
    """
    import qrcode

    repo_url = "https://github.com/gist-framework/gdo-security"

    # QR semplice
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(repo_url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('qr_code_repository_simple.png')

    print(f"QR Code semplice generato: qr_code_repository_simple.png")

if __name__ == "__main__":
    try:
        # Prova versione completa
        generate_repository_qr()
    except ImportError as e:
        print(f"Alcune dipendenze mancanti: {e}")
        print("Generazione QR code semplice...")

        # Fallback a versione semplice
        try:
            generate_simple_qr()
        except ImportError:
            print("\nErrore: qrcode non installato")
            print("Installa con: pip install qrcode[pil]")

            # Istruzioni manuali
            print("\nAlternativa: Genera QR code online")
            print("1. Vai su: https://www.qr-code-generator.com/")
            print("2. Inserisci: https://github.com/gist-framework/gdo-security")
            print("3. Scarica come PNG")
            print("4. Salva come: figure/qr_code_repository.png")