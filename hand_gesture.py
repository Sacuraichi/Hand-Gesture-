import cv2
from cvzone.HandTrackingModule import HandDetector
import math

# Initialize HandDetector with enhanced parameters
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Initialize webcam
cap = cv2.VideoCapture(0)

def get_gesture(hand):
    fingers = detector.fingersUp(hand)
    handType = hand["type"]
    
    # Identify gestures based on finger states
    total = sum(fingers)
    gesture = ""
    if total == 0:
        gesture = "Fist"
    elif total == 5:
        gesture = "Open Hand"
    elif fingers == [0, 1, 1, 0, 0]:
        gesture = "Peace"
    elif fingers == [0, 1, 0, 0, 0]:
        gesture = "One"
    elif fingers == [1, 0, 0, 0, 0]:
        gesture = "Thumbs Up"
    else:
        gesture = "Unknown"
    
    return f"{handType} Hand: {gesture}"

while True:
    success, frame = cap.read()
    if not success:
        break
    
    
    
    # Find hands
    hands, frame = detector.findHands(frame)
    
    if hands:
        y_position = 50
        for hand in hands:
            # Get and display gesture with hand type
            gesture = get_gesture(hand)
            cv2.putText(frame, gesture, (10, y_position), cv2.FONT_HERSHEY_SIMPLEX, 
                       1, (0, 255, 0), 2, cv2.LINE_AA)
            y_position += 50  # Offset for next text line
    
    # Display the frame
    cv2.imshow('Hand Gesture Recognition', frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()