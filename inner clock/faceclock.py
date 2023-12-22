from deepface import DeepFace
import cv2
import tkinter
import math
from datetime import datetime

class clock(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.x = 150
        self.y = 150
        selfx1 =self.x + 300
        self.geometry('600x300')
        self.hour_length = 30
        self.canvas = tkinter.Canvas(self, bg='white')
        self.canvas.pack(expand='yes', fill='both')

        hour_stick = self.canvas.create_line(
                                    self.x, self.y,
                                    self.x + self.hour_length, self.y + self.hour_length,
                                    width=3, fill="white")
        hour_stick1 = self.canvas.create_line(
                                    selfx1, self.y,
                                    selfx1 + self.hour_length , self.y + self.hour_length,
                                    width=3, fill="white")
        min_stick = self.canvas.create_line(
                                    self.x, self.y,
                                    self.x + self.hour_length, self.y + self.hour_length,
                                    width=3, fill="white")
        min_stick1 = self.canvas.create_line(
                                    selfx1, self.y,
                                    selfx1+self.hour_length, self.y + self.hour_length,
                                    width=3, fill="white")

        
        sec_stick = self.canvas.create_line(
                                    self.x, self.y,
                                    self.x + self.hour_length, self.y + self.hour_length,
                                    width=1, fill="blue")
        sec_stick1 = self.canvas.create_line(
                                    selfx1, self.y,
                                    selfx1 + self.hour_length, self.y + self.hour_length,
                                    width=1, fill="blue")
        
        self.sticks = [hour_stick, min_stick, sec_stick]
        self.sticks1 = [hour_stick1,min_stick1, sec_stick1]

        fsize = 13
        fcolor = "black"
        self.canvas.create_text(10, 150, text="9", font=("나눔고딕코딩", fsize), fill=fcolor)
        self.canvas.create_text(150, 10, text="12", font=("나눔고딕코딩", fsize), fill=fcolor)
        self.canvas.create_text(290, 150, text="3", font=("나눔고딕코딩", fsize), fill=fcolor)
        self.canvas.create_text(150, 290, text="6", font=("나눔고딕코딩", fsize), fill=fcolor)
        self.canvas.create_text(310, 150, text="9", font=("나눔고딕코딩", fsize), fill=fcolor)
        self.canvas.create_text(450, 10, text="12", font=("나눔고딕코딩", fsize), fill=fcolor)
        self.canvas.create_text(590, 150, text="3", font=("나눔고딕코딩", fsize), fill=fcolor)
        self.canvas.create_text(450, 290, text="6", font=("나눔고딕코딩", fsize), fill=fcolor)
        
        w = 150
        h = 150
        r = 130
        x0 = w - r
        y0 = h - r
        x1 = w + r
        y1 = h + r
        self.canvas.create_oval(x0, y0, x1, y1)
        self.canvas.create_oval(x0+300, y0, x1+300, y1)
    
    def update_clock(self, hour_speed = 1,min_speed=1,sec_speed=1):
        current_time = datetime.now()
        str_time = current_time.strftime("%I%M%S")

        current_time1 = datetime.now()
        str_time1 = current_time1.strftime("%I%M%S")

        _hour = int(str_time[0:2]) * 5
        _min = int(str_time[2:4])
        _sec = int(str_time[4:6])

        _hour1 = int(str_time1[0:2]) * 5
        _min1 = int(str_time1[2:4])
        _sec1 = int(str_time1[4:6])

        # x, y = self.canvas.coords(self.sticks[0])[0:2]
        # x2 = (self.hour_length + 50) * math.cos(math.radians(_hour * 6) - math.radians(90)) + self.x
        # y2 = (self.hour_length + 50) * math.sin(math.radians(_hour * 6) - math.radians(90)) + self.y
        # self.canvas.coords(self.sticks[0], tuple([x, y, x2, y2]))

        # x, y = self.canvas.coords(self.sticks1[0])[0:2]
        # x2 = (self.hour_length + 50) * math.cos(math.radians(_hour1 * 6*hour_speed) - math.radians(90)) + self.x +300
        # y2 = (self.hour_length + 50) * math.sin(math.radians(_hour1 * 6*hour_speed) - math.radians(90)) + self.y
        # self.canvas.coords(self.sticks1[0], tuple([x, y, x2, y2]))

        # x, y = self.canvas.coords(self.sticks[1])[0:2]
        # x2 = (self.hour_length + 90) * math.cos(math.radians(_min * 6) - math.radians(90)) + self.x
        # y2 = (self.hour_length + 90) * math.sin(math.radians(_min * 6) - math.radians(90)) + self.y
        # self.canvas.coords(self.sticks[1], tuple([x, y, x2, y2]))

        # x, y = self.canvas.coords(self.sticks1[1])[0:2]
        # x2 = (self.hour_length + 90) * math.cos(math.radians(_min1 * 6*min_speed) - math.radians(90)) + self.x+300
        # y2 = (self.hour_length + 90) * math.sin(math.radians(_min1 * 6*min_speed) - math.radians(90)) + self.y
        # self.canvas.coords(self.sticks1[1], tuple([x, y, x2, y2]))

        x, y = self.canvas.coords(self.sticks[2])[0:2]
        x2 = (self.hour_length + 90) * math.cos(math.radians(_sec * 6) - math.radians(90)) + self.x
        y2 = (self.hour_length + 90) * math.sin(math.radians(_sec * 6) - math.radians(90)) + self.y
        self.canvas.coords(self.sticks[2], tuple([x, y, x2, y2]))

        x, y = self.canvas.coords(self.sticks1[2])[0:2]
        x2 = (self.hour_length + 90) * math.cos(math.radians(_sec1 * 6*sec_speed) - math.radians(90)) + self.x+300
        y2 = (self.hour_length + 90) * math.sin(math.radians(_sec1 * 6*sec_speed) - math.radians(90)) + self.y
        self.canvas.coords(self.sticks1[2], tuple([x, y, x2, y2]))


# 웹캠 또는 비디오 파일에서 프레임을 읽어옴
cap = cv2.VideoCapture(0)
time =1
clock = clock()
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
        
        clock.update()
        clock.update_clock(hour_speed=1,min_speed=1,sec_speed=new_time)

        
        # 화면에 출력
        cv2.imshow('Emotion Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
    except ValueError:
        pass
  

# 작업 완료 후 비디오 캡처 객체 해제
cap.release()
cv2.destroyAllWindows()


