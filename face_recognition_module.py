import cv2

def capture_frame(frame, key):
    if key == ord('c'):
        # フレームを保存
        cv2.imwrite('captured_frame.jpg', frame)
        print("Frame captured and saved as 'captured_frame.jpg'")
    return frame