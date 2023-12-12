from PIL import Image

# TODO 0: Import beberapa library lain yang dibutuhkan

# TODO 1: Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open("/Users/rian/Documents/MyDoc/background.jpg")
overlay_image = Image.open("/Users/rian/Documents/MyDoc/olaf.png")

# TODO 2: Konversi overlay image ke mode RGBA (menghilangkan alpha channel)
overlay_image = overlay_image.convert("RGBA")

# TODO 3: (optional) Perkecil ukuran gambar overlay menggunakan method resize()
overlay_image = overlay_image.resize((120, 160))  # Ganti ukuran sesuai kebutuhan

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# TODO 4: Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center), overlay_image)

# TODO 5: Simpan gambar hasil edit
background_image.save("percobaan_dua.jpg")

# TODO 6: Tampilkan hasil edit gambar
background_image.show()
