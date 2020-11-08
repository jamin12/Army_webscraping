from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480")

# mode : indeterminate (언제 끝날지 모름 바의 게이지기 차지 않고 계속 왔다갔다함)
# progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")
# mode : determinate 바가 차오름
# progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate")
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지


# btn = Button(root,text="중지",command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 160, variable = p_var2)
progressbar2.pack()

def btncmd():
    for i in range(101):
        time.sleep(0.01)
        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # for 문이 한번 돌때마다 프로그레스바가 업데이트 됨
        # print(p_var2.get())
btn = Button(root,text="중지",command=btncmd)
btn.pack()


root.mainloop()