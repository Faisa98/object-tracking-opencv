# 🎯 Object Tracking with OpenCV

This project demonstrates how to track a selected object in a video using OpenCV's built-in tracking algorithms.  
The user selects a region in the first frame, and the tracker follows it through the rest of the video.

---

## 📸 Demo

https://github.com/user-attachments/assets/3fc1034e-8b0d-410b-86b5-a81d41faa8e4


---

## 🧰 Technologies Used

- Python 3.x
- OpenCV (`opencv-contrib-python` for tracking modules)

---

## 🚀 How It Works

1. The script opens a video file.
2. The user selects the object to track in the first frame.
3. OpenCV's tracker (default: `CSRT`) begins following the object.
4. A green rectangle shows the tracked object in each frame.

---

## 📦 Installation

1. Clone this repo:
```bash
git clone https://github.com/Faisa98/object-tracking-opencv.git
cd object-tracking-opencv
