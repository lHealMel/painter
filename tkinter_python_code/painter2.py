from tkinter import *
import main as mn
import webbrowser


def callback(url):
    webbrowser.open_new(url)


def search():
    print(input_text.get())
    mn.main_start(input_text.get())
    name = ["frame1", "frame2", "frame3", "frame4", "frame5", "frame6", "frame7", "frame8", "frame9"]
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(0, 9):
        name[i] = Frame(window, width=300, height=300, relief="solid", bd=1)
        name[i].pack(pady=10)

    for i in range(0, 9):
        Label(name[i], text=mn.title_list[i]).pack(anchor = "center")
        x[i] = Label(name[i], text="링크:" + "https://www.10000recipe.com" + mn.link_list[i], cursor="hand2", fg="blue")
        x[i].pack(anchor="center")
        x[i].bind("<Button-1>", lambda e: callback("https://www.10000recipe.com" + mn.link_list[i]))
        Label(name[i], text="조회수" + mn.buyer_list[i]).pack(anchor="center")


def del_1():
    filename = "file1.txt"
    infile = open(filename, encoding='utf-8')
    x = infile.readlines()
    infile.close()
    outfile = open(filename, "w", encoding='utf-8')
    for line in x:
        y = line
        line = line.replace(y, "")
        print(line, file=outfile, end="")
    print("변경된 파일이 저장되었습니다")
    outfile.close()


def del_2():
    filename = "file2.txt"
    infile = open(filename, encoding='utf-8')
    x = infile.readlines()
    infile.close()
    outfile = open(filename, "w", encoding='utf-8')
    for line in x:
        y = line
        line = line.replace(y, "")
        print(line, file=outfile, end="")
    print("변경된 파일이 저장되었습니다")
    outfile.close()




window = Tk()
window.title("Applay")
window.geometry("1400x900+100+100")


search_frame = Frame(window, width=800, height=150)
search_frame.pack()



delete1 = Button(search_frame, bg="black", fg="white", text="삭제1", relief="solid", width=5, height=1, repeatdelay=100,
                 repeatinterval=100, command=del_1)
delete1.pack(anchor='ne')
delete2 = Button(search_frame, bg="black", fg="white", text="삭제2", relief="solid", width=5, height=1, repeatdelay=100,
                 repeatinterval=100, command=del_2)
delete2.pack(anchor='ne')

input_text = Entry(search_frame, width=100)
input_text.pack()

search = Button(search_frame, bg="black", fg="white", text="검색", relief="solid", width=5, height=1, repeatdelay=100,
                repeatinterval=100, command=search)
search.pack()

window.mainloop()
