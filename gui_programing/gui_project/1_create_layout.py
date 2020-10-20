from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

root = Tk()
root.title("Nado Photo")
root.resizable(False,False)

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill = "x",padx = 5, pady = 5) #간격 띄우기

#버튼 정의
btn_add_file = Button(file_frame, text = "파일 추가",padx = 5, pady = 5, width = 12)
btn_del_file = Button(file_frame, text = "선택 삭제",padx = 5, pady = 5, width = 12)

#버튼 프레임에 부착
btn_add_file.pack(side = "left")
btn_del_file.pack(side = "right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill = "both",padx = 5, pady = 5,ipady = 5)

#스크롤 바
file_list_scrollbar = Scrollbar(list_frame)
file_list_scrollbar.pack(fill = "y", side = "right")

#리스트 박스
list_file = Listbox(list_frame,selectmod = "extended", height = 15,yscrollcommand = file_list_scrollbar)
list_file.pack(side = "left", fill = "both", expand = True)

file_list_scrollbar.config(command = list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root,text = "저장경로")
path_frame.pack(fill = "x",padx = 5, pady = 5,ipady = 5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side = "left", fill = "x", expand = True,padx = 5, pady = 5,ipady = 4)

btn_dest_path = Button(path_frame,text = "찾아보기",width=10)
btn_dest_path.pack(side = "right",padx = 5, pady = 5)

#옵션 프레임
option_frame = LabelFrame(root, text = "옵션")
option_frame.pack(padx = 5, pady = 5,ipady = 5)

#가로 넓이 옵션
#가로 넓이 레이블
lbl_width = Label(option_frame,text ="가로넓이",width = 8)
lbl_width.pack(side = "left",padx = 5, pady = 5)

# 가로 넓이 콤보
opt_width = ["원본유지","1024","800","640"]
cmb_width = ttk.Combobox(option_frame, state = "readonly", values = opt_width,width = 10)
cmb_width.current(0)
cmb_width.pack(side = "left",padx = 5, pady = 5)

# 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(option_frame,text ="간격",width = 8)
lbl_space.pack(side = "left",padx = 5, pady = 5)


#간격 옵션 콤보
opt_space = ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(option_frame, state = "readonly", values = opt_space,width = 10)
cmb_space.current(0)
cmb_space.pack(side = "left",padx = 5, pady = 5)

# 파일 포맷 옵션
# 파일 옵션 레이블
lbl_format = Label(option_frame,text ="포맷",width = 8)
lbl_format.pack(side = "left",padx = 5, pady = 5)


# 파일 옵션 콤보
opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(option_frame, state = "readonly", values = opt_format,width = 10)
cmb_format.current(0)
cmb_format.pack(side = "left",padx = 5, pady = 5)

# 진행 상황 progresss bar
progress_frame = LabelFrame(root, text = "진행상황")
progress_frame.pack(fill = "x",padx = 5, pady = 5,ipady = 5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame,maximum = 100, variable = p_var)
progress_bar.pack(fill = "x",padx = 5, pady = 5)

# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill = "x",padx = 5, pady = 5)

btn_close = Button(run_frame, padx = 5,pady = 5,text = "닫기",width = 12,command = root.quit)
btn_close.pack(side = "right",padx = 5, pady = 5)

btn_start = Button(run_frame, padx = 5,pady = 5,text = "시작",width = 12)
btn_start.pack(side = "right",padx = 5, pady = 5)


root.mainloop()

