# AI Virtual Painter 🎨

This is an application that enables one to vitually paint in the air using their fingers. It is developed in python on openCV and Mediapipe. So go ahead and recreate your imaginations in the air !

![Alt text](paint.gif)

## Getting Started

- Use the command to clone this repository to your machine
`git clone https://github.com/darthdaenerys/Virtual-Painter`

- Now change current directory to the folder `cd Virtual-Painter`

- `pip install -r requirements.txt`

- `python paint.py`

## Features

- Can draw on your System screen based on your Index finger movement
- Can track your hand in real-time
- Change colour for your brush
- Change your brush size
- Save your beautiful creations by pressing `S`.
- Clear for a fresh screen by pressing `C`.
- Train for your own use case from scratch.

## Working

- This project is a use case of Hand Tracking technology.
- As soon as the user shows up his hand in the camera the application detects it.
- The left hand determines the `standby` or `drawing` mode.
- To Select different color or eraser from the top of Canvas, User must select it by taking his Index finger at the top of icon. The same can also be selected using mouse click.

## Note

Feel free to file a new issue with a respective title and description on the AI-Virtual-Paint. If you already found a solution to your problem, I would love to review your pull request!


# 🎨 AI Virtual Painter — Gesture-Controlled Digital Art System

An **AI-powered Virtual Painting System** that allows users to draw, erase, and create art **using only hand gestures** captured by a webcam.  
Built with **Python, OpenCV, and MediaPipe**, this project showcases the power of **computer vision, real-time hand tracking**, and **gesture-based interaction**.

![Virtual Painter Demo](paint.gif)

---

## 🚀 Features

✅ **Real-Time Hand Tracking** — Detects hand landmarks using MediaPipe with high accuracy.  
✅ **Air Drawing** — Draw and paint using your index finger — no mouse or touch needed.  
✅ **Gesture Modes** — Switch between drawing, erasing, and standby mode using simple hand gestures.  
✅ **Dynamic Brush & Color Control** — Change colors or brush sizes in real time.  
✅ **Save & Clear Canvas** — Press `S` to save your artwork or `C` to clear the screen.  
✅ **Custom Training Option** — Extend functionality by training your own gesture dataset.

---

## 🧠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python 3 |
| Computer Vision | OpenCV |
| Hand Tracking | MediaPipe |
| AI / ML | PyTorch, TensorFlow |
| Data Handling | NumPy, Pickle |
| Visualization | OpenCV GUI |

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Balaji-r-2004/Futuristic-Digital-Art-AI-Driven-Painting-with-Gesture-Automated-Shape-Precision.git
cd Futuristic-Digital-Art-AI-Driven-Painting-with-Gesture-Automated-Shape-Precision

pip install -r requirements.txt

python paint.py

🖐️ How It Works
🧩 This project uses MediaPipe to detect 21 hand landmarks in real-time.
Your index finger is used to draw on the virtual canvas.
The thumb and finger pinch gesture is used to switch tools (colors, eraser).
The left hand controls drawing mode (active / standby).

When your hand enters the camera frame:
Index finger movement → Draw
Pinch gesture → Change tool
Press S → Save artwork
Press C → Clear screen
Press Q → Quit

AI-Virtual-Painter/
│
├── paint.py                # Main application
├── handTracker.py          # Hand detection and tracking
├── sketch_corrector.py     # AI-based shape correction (PyTorch)
├── quickdraw_integration.py# Sketch recognition using QuickDraw
├── train.py                # Custom gesture training script
├── test_shapes.py          # Test for shape recognition
├── requirements.txt        # Project dependencies
└── README.md               # Documentation

💡 Future Enhancements
🧠 Add gesture-based undo/redo
🌈 Include voice command integration
💾 Cloud sync for saved artworks
📱 Deploy on web or mobile using TensorFlow.js

👨‍💻 Author

Balaji R
🎓 Final Year B.E. CSE | K.S. Institute of Technology
💡 Passionate about Python, AI, and Computer Vision
📫 LinkedIn
 | GitHub

📜 License

This project is open-source under the MIT License.
