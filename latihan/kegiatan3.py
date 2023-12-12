from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan Pillow
image = Image.open("/Users/rian/Documents/MyDoc/Semester 5/Praktikum Fungsional/Modul6/percobaan_dua.jpg")

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(1.5)
enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
final_image.save("brightness_contrast_image.jpg")

# TODO 4: Tampilkan
final_image.show()
