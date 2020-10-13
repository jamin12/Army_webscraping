from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Nado Photo")
root.resizable(False,False)

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack()

#버튼 정의
btn_add_file = Button(file_frame, text = "파일 추가",padx = 5, pady = 5, width = 12)
btn_del_file = Button(file_frame, text = "선택 삭제",padx = 5, pady = 5, width = 12)

#버튼 프레임에 부착
btn_add_file.pack(side = "left")
btn_del_file.pack(side = "right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill = "both")

#스크롤 바
file_list_scrollbar = Scrollbar(list_frame)
file_list_scrollbar.pack(fill = "y", side = "right")

#리스트 박스
list_file = Listbox(list_frame,selectmod = "extended", height = 15,yscrollcommand = file_list_scrollbar)
list_file.pack(side = "left", fill = "both", expand = True)

file_list_scrollbar.config(command = list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root,text = "저장경로")
path_frame.pack()

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side = "left", fill = "x", expand = True,ipady = 4)

btn_dest_path = Button(path_frame,text = "찾아보기",width=10)
btn_dest_path.pack(side = "right")

root.mainloop()