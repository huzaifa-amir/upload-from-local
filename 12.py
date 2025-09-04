import tkinter as tk
def on_Click():
    text=ent.get()
    label.config(text=text)
win=tk.Tk()
label=tk.Label(win,text='Label',bg="#43b1ec",fg="#71d711",font=("Impact", 20))
label.pack(padx=10,pady=10)
btn=tk.Button(win,text='Click me',command=on_Click)
btn.pack(padx=10,pady=10)
ent=tk.Entry(win,font=("Arial",20))
ent.pack(padx=10,pady=10)
tk.mainloop()




