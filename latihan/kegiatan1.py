from PIL import Image, ImageDraw, ImageFont

# TODO 1: Load image
gambarku = Image.open("/Users/rian/Documents/MyDoc/lambang umm.png")

# TODO 2: Ubah gambar menjadi hitam-putih
grayscale_image = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(grayscale_image)
font_path = "/Users/rian/Downloads/New folder (6)/arialn/Arialn.ttf" 
font_size = 24
font = ImageFont.truetype(font_path, font_size)
text = "Nama: Aprizal Triansyah\nNIM: 202110370311039"

# Gunakan textbbox untuk mendapatkan bounding box
text_bbox = draw.textbbox((0, 0), text, font=font)

# Extract width and height from the bounding box
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Koordinat untuk menempatkan teks di tengah gambar
text_x = (grayscale_image.width - text_width) // 2
text_y = (grayscale_image.height - text_height) // 2

draw.text((text_x, text_y), text, font=font, fill=150)

# TODO 4: Simpan gambar hasil edit
grayscale_image.save("percobaan_satu.jpg")

# TODO 5: Tampilkan hasil akhir gambar
grayscale_image.show()
