### Uykulu/Uykusuz Tespiti OpenCV&Python 😴 🚫 🚗 
##
Bu kod araba süren bir kişinin uykulu/uykusuz tespitini yapıyor.
### Neden kullanılır ? 🎯
##
Sürücüler yolda giderken uyuyup kazaya yol açıyor. Bu uygulama uyumayı engelliyor ve kaza riskini büyük ölçüde azaltıyor.
##
### Kod için gereksinimler
Python

## Dependencies
1.import cv2 <br>
2.import dlib <br>
3.from scipy.spatial import distance as dist <br>
4.import time <br>
5.import pygame <br>
6.import threading <br>
7.from imutils import face_utils

### Tanım 📌
Gerçek zamanlı bir video akışında sürücünün uykulu olduğunu otomatik olarak algılayabilen ve ardından sürücü uykulu görünüyorsa alarm çalabilen bir bilgisayar görüş sistemi.

### Algoritma 
Her göz, gözün sol köşesinden başlayan (sanki kişiye bakıyormuşsunuz gibi) ve ardından göz çevresinde saat yönünde ilerleyen 6 (x, y) koordinatıyla temsil edilir.

Eye Thresh hold oranı 0.25'ten küçükse ve calculate_blink_duration > Blink_Duration'den büyükse uyarı oluşturur.

### İlişki
<img src="https://github.com/mehmetuner/goruntuproje/blob/main/fotograflar/03-driver-drowsiness-detection-EAR-points.png" alt="alt text" width="320" height="180">
<img src="https://github.com/mehmetuner/goruntuproje/blob/main/fotograflar/12-driver-drowsiness-detection-AVG_EAR-equation.png" alt="alt text" width="320" height="180">

### Özetle

<img src="https://github.com/mehmetuner/goruntuproje/blob/main/fotograflar/eye3.jpg" alt="alt text" width="320" height="180">

### Sonuç
