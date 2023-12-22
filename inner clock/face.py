from deepface import DeepFace
import cv2


# 웹캠 또는 비디오 파일에서 프레임을 읽어옴
cap = cv2.VideoCapture(0)
time =1
while True:

    try:
        ret, frame = cap.read()

        # DeepFace를 사용하여 얼굴 감정 분석 수행
        result = DeepFace.analyze(frame, actions=('emotion'))

        # 감정 결과 출력
        x= result[0]
        e = x["dominant_emotion"]
        if e == "happy":
            new_time = time*1.4
            sdf =str(new_time)+ " per sec"
            
        elif e == "sad":
            new_time = time*0.8
            sdf = str(new_time)+ " per sec"
        elif e == "angry":
            new_time = time*0.8
            sdf = str(new_time)+ " per sec"
        else:
            new_time = time
            sdf = str(new_time)+ " per sec"
        

        
        cv2.putText(frame, f"Emotion: {e}     {sdf}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
    
        
        # 화면에 출력
        cv2.imshow('Emotion Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except ValueError:
        pass

# 작업 완료 후 비디오 캡처 객체 해제
cap.release()
cv2.destroyAllWindows()