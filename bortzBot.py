import tkinter as tk
import pyautogui
import time
# relx=,rely=,relwidth=,relheight=


def mtn():
    x = pyautogui.locateCenterOnScreen('mbox.png', confidence=0.6)
    pyautogui.click(x)
    for i in range(int(amount.get())):
        time.sleep(0.1)
        pyautogui.write(ttx.get())
        pyautogui.press('enter')
        
def dtn():
    x = pyautogui.locateCenterOnScreen('dbox.png', confidence=0.7)
    pyautogui.click(x)
    for i in range(int(amount.get())):
        time.sleep(0.1)
        pyautogui.write(ttx.get())
        pyautogui.press('enter')
def ttn():
    x = pyautogui.locateCenterOnScreen('tbox.png', confidence=0.7)
    pyautogui.click(x)
    for i in range(int(amount.get())):
        time.sleep(0.1)
        pyautogui.write(ttx.get())
        pyautogui.press('enter')



root = tk.Tk()

canvas = tk.Canvas(root , width=600, height=260)
canvas.pack()
root.title('SpamBott')
frame = tk.Frame(root, bg='gray')
frame.place(relx=0.157, rely =0.1,relwidth=0.7, relheight=0.8)
labe1 = tk.Label(frame, text='Add Amount :', bg='gray',font=('Courier', 10))
labe1.place(relx=0.1,rely=0.7,relwidth=0.23,relheight=0.23)
labe2 = tk.Label(frame, text='Add Text You Wanna Spam :', bg='gray')
labe2.place(relx=0.001,rely=0.01,relwidth=0.4,relheight=0.4)
btn = tk.Button(frame, text='messenger',command=lambda:mtn())
btn.place(relx=0.1,rely=0.37,relwidth=0.23,relheight=0.23)
btn2 = tk.Button(frame, text='discord',command=lambda:dtn())
btn2.place(relx=0.39,rely=0.37,relwidth=0.23,relheight=0.23)
btn3 = tk.Button(frame, text='telegram',command=lambda:ttn())
btn3.place(relx=0.67,rely=0.37,relwidth=0.23,relheight=0.23)


amount = tk.Entry(frame, bg='white')
amount.place(relx=0.39,rely=0.7,relwidth=0.23,relheight=0.23)

ttx = tk.Entry(frame)
ttx.place(relx=0.38,rely=0.1,relwidth=0.23,relheight=0.23)

tk.mainloop()
