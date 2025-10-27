#!/usr/bin/env python3
"""
Test script for shape detection and auto-correction functionality
"""

import numpy as np
import cv2
from sketch_corrector import SketchCorrector

def test_shape_detection():
    """Test shape detection with sample strokes"""
    corrector = SketchCorrector()
    
    # Test circle
    print("Testing circle detection...")
    angles = np.linspace(0, 2*np.pi, 50)
    center = np.array([100, 100])
    radius = 50
    circle_stroke = np.array([
        center + radius * np.array([np.cos(angle), np.sin(angle)]) + np.random.normal(0, 5, 2)
        for angle in angles
    ])
    
    detected = corrector.detect_shape(circle_stroke)
    print(f"Detected shape: {detected}")
    
    # Test square
    print("\nTesting square detection...")
    square_stroke = np.array([
        [50, 50], [150, 50], [150, 150], [50, 150], [50, 50]
    ])
    detected = corrector.detect_shape(square_stroke)
    print(f"Detected shape: {detected}")
    
    # Test triangle
    print("\nTesting triangle detection...")
    triangle_stroke = np.array([
        [100, 50], [50, 150], [150, 150], [100, 50]
    ])
    detected = corrector.detect_shape(triangle_stroke)
    print(f"Detected shape: {detected}")
    
    print(f"\nAvailable shapes: {corrector.get_available_shapes()}")

def test_shape_correction():
    """Test shape correction with visual output"""
    corrector = SketchCorrector()
    
    # Create a canvas
    canvas = np.zeros((400, 600, 3), dtype=np.uint8)
    
    # Test circle correction
    print("Testing circle correction...")
    angles = np.linspace(0, 2*np.pi, 30)
    center = np.array([150, 150])
    radius = 60
    # Create imperfect circle
    imperfect_circle = np.array([
        center + radius * np.array([np.cos(angle), np.sin(angle)]) + np.random.normal(0, 15, 2)
        for angle in angles
    ])
    
    # Detect and correct
    detected = corrector.detect_shape(imperfect_circle)
    corrected = corrector.correct_stroke(imperfect_circle, detected)
    
    # Draw original (red) and corrected (green)
    for i in range(len(imperfect_circle) - 1):
        cv2.line(canvas, tuple(imperfect_circle[i].astype(int)), 
                tuple(imperfect_circle[i+1].astype(int)), (0, 0, 255), 3)
    
    for i in range(len(corrected) - 1):
        cv2.line(canvas, tuple(corrected[i]), tuple(corrected[i+1]), (0, 255, 0), 3)
    
    cv2.putText(canvas, f"Detected: {detected}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Test square correction
    print("Testing square correction...")
    imperfect_square = np.array([
        [300, 100], [450, 120], [430, 250], [280, 230], [300, 100]
    ])
    
    detected = corrector.detect_shape(imperfect_square)
    corrected = corrector.correct_stroke(imperfect_square, detected)
    
    # Draw original (red) and corrected (green)
    for i in range(len(imperfect_square) - 1):
        cv2.line(canvas, tuple(imperfect_square[i].astype(int)), 
                tuple(imperfect_square[i+1].astype(int)), (0, 0, 255), 3)
    
    for i in range(len(corrected) - 1):
        cv2.line(canvas, tuple(corrected[i]), tuple(corrected[i+1]), (0, 255, 0), 3)
    
    cv2.putText(canvas, f"Detected: {detected}", (300, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Show result
    cv2.imshow("Shape Correction Test", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Testing shape detection and correction...")
    test_shape_detection()
    test_shape_correction()
    print("Test completed!")

