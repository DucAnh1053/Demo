import math

from sympy import solve
def solveEquation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return ("Infinite Solutions")
            else:
                return ()
        else:
            x = -c/b
            return (x, )
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return ()
        elif delta == 0:
            x = -b/(2*a)
            return (x, )
        else:
            x1 = (-b - math.sqrt(delta))/(2*a)
            x2 = (-b + math.sqrt(delta))/(2*a)
            return (x1, x2)

def main():
    print(solveEquation(1, 1, -2)) #(-2.0, 1.0)
    print(solveEquation(1, 2, 1)) #(-1.0,)
    print(solveEquation(1, 0, 1)) #()
    print(solveEquation(0, 0, 0)) #Infinite Solutions
    print(solveEquation(0, 0, 2)) #()
    print(solveEquation(0, 1, 2)) #(-2.0,)
    
if __name__ == "__main__":
    main()