import matplotlib.pyplot as plt

# Data nilai siswa
data_nilai = [
    {'siswa': 'Siswa 1', 'nilai': 80},
    {'siswa': 'Siswa 2', 'nilai': 90},
    {'siswa': 'Siswa 3', 'nilai': 75},
    {'siswa': 'Siswa 4', 'nilai': 85},
    {'siswa': 'Siswa 5', 'nilai': 92},
    {'siswa': 'Siswa 6', 'nilai': 78},
    {'siswa': 'Siswa 7', 'nilai': 88},
    {'siswa': 'Siswa 8', 'nilai': 95},
    {'siswa': 'Siswa 9', 'nilai': 70},
    {'siswa': 'Siswa 10', 'nilai': 82},
]

# Fungsi High Order untuk menghitung rata-rata nilai
calculate_average = lambda values: sum(values) / len(values)

# Fungsi Lambda untuk mendapatkan hanya nama siswa dari setiap item
get_student_name = lambda student: student['siswa']

# Menggunakan Map dan Lambda untuk mendapatkan list nama siswa
student_names = list(map(get_student_name, data_nilai))

# Menggunakan Map dan fungsi High Order untuk menghitung rata-rata nilai
average_score = calculate_average(list(map(lambda student: student['nilai'], data_nilai)))

# Fungsi High Order untuk mendapatkan siswa dengan nilai di atas rata-rata
get_above_average_students = lambda student: student['siswa'] if student['nilai'] > average_score else None
above_average_students = list(filter(None, map(get_above_average_students, data_nilai)))

# Membuat grafik batang
plt.bar(student_names, list(map(lambda student: student['nilai'], data_nilai)))
plt.axhline(y=average_score, color='red', linestyle='--', label='Rata-rata Nilai')  # Garis merah menunjukkan rata-rata nilai
plt.xlabel('Siswa')
plt.ylabel('Nilai')
plt.title('Grafik Nilai Siswa Kelas A')
plt.legend()
plt.show()

# Cetak hasil secara fungsional
print(f"Rata-rata nilai siswa: {average_score:.2f}")
print("Siswa dengan nilai di atas rata-rata:")
