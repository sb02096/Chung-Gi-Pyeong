import turtle as t
import random
a=random.randint(0,360) # 원의 초기출발 각도를 설정할 수를 a에 저장
t.shape('turtle') # 모양을 거북이로
t.up()
t.goto(-250,-250)
t.down()
for x in range(4): # 500 x 500 모양을 만드는 반복함수
t.fd(500)
t.lt(90)
t.up()
t.goto(100,100)
t.down()
t.begin_fill()
t.color('green')
for x in range(4): # 속도 다르게 할  영역 설정
t.fd(100)
t.lt(90)
t.end_fill()
t.color('black')
t.up()
t.home() # 원래 위치로
t.down()
t.seth(a) # 출발 각도 설정
while True: # 
    ang=int(t.heading()) # 부딪혔을 때 각도
    t.fd(1) #거북이가 움직일 거리(속도처럼 씀)   
    if int(t.xcor()) >= 250: #오른쪽 벽에 부딪히면 튕김 
        t.seth(180-ang) 
    if t.xcor() <= -250: #왼쪽 벽에 부딪히면 튕김 
        t.seth(180-ang)
    if t.ycor() >= 250: #위쪽 벽에 부딪히면 튕김   
        t.seth(360-ang)    
    if t.ycor() <= -250: #아래쪽 벽에 부딪히면 튕김   
        t.seth(360-ang) 
    if 100<=t.xcor()<=200 and 100<=t.ycor()<=200: #초록색 사각형에 들어갈 시 속도 줄음
        t.fd(0.3)
