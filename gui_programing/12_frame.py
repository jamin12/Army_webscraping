from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root,text = "메뉴를 선택해 주세요").pack(side="top")

Button(root,text="주문하기").pack(side="bottom")

frame_buger = Frame(root, relief = "solid", bd = 1)
frame_buger.pack(side = "left",fill="both", expand = True)

Button(frame_buger, text="햄버거").pack()    
Button(frame_buger, text="치즈버거").pack()    
Button(frame_buger, text="치킨버거").pack()    

frame_drink = LabelFrame(root,text="음료")
#pack에 여러 설정으로 화면을 어떻게 채울지 결정
frame_drink.pack(side = "right", fill="both", expand = True)

Button(frame_drink, text="콜라").pack()    
Button(frame_drink, text="사이다").pack()    
root.mainloop()