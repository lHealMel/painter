import tkinter

# 기본 설정
painting_window = tkinter.Tk()
painting_window.geometry("800x600+100+100")
painting_window.resizable(0, 0)
painting_window.title("Painting Program")

# 프레임 설정
frame_canvas = tkinter.Frame(painting_window, width = 600, height = 400, relief = "solid", bd = 2)
frame_canvas.pack(side = "top")
frame_label = tkinter.Frame(painting_window, width = 400, height = 100, relief = "solid", bd = 2)
frame_label.pack()
frame_button = tkinter.Frame(painting_window, width = 600, height = 100, relief = "solid", bd = 2)
frame_button.pack(side = "bottom")

# 캔버스 설정
canvas = tkinter.Canvas(frame_canvas, width = 600, height = 400, cursor = "pencil")

# 전역 변수 선언
wid = 1
# 딕셔너리 생성 color = {"black" : "검은색", "red" : "빨간색", "yellow": "노란색", "green": "초록색"}
color = "black"
now_color = "검은색"


# 페인트 변수 선언(사실은 원 그리기)
def paint(event):
    x1, y1 = (event.x - 0), (event.y + 0)
    x2, y2 = (event.x + 0), (event.y - 0)
    canvas.create_oval(x1, y1, x2, y2, fill = color, width = wid, outline = color)


def eraser(event):
    x2, y2 = (event.x - 1), (event.y + 1)
    x3, y3 = (event.x + 1), (event.y - 1)
    canvas.create_rectangle(x2, y2, x3, y3, fill = "SystemButtonFace")
    canvas.config(cursor = "dotbox")
    label_wid.config(text = "지우개의 굵기:" + str(wid))


# 마우스 휠로 크기(원의) 조정
def scroll(event):
    global wid
    if wid < 100:
        if event.delta == 120:
            wid += 1
            label_wid.config(text = "굵기:" + str(wid))
    if wid > 1:
        if event.delta == -120:
            wid -= 1
            label_wid.config(text = "굵기:" + str(wid))
    # if color == "SystemButtonFace":
    #     if wid < 100:
    #         if event.delta == 120:
    #             wid += 1
    #             label_wid.config(text = "지우개의 굵기:" + str(wid))
    #     if wid > 1:
    #         if event.delta == -120:
    #             wid -= 1
    #             label_wid.config(text = "지우개의 굵기:" + str(wid))


# 색 지정 커맨드
def red_color():
    global color, now_color
    color = "red"
    now_color = "빨간색"
    canvas.config(cursor = "pencil")
    label_color.config(text = "붓의 색:" + str(now_color), fg = color, bg = "SystemButtonFace")


def yellow_color():
    global color, now_color
    color = "yellow"
    now_color = "노란색"
    canvas.config(cursor = "pencil")
    label_color.config(text = "붓의 색:" + str(now_color), fg = color, bg = "black")


def green_color():
    global color, now_color
    color = "green"
    now_color = "초록색"
    canvas.config(cursor = "pencil")
    label_color.config(text = "붓의 색:" + str(now_color), fg = color, bg = "SystemButtonFace")


def black_color():
    global color, now_color
    color = "black"
    now_color = "검정색"
    canvas.config(cursor = "pencil")
    label_color.config(text = "붓의 색:" + str(now_color), fg = color, bg = "SystemButtonFace")


# 라벨 생성
label_wid = tkinter.Label(frame_label, text = "굵기:" + str(wid))
label_wid.pack()
label_color = tkinter.Label(frame_label, text = "붓의 색:" + str(now_color))
label_color.place(y = 100)
label_color.pack(anchor = "center")

# 버튼 생성
button1 = tkinter.Button(frame_button, text = "빨간색", command = red_color, cursor = "pencil").pack()
button2 = tkinter.Button(frame_button, text = "노란색", command = yellow_color, cursor = "pencil").pack()
button3 = tkinter.Button(frame_button, text = "초록색", command = green_color, cursor = "pencil").pack()
button4 = tkinter.Button(frame_button, text = "검정색", command = black_color, cursor = "pencil").pack()
button5 = tkinter.Button(frame_button, text = "지우개", command = eraser, cursor = "dotbox").pack()

# 캔버스 설정 2
canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-1>", paint)
canvas.bind("<MouseWheel>", scroll)
canvas.pack()

painting_window.mainloop()