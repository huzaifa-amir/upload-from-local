import sympy as sp
from colorama import init,Fore,Back,Style
init(autoreset=True)
print(Back.GREEN+Fore.LIGHTYELLOW_EX+"   Interactive Calculator   ")
def simplify_equation(equation):
    simplified=sp.simplify(equation)
    print("Simplified:"+str(simplified))
while True:
    user_input=input(Fore.RED + "Enter equation to simplify: "+Style.RESET_ALL)
    if not user_input.strip():
        continue
    simplify_equation(user_input)
