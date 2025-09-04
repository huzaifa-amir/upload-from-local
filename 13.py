import tkinter as tk
import sympy as sp
def simplify_equation(equation):
    expr=sp.sympify(equation)
    return sp.simplify(expr)
def evaluate_expression(equation):
    expr=sp.sympify(equation)
    return expr.evalf()
def solve_equation(equation):
    expr=sp.sympify(equation)
    return sp.solve(expr)
def show_result():
    expr = inp.get()
    todo = myvar.get()
    if todo=='Simplify Equation':
        result=simplify_equation(expr)
        result_label.config(text=result)
    elif todo=='Evaluate':
        result=evaluate_expression(expr)
        result_label.config(text=f"{result:.2f}")
    elif todo=='Solve Equation':
        result=solve_equation(expr)
        l = ''
        if isinstance(result, list):
            for r in result:
                l += str(r) + '\n'
        else:
            l = result
        result_label.config(text=l)
win=tk.Tk()
win.title("Calculator")
win.geometry("500x600")
win.resizable(False,False)
myvar=tk.StringVar()
lbl=tk.Label(win, text="Calculator", 
               font=("Arial", 20, 'italic'), 
               bg="#0CDCC0",
               fg="#bfc81e")
lbl.pack(fill='x')
opt = tk.OptionMenu(win, myvar, 'Evaluate', 'Solve Equation', 'Simplify Equation')
opt.pack(padx=5, pady=5)

inp = tk.Entry(win, font=("Cambria Math", 20))
inp.pack(fill='x', padx=10, pady=10)

btn = tk.Button(win,text="Show Results", command=show_result)
btn.pack()

result_label = tk.Label(win, font=("Cambira Math", 30, 'underline'))
result_label.pack()
win.mainloop()