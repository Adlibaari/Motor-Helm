# Motor-Helm
## Overview
Proyek ini bertujuan untuk mengembangkan sistem deteksi objek yang dapat mengidentifikasi pengendara motor yang menggunakan helm maupun yang tidak, sekaligus mendeteksi keberadaan motor itu sendiri. Sistem ini dirancang untuk mendukung pengecekan kepatuhan terhadap peraturan lalu lintas, terutama dalam memantau pengendara yang tidak menggunakan helm dan memastikan motor tidak berada di jalur yang tidak semestinya, seperti trotoar.

## Dataset
Dataset didapatkan dari gabungan dataset [helmet-detection Computer Vision Project](https://universe.roboflow.com/imagerecognition-43zpb/helmet-detection-ntbfz/dataset/14) dan beberapa gambar yang diambil dari internet yang memiliki gambar motor atau dan helm yang bervariasi. Setiap gambar pada dataset telah melalui proses augmentasi dengan dibalik dan diputar sebesar 15 derajat. Persebaran data yang digunakan adalah sebagai berikut:  
| Folder  | Image Count | 
| ------------- | ------------- |
| Train  | 11219 | 
| Validation | 493 | 
| Test | 469 |

## Model 
Proyek ini menggunakan model YOLOv11 sebagai algoritma deteksi objek utama, yang telah diimplementasikan dengan melakukan hyperparameter tuning untuk mengoptimalkan performa deteksi.

### Environment
- Quadro RTX 5000
- Python 3.12.1
- Pytorch 2.5.1
- Torchvision 0.20.1
- Torchaudio 2.5.1
- Ultralytics 8.3.39

### Hyper-parameter Tuning
Hyper-parameter tuning dilakukan dengan menggunakan fungsi model.tune yang disediakan pada library ultralytics untuk mencari learning rate yang terbaik. Tuning dilakukan sebanyak 25 iterasi dengan masing-masing iterasi dijalankan selama 100 epoch.

### Metrik Evaluasi
![image](https://github.com/user-attachments/assets/c4f633d2-7f8b-4960-886f-1ccd04d4b9af)

| Model | epoch  | Imgsz | lr0  | lrf | Recall  | Precision | mAP50  | mAP50-95 |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Baseline | 100  | 1280  | 0.01  | 0.01 | 0.93795  | 0.93714  | 0.96463 | 0.8126  |
| Hypertuned | 100  | 1280  | 0.01052  | 0.00898 | 0.93318  | 0.94045  | 0.96388 | 0.8156  |

### Hasil
![image](https://github.com/user-attachments/assets/d3671bc1-89a5-45f4-aa81-521d1eca5a86)







