from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀 설정

label1 = Label(root,text="안녕하세요")
label1.pack()


photo = PhotoImage(file="gui_programing/image/img1.png")
label2 = Label(root,image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

btn = Button(root,text="클릭",command=change)
btn.pack()
root.mainloop()