# Pantry Defender

*A fun and mildly over-engineered solution to keep little ones out of the pantry.*

## Dedication
For my daughter, who found it fun to wake up at 04:30, raid the pantry, and proceed to feed our dogs Nutella.

## Purpose
This program is designed to deter small children from entering a pantry without parental consent. By utilizing **YOLOv8** and some creative coding, we can trigger voice messages through the computer's speakers when certain conditions are met.

## Requirements
- A **webcam** (any decent one should work).
- A **computer with sufficient processing power** (if performance is an issue, downgrade from `yolov8m` to `yolov8n`).

## Installation & Setup
To deploy **Pantry Defender** in your household, follow these steps:

### 1. Install Dependencies
Create a virtual environment and install the necessary dependencies:
```sh
pip install -r requirements.txt
```

### 2. Install YOLOv8 Weights
If you don’t already have `yolov8m.pt`, install it using Ultralytics:
```sh
pip install ultralytics
```

### 3. Train a Custom Model *(Optional)*
In my implementation, I trained a custom model using images of my daughter. If you want to do the same, refer to the [Ultralytics documentation](https://docs.ultralytics.com) for guidance on training YOLOv8 models.

### 4. Configure `main.py`
- Set your monitoring window by initializing the `ChocolateDefender` class.
- Define the time range when Pantry Defender should be active.

### 5. Adjust Audio Alerts
Replace the `.mp4` paths in the script with recordings of your own voice. *(MP3 files could work too, but I was too lazy to convert them from MP4 to MP3.)*

## Future Enhancements (TODO)
- 📱 **Phone notifications** for parents.
- 🔫 **Nerf gun deterrent** for extra security.
- 🏀 **Laundry basket trap** to gently contain intruders.
- 👨‍🦰 **Adult detection** (because we should probably avoid triggering alerts on ourselves).

---
**Enjoy defending your pantry!** 😆
