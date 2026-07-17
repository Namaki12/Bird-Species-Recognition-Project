# BIRD SPECIES RECOGNITION
Bird Species Recognition merupakan proyek Machine Learning berbasis Python yang mampu mengidentifikasi spesies burung berdasarkan rekaman suara (audio berformat .mp3).
Proyek ini menggunakan algoritma Random Forest Classifier dan metode ekstraksi fitur MFCC (Mel Frequency Cepstral Coefficients) untuk mengenali pola suara dari berbagai spesies burung.
---

## FITUR PROGRAM
Program ini memiliki beberapa fitur, di antaranya:
- Klasifikasi spesies burung berdasarkan suara.
- Mendukung 12 spesies burung.
- Ekstraksi fitur audio menggunakan MFCC.
- Menggunakan algoritma Random Forest Classifier.
- Menampilkan Confidence Score (tingkat keyakinan prediksi).
- Mendeteksi spesies burung yang tidak terdapat pada dataset.
- Validasi dataset audio secara otomatis.
- Evaluasi model menggunakan Cross Validation.
- Menampilkan Classification Report.
- Menampilkan Confusion Matrix.
- Mudah digunakan melalui terminal (Command Prompt).
---

## DAFTAR SPESIES BURUNG
|  Nama Ilmiah  |  Nama Umum  |
|---------------|-------------|
| Grallaria_cochabambae | Bolivian Antpitta |
| Grallaria_saltuensis | Perija Antpitta |
| Grallaria_saturata | Equatorial Antpitta |
| Grallaria_spatiator | Sierra Nevada Antpitta |
| Penelope_bridgesi | Yungas Guan |
| Pyriglena_similis | Tapajos Fire-eye |
| Pyriglena_maura | Western Fire-eye |
| Sitta_insularis | Bahama Nuthatch |
| Basileuterus_delattrii | Chestnut-capped Warbler |
| Phylloscopus_nesophilus | Sulawesi Leaf Warbler |
| Pitta_concinna | Ornate Pitta |
| Larvivora_namiyei | Okinawa Robin |
---

## STRUKTUR FOLDER PROYEK
```
Bird Species Recognition Project
│
├── dataset
│   ├── Grallaria_cochabambae
│   ├── Grallaria_saltuensis
│   ├── Grallaria_saturata
│   ├── Grallaria_spatiator
│   ├── Penelope_bridgesi
│   ├── Pyriglena_similis
│   ├── Pyriglena_maura
│   ├── Sitta_insularis
│   ├── Basileuterus_delattrii
│   ├── Phylloscopus_nesophilus
│   ├── Pitta_concinna
│   └── Larvivora_namiyei
│
├── Main_Code
│   ├── testAudio.py
│   ├── trainModel.py
│   └── predict.py
│
├── Model
│   └── bird_model.pkl
│
└── Test_Audio
    └── Uji.mp3
```

## LIBRARY YANG DIGUNAKAN
Pastikan seluruh library berikut telah terinstal !!
```bash
pip install librosa numpy scikit-learn joblib
```

Library yang digunakan:
- Librosa
- NumPy
- Scikit-Learn
- Joblib
---

## ALUR KERJA PROGRAM
```
Audio Burung (.mp3)
          ↓
    Normalize Audio
          ↓
      Trim Silence
          ↓
    MFCC (40 Fitur)
          ↓
 Train-Test Split (80 : 20)
          ↓
 Random Forest Classifier
          ↓
 Cross Validation (5 Fold)
          ↓
      Evaluasi Model
          ↓
     Simpan Model (.pkl)
          ↓
      Prediksi Audio
          ↓
      Confidence Score
          ↓
 Identifikasi Spesies Burung
---

## INFORMASI DATASET
Dataset yang digunakan memiliki spesifikasi sebagai berikut:

|  Keterangan  |  Jumlah  |
|--------------|----------|
| Total Spesies Burung | 12 |
| Total Audio | 238 |
| Rata-rata Audio per Spesies | 19,75 |
| Format Audio | .mp3 |
| Sampling Rate | 22050 Hz |
---

## REKOMENDASI DATASET AUDIO
Agar memperoleh hasil prediksi yang optimal, audio yang digunakan disarankan memiliki karakteristik berikut:
- Durasi audio 1 - 3 detik.
- Suara burung terdengar jelas.
- Noise atau suara latar belakang seminimal mungkin.
- Menggunakan format .mp3.
- Memiliki sampling rate 22050 Hz.
---

## PERFORMA MODEL
Berdasarkan hasil pelatihan model, diperoleh hasil evaluasi sebagai berikut:

| Metode Evaluasi | Hasil |
|-----------------|-------|
| Accuracy Score | 97,92% |
| Cross Validation Score | 89,42% |

Hasil pengujian tambahan:
- Tingkat keberhasilan prediksi pada audio uji yang digunakan mencapai 100%.
> Catatan: Hasil pengujian dapat berbeda tergantung kualitas audio yang digunakan.
---

## CARA MENJALANKAN PROGRAM

### 1. Mengecek Dataset
Jalankan perintah berikut:
```bash
python testAudio.py
```

Program akan melakukan:
- Validasi seluruh file audio.
- Menampilkan durasi audio.
- Menampilkan sampling rate.
- Menampilkan jumlah audio pada masing-masing spesies.
- Menampilkan ringkasan dataset.
---

### 2. Melatih Model
Jalankan perintah berikut:
```bash
python trainModel.py
```

Program akan melakukan:
- Membaca seluruh dataset.
- Melakukan ekstraksi fitur MFCC.
- Melatih model Random Forest.
- Mengevaluasi performa model.
- Menyimpan model secara otomatis.

Output yang dihasilkan:
```
bird_model.pkl
```
File model akan tersimpan pada folder:
```
model/
```

### 3. Menguji Audio Burung
Masukkan audio yang ingin diuji ke dalam folder berikut:
```
test_audio/
```

Contoh:
```
test_audio/
Uji.mp3
```

Kemudian jalankan:
```bash
python predict.py
---

## Contoh Hasil Prediksi
```
==========================================
BIRD SPECIES RECOGNITION
==========================================
Scientific Name :
Pitta_concinna

Common Name :
Ornate Pitta

Prediction Status :
KNOWN BIRD SPECIES

Confidence Score :
91.52 %
==========================================
```

---

## Deteksi Spesies Burung yang Tidak Dikenali
Apabila audio yang dimasukkan bukan merupakan salah satu dari 12 spesies pada dataset, maka program akan menampilkan:

```
Prediction :
UNKNOWN BIRD SPECIES

Confidence Score :
18.45 %
```

Fitur ini memungkinkan program untuk mengidentifikasi bahwa audio yang diberikan tidak sesuai dengan spesies yang telah dipelajari oleh model.
---

## Catatan Penggunaan
Untuk memperoleh hasil prediksi yang lebih akurat, disarankan untuk:
- Menggunakan dataset sebanyak mungkin sebagain bahan train dari program
- Menggunakan audio yang memiliki suara burung yang jelas.
- Menggunakan durasi audio sekitar 1 - 3 detik.
- Meminimalkan noise pada audio.
- Menggunakan karakteristik audio yang serupa dengan dataset pelatihan.
- Menggunakan format file .mp3.
---

## Pengembangan Selanjutnya
Beberapa pengembangan yang dapat dilakukan pada proyek ini antara lain:
- Prediksi beberapa audio sekaligus (Batch Prediction).
- Pembuatan antarmuka grafis (GUI).
- Visualisasi Spectrogram suara burung.
- Implementasi Deep Learning (CNN).
- Prediksi suara burung secara real-time.
- Pengembangan aplikasi berbasis mobile atau web.
---

## Penulis
Proyek Bird Species Recognition dikembangkan menggunakan:
- Python 3.11.9
- Librosa
- NumPy
- Scikit-Learn
- Random Forest Classifier
- MFCC (Mel Frequency Cepstral Coefficients)
