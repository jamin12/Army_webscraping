from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀 설정

btn1 = Button(root, text = "버튼1")
btn1.pack()

btn2 = Button(root, padx = 5, pady = 10 , text="버튼 2")
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5 , text="버튼 3") # padx pady 여백의 크기 (유동적)
btn3.pack()

btn4 = Button(root, width = 10, height = 3, text="버튼 4") # width height 너비 높이(고정된 크기)
btn4.pack()

#버튼에 색 넣기
btn5 = Button(root,fg = "red",bg="yellow",text="버튼5")
btn5.pack()

# 버튼에 이미지 넣기
photo = PhotoImage(file="gui_programing/image/img1.png")
btn6 = Button(root,image=photo)
btn6.pack()

#버튼 액션 활성화
def btncmd():
    print("버튼이 클릭 되었어요")

#command : 버튼이 눌려졋을때 발생하는 이벤트
btn7 = Button(root, text="동작하는 버튼",command=btncmd)
btn7.pack()

root.mainloop()