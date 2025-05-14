# Military Soldier Safety

This Python script analyzes an image (e.g., from a battlefield or surveillance feed) to detect high concentrations of red regions that could indicate danger zones like fire, explosions, or enemy presence. It uses computer vision techniques to classify the area as **Safe** or **Danger Zone** based on the number of red pixels detected.

## 🔍 Features

- Loads and processes an image using OpenCV.
- Converts the image to HSV color space for better color detection.
- Detects red-colored regions by combining two hue ranges.
- Classifies the image as:
  - ✅ **Safe Area**
  - 🚨 **Danger Zone Detected!**
- Annotates the result and saves the output image as `result.png`.

## 🧠 How It Works

1. **Image Loading**: Reads an image from the local path.
2. **Color Space Conversion**: Converts BGR to HSV for better color detection.
3. **Red Region Detection**: Detects red using two HSV hue ranges.
4. **Pixel Counting**: Counts red pixels using a mask.
5. **Decision Making**: If red pixels > 5000 → Danger Zone.
6. **Output**: Saves the annotated image with a message.

## 🖥️ Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Install dependencies:
  pip install opencv-python numpy

## 🚀 Usage
1. Place your battlefield image in the project directory as `battlefield.png`.
2. Run the script:
3. Check the generated file result.png for the annotated output.
   
## 📷 Sample Output
If a danger zone is detected, the text "Danger Zone Detected!" appears in red.
Otherwise, "Safe Area" appears in green.

## ⚠️ Notes
Ensure the image file is named battlefield.png or modify the image_path in the script.

Designed for environments where visual red indicators represent threats (e.g., thermal imaging, sensor feeds).

## 📌 Title
Military Soldier Safety

## 🛡️ License
This project is free to use and modify for academic and research purposes.

