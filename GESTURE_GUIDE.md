# AI Virtual Painter - Hand Gesture Guide

## Overview
The AI Virtual Painter now supports hand gestures to automatically draw perfect shapes. Use your left hand to make specific gestures, then draw with your right hand to create perfectly corrected shapes.

## Basic Controls
- **Left Hand**: Make gestures to select shapes
- **Right Hand**: Draw on the canvas
- **Left Fist**: Drawing mode (normal drawing)
- **Left Hand Open**: Selection mode (choose colors/brush sizes)

## Shape Gestures

### Circle
- **Gesture**: Thumb + Index finger (OK sign)
- **How to**: Extend thumb and index finger, keep other fingers closed
- **Result**: Perfect circle regardless of how you draw

### Square
- **Gesture**: Thumb + Index + Middle finger (3 fingers)
- **How to**: Extend thumb, index, and middle fingers, keep ring and pinky closed
- **Result**: Perfect square with equal sides

### Triangle
- **Gesture**: Thumb + Index + Middle + Ring finger (4 fingers)
- **How to**: Extend thumb, index, middle, and ring fingers, keep pinky closed
- **Result**: Perfect equilateral triangle

### Rectangle
- **Gesture**: All 5 fingers extended
- **How to**: Extend all fingers on your left hand
- **Result**: Perfect rectangle maintaining aspect ratio

### Diamond
- **Gesture**: Index + Middle finger (2 fingers, no thumb)
- **How to**: Extend only index and middle fingers, keep thumb and other fingers closed
- **Result**: Perfect diamond shape

### Star
- **Gesture**: Index + Middle + Ring finger (3 fingers, no thumb)
- **How to**: Extend index, middle, and ring fingers, keep thumb and pinky closed
- **Result**: Perfect 5-pointed star

### Heart
- **Gesture**: Index + Pinky finger (peace sign)
- **How to**: Extend index and pinky fingers, keep thumb, middle, and ring closed
- **Result**: Perfect heart shape

### Oval
- **Gesture**: Thumb + Pinky finger (hang loose)
- **How to**: Extend thumb and pinky fingers, keep other fingers closed
- **Result**: Perfect oval/ellipse

## Keyboard Shortcuts

- **A**: Toggle auto-correction on/off
- **H**: Show help with all available shapes and gestures
- **G**: Toggle gesture guide overlay
- **C**: Clear canvas
- **S**: Save image
- **Q**: Quit application

## How to Use

1. **Start the application**: Run `python paint.py`
2. **Make a gesture**: Use your left hand to make one of the shape gestures above
3. **Draw**: Use your right hand to draw on the canvas
4. **Result**: The shape will be automatically corrected to a perfect version

## Tips

- **Gesture Recognition**: Make sure your left hand is clearly visible to the camera
- **Drawing Area**: Draw with your right hand in the main canvas area (right side of screen)
- **Auto-correction**: Keep auto-correction enabled (default) for best results
- **Gesture Guide**: Press 'G' to see the gesture guide overlay while drawing
- **Help**: Press 'H' to see all available shapes and gestures in the console

## Troubleshooting

- **Gesture not detected**: Ensure good lighting and clear hand visibility
- **Shape not correcting**: Make sure auto-correction is enabled (press 'A' to toggle)
- **Camera issues**: Check camera settings in `settings.json`
- **Performance**: Close other applications to improve frame rate

## Supported Shapes

The system can auto-correct the following shapes:
- Circle
- Square
- Rectangle
- Triangle
- Diamond
- Star
- Heart
- Oval

Each shape has its own gesture for forced correction, or the system can auto-detect shapes when no specific gesture is made.

