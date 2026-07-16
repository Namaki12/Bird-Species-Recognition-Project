# Bird Species Recognition using Machine Learning

## Deskripsi Proyek

Bird Species Recognition merupakan proyek Machine Learning yang dibuat untuk mengidentifikasi spesies burung berdasarkan rekaman suara (audio).

Program ini menggunakan:
- Python 3.11.9
- Librosa (Audio Processing)
- MFCC (Mel Frequency Cepstral Coefficients)
- Random Forest / K-Nearest Neighbors (Machine Learning Classification)
- Joblib (Model Saving)
- NumPy
- Scikit-Learn

Program mampu:
- Mengidentifikasi 12 spesies burung berdasarkan suara.
- Memprediksi spesies dari audio baru.
- Menampilkan confidence score hasil prediksi.
- Mendeteksi audio yang tidak dikenali (Unknown Bird Species).
---

## Daftar Spesies Burung
1. Grallaria cochabambae
2. Grallaria saltuensis
3. Grallaria saturata
4. Grallaria spatiator
5. Penelope bridgesi
6. Pyriglena similis
7. Pyriglena maura
8. Sitta insularis
9. Basileuterus delattrii
10. Phylloscopus nesophilus
11. Pitta concinna
12. Larvivora namiyei
---

## Struktur Folder
Bird Species Recognition Project
```
- dataset
- main_code
    - test_audio.py
    - train_model.py
    - predict.py
- model
    - test_audio
- README.md
---

## Requirement
### Python Version
```
Python 3.11.9
```

### Library yang Digunakan
Install seluruh library berikut:
```bash
pip install librosa
pip install numpy
pip install scikit-learn
pip install joblib
```

atau sekaligus:
```bash
pip install librosa numpy scikit-learn joblib
---

## Dataset Requirement
Format audio yang didukung:
```
.mp3
```

Struktur dataset:
```
dataset
- Pitta_concinna
    - Pitta_Concinna_1.mp3
    - Pitta_Concinna_2.mp3
      ...
- Larvivora_namiyei
    - Larvivora_Namiyei_1.mp3
    - Larvivora_Namiyei_2.mp3
    ...
---

## Rekomendasi Dataset
Untuk mendapatkan hasil klasifikasi yang lebih baik:
- Gunakan audio berdurasi 5-10 detik.
- Pastikan suara burung terdengar jelas.
- Hindari audio yang terlalu banyak noise.
- Hindari audio yang didominasi suara angin atau burung lain.
- Gunakan minimal 8-10 audio per spesies.
- Semakin banyak dataset, semakin baik performa model.
---

## Preprocessing Audio
Jika audio yang diperoleh berdurasi panjang (20 detik hingga 1 menit), disarankan untuk:
1. Memotong audio menjadi beberapa clip.
2. Mengambil bagian yang memiliki suara burung paling jelas.
3. Menggunakan durasi sekitar 5-10 detik setiap clip.

Contoh:
```
Audio Asli:
60 detik
↓
Dipotong menjadi:
- 8 detik
- 7 detik
- 9 detik
- 10 detik
```
Metode ini akan:
- Mengurangi noise.
- Memperbanyak jumlah data training.
- Meningkatkan akurasi model.
---

## Cara Menjalankan Program
### 1. Testing Dataset
Masuk ke folder:
```
main_code
```
Kemudian jalankan:
```bash
python test_audio.py
```
Program akan mengecek seluruh file audio pada dataset.

---
### 2. Training Model
Masuk ke folder:
```
main_code
```
Jalankan:
```bash
python train_model.py
```

Output:
```
Training berhasil!
Model berhasil disimpan!
```
File model akan disimpan pada:
```
model/bird_model.pkl
---

### 3. Melakukan Prediksi
Masukkan file audio yang ingin diuji ke dalam folder:
```
test_audio
```
Contoh:
```
test_audio
↓
uji.mp3
```
Kemudian jalankan:
```bash
python predict.py
---

## Contoh Output
```
====================================
BIRD SPECIES RECOGNITION
====================================
Scientific Name :
Pitta_concinna

Common Name :
Ornate Pitta

Confidence Score :
96.45 %
====================================
---

## Unknown Bird Species Detection
Jika confidence score berada di bawah threshold tertentu (misalnya 70%), maka sistem dapat memberikan output:
```
Unknown Bird Species
```

Contoh:
```
====================================
BIRD SPECIES RECOGNITION
====================================
Prediction :
Unknown Bird Species

Confidence Score :
43.26 %
====================================
```

Hal ini dilakukan agar sistem tidak memaksakan klasifikasi terhadap audio yang berada di luar dataset.
---

## Alur Kerja Sistem
```
Input Audio
      ↓
Audio Processing
      ↓
Feature Extraction (MFCC)
      ↓
Machine Learning Training
      ↓
Model Generation
      ↓
Input Audio Baru
      ↓
Feature Extraction
      ↓
Prediction
      ↓
Confidence Score
      ↓
Known Species / Unknown Species
---

## Metode yang Digunakan
### Audio Processing
Library:
- Librosa

### Feature Extraction
Metode:
- MFCC (Mel Frequency Cepstral Coefficients)

### Machine Learning
Algoritma:
- Random Forest Classifier
atau
- K-Nearest Neighbors (KNN)

### Model Saving
Library:
- Joblib
---