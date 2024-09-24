import cv2
import os
import sys

# 同じディレクトリにあるface_recognition_module.pyをインポート
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from face_recognition_module import capture_frame

# メイン関数を呼び出す
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("カメラを開くことができませんでした")
        exit()

    while True:
        # フレームをキャプチャ
        ret, frame = cap.read()

        if not ret:
            print("フレームを取得できませんでした")
            break

        # キー入力を取得
        key = cv2.waitKey(1) & 0xFF

        # フレームを処理
        frame = capture_frame(frame, key)

        # フレームを表示
        cv2.imshow('Camera', frame)

        # 'q'キーが押されたらループを終了
        if key == ord('q'):
            break

    # リソースを解放
    cap.release()
    cv2.destroyAllWindows()