import cv2

# ビデオキャプチャオブジェクトを作成
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

    # フレームを表示
    cv2.imshow('Camera', frame)

    # 'q'キーが押されたらループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# キャプチャを解放し、ウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()
