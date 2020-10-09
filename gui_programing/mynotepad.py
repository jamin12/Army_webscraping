from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장") # 타이틀 설정
root.geometry("640x480") # 가로 x 세로

menu = Menu(root)

menu_File = Menu(menu,tearoff = 0)
menu_File.add_command(label = "Open")
menu_File.add_command(label = "Save")
menu_File.add_command(label = "Exit",command = root.quit)

menu.add_cascade(label="File",menu = menu_File)

txt = Text(root)
txt.pack(fill="both")

root.config(menu = menu)
root.mainloop()