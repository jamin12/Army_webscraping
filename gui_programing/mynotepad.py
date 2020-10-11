from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("제목 없음 - Windows 메모장") # 타이틀 설정
root.geometry("640x480") # 가로 x 세로

menu = Menu(root)

#스크롤 바 설정
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right",fill = "y")

#텍스트 에리아 설정 yscrollcommand : 스크롤 사용 가능하게 하는 명령어
txt = Text(root,height = 1080,width = 1920, yscrollcommand=scrollbar.set)
txt.pack(side = "left")

#스크롤바와 txt가 서로 상호 작용 할수 있도록 해줌
scrollbar.config(command = txt.yview)
# 저장 기능
def save():
    with open("mynote.txt","wt") as f:
        f.write(txt.get(1.0,END))

# 파일 열기 
def fileopen():
    txt.delete("1.0",END)
    try:
        with open("mynote.txt","rt") as f:
            while True:
                line = f.readline()
                if not line: break
                txt.insert(END,line)
    except FileNotFoundError:
        msgbox.showerror("경고","파일이 없습니다.")

# 메뉴 바 설정 
#메뉴 파일(저장 열기 닫기)
menu_File = Menu(menu,tearoff = 0)
menu_File.add_command(label = "Open",command = fileopen)
menu_File.add_command(label = "Save",command = save)
menu_File.add_separator()
menu_File.add_command(label = "Exit",command = root.quit)

menu_edit = Menu(menu,tearoff = 0)

menu.add_cascade(label="File",menu = menu_File)
menu.add_cascade(label = "menu_edit",menu = menu_edit)

root.config(menu = menu)
root.mainloop()