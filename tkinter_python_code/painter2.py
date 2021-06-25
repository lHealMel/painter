import tkinter

# 전역 변수 선언
wid = 1
color = "black"
now_color = "검은색"
lastx1, lasty1 = 0, 0


def paintering2():
    # 기본 설정
    painting_window = tkinter.Tk()
    painting_window.geometry("800x600+100+100")
    painting_window.resizable(0, 0)
    painting_window.title("그림판")


    # 프레임 설정
    frame_canvas = tkinter.Frame(painting_window, width = 600, height = 400, relief = "solid", bd = 2)
    frame_canvas.pack(side = "top")
    frame_label = tkinter.Frame(painting_window, width = 400, height = 100, relief = "solid", bd = 2)
    frame_label.pack()
    frame_button = tkinter.Frame(painting_window, width = 500, height = 500, relief = "solid", bd = 2)
    frame_button.pack(side = "bottom")
    frame_button.place(x = 720)

    # 캔버스 설정
    canvas = tkinter.Canvas(frame_canvas, width = 600, height = 400, cursor = "pencil")

   # 메뉴 설정
    menu_bar = tkinter.Menu(painting_window)
    menu1 = tkinter.Menu(menu_bar, tearoff = 0)



    # 페인트 변수 선언(사실은 원 그리기)
    def paint_line(event):
        global lastx1, lasty1
        lastx1, lasty1 = event.x, event.y
        canvas.create_line(event.x, event.y, event.x + 0.5, event.y + 0.5, fill = color, width = wid)

    def lining(event):
        global lastx1, lasty1
        canvas.create_line(lastx1, lasty1, event.x, event.y, fill = color, width = wid)
        lastx1, lasty1 = event.x, event.y

    # 마우스 휠로 크기(원의) 조정
    def scroll(event):
        global wid
        if color == "SystemButtonFace":
            if wid < 5:
                if event.delta == 120:
                    wid += 1
                    label_wid.config(text = "지우개의 굵기:" + str(wid))
            if wid > 1:
                if event.delta == -120:
                    wid -= 1
                    label_wid.config(text = "지우개의 굵기:" + str(wid))
        else:
            if wid < 5:
                if event.delta == 120:
                    wid += 1
                    label_wid.config(text = "굵기:" + str(wid))
            if wid > 1:
                if event.delta == -120:
                    wid -= 1
                    label_wid.config(text = "굵기:" + str(wid))

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

    # 지우개 커맨드
    def eraser():
        global color
        color = "SystemButtonFace"
        canvas.config(cursor = "dotbox")
        label_wid.config(text = "지우개의 굵기:" + str(wid))

    # 메뉴로 돌아가는 함수
    def return_menu():
        from painter_menu import painter_menuing
        painting_window.destroy()
        painter_menuing()

    def all_clear():
        canvas.delete("all")

    # 라벨 생성
    label_wid = tkinter.Label(frame_label, text = "굵기:" + str(wid))
    label_wid.pack()
    label_color = tkinter.Label(frame_label, text = "붓의 색:" + str(now_color))
    label_color.place(y = 100)
    label_color.pack(anchor = "center")

    # 버튼 생성
    button1 = tkinter.Button(frame_button, command = red_color, cursor = "pencil", background = "red").pack(fill="x")
    button2 = tkinter.Button(frame_button,  command = yellow_color, cursor = "pencil", bg = "yellow").pack(fill="x")
    button3 = tkinter.Button(frame_button, command = green_color, cursor = "pencil", bg = "green").pack(fill="x")
    button4 = tkinter.Button(frame_button,  command = black_color, cursor = "pencil", bg = "black").pack(fill="x")
    button5 = tkinter.Button(frame_button, text = "지우개", command = eraser, cursor = "dotbox").pack(fill="x")
    button7 = tkinter.Button(painting_window, text = "모두 지우기", command = all_clear).place(x = 1, y = 35)

    #메뉴 설정
    menu_bar.add_cascade(label = "메뉴", menu=menu1)
    menu1.add_command(label = "메뉴로 가기", command = return_menu)

    # 캔버스 설정 2
    canvas.bind("<B1-Motion>", lining)
    canvas.bind("<Button-1>", paint_line)
    canvas.bind("<MouseWheel>", scroll)
    canvas.pack()

    painting_window.config(menu = menu_bar)
    painting_window.mainloop()
