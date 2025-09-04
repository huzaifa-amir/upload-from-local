# Sympy
from colorama import init, Fore, Back, Style
import sympy as sp

init(autoreset=True)

print(Back.BLUE + Fore.LIGHTBLACK_EX + "   Interactive Calculator   ")

def simplify_equation(equation):
    print(f"{Style.RESET_ALL}SIMPLFIED: {Fore.GREEN}{sp.simplify(equation)}{Style.RESET_ALL}")

def solve_equation(equation):
    print(f"{Style.RESET_ALL}SOLVED: {Fore.GREEN}{sp.solve(equation)}{Style.RESET_ALL}")

def evaluate(expression):
    print(f"{Style.RESET_ALL}EVALUATED: {Fore.GREEN}{eval(expression, {}, {})}{Style.RESET_ALL}")

while True:
    inp = input(Fore.LIGHTGREEN_EX + '>> ')
    spl = inp.split(':', 1)
    try:
        if spl[0].__len__() == 0:
            continue
        elif spl[0].upper() == 'SY':
            simplify_equation(spl[1])
        elif spl[0].upper() == 'SO':
            solve_equation(spl[1])
        else:
            evaluate(spl[0])
    except:
        print(Fore.LIGHTCYAN_EX+"error")      


'''
>> SY: 2*x + y

'''