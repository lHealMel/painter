# tkinter, tkinter 의 message box, painter의 paintering import
import tkinter
from painter import paintering
from painter2 import paintering2
from tkinter import messagebox


# 기본 설정
menu_window = tkinter.Tk()
menu_window.geometry("300x300+100+100")
menu_window.resizable(0, 0)
menu_window.title("메뉴")


# button1 의 실행 문장, 그림판 실행
def start_painter():
    menu_window.destroy()
    paintering()

# button2 의 실행 문장, 그림판2 실행
def start_painter2():
    menu_window.destroy()
    paintering2()


# button3 의 실행 문장
def show_me():
    tkinter.messagebox.showinfo("제작자", "제작자: HealMe- or lHealMel")


# button4 의 실행 문장
def closing():
    question_box = tkinter.messagebox.askquestion(title = "?", message = "정말로 종료하시겠습니까?")
    if question_box == 'yes':
        menu_window.destroy()
    else:
        pass


# 버튼의 X좌표값, hei: 높이, wid: 두께
a = 115
hei = 1
wid = 10

# 버튼 설정
button1 = tkinter.Button(menu_window, text = "그림판 초기버전 실행", command = start_painter, height = hei,
                         anchor = "s").place(x = 95, y = 50)
button2 = tkinter.Button(menu_window, text = "그림판 2nd 버전 실행", command = start_painter2, height = hei,
                         anchor = "s").place(x = 95, y = 100)
button3 = tkinter.Button(menu_window, text = "제작자", command = show_me, height = hei, width = wid, anchor = "s").place(
    x = a, y = 200)
button4 = tkinter.Button(menu_window, text = "종료", command = closing, height = hei, width = wid, anchor = "s").place(
    x = a, y = 250)

# 끝
menu_window.mainloop()
