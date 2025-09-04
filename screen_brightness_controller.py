import screen_brightness_control as sbc
import tkinter as tk

win = tk.Tk()
lbl=tk.Label(win,text="brightness",borderwidth=1,font=("blue",20),pady=20,bg="gray",fg="white",highlightbackground="black",highlightthickness=3,)
lbl.pack(fill="x")
win.geometry("500x500")
win.resizable(False,False)


win.title("Screen Brightness Controller")

def change_brightness(e):
    sbc.set_brightness(e)

slider = tk.Scale(win, orient='horizontal',length=150, command=lambda e: change_brightness(e),sliderlength=20,borderwidth=5,highlightbackground="black",highlightthickness=5,activebackground="gray",background="#C99A9C",border=7,fg='blue',font=("Impact",25),)
slider.set(sbc.get_brightness())
slider.pack(padx=5,pady=50)

win.mainloop()

