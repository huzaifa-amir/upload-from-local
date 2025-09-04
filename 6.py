import math

# Function to solve the quadratic equation
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if discriminant is positive, zero, or negative
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        # One real root
        root = -b / (2 * a)
        return (root,)
    else:
        # Complex roots (discriminant < 0)
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

# Taking input from the user for the coefficients
print("Enter the coefficients for the quadratic equation ax^2 + bx + c = 0")

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation
roots = solve_quadratic(a, b, c)

# Display the roots
if len(roots) == 2:
    print(f"The roots are: {roots[0]} and {roots[1]}")
else:
    print(f"The root is: {roots[0]}")



