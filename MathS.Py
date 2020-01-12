import time
import cmd as c

def start():
    print("\nChoose a task!")
    print("[1] Slope to standard")
    print("[2] Solve equations with elimination")
    l = ['1', '2']
    cmd = c.g(l)
    if cmd == '1':
        SS()
    elif cmd == '2':
        ES()

def SS():
    print("Y = A/Bx + b --> Ax + By = C")
    time.sleep(1)
    print("enter y value")
    y = float(input())
    print("enter M as fraction A/B - A")
    A = float(input())
    print("enter M as fraction A/B - B")
    B = float(input())
    print("enter b")
    b = float(input())
    ystr = str(y)
    Astr = str(A)
    Bstr = str(B)
    bstr = str(b)
    print("equation: "+ystr+"y = "+Astr+"/"+Bstr+"x + "+bstr)
    time.sleep(1)
    print("\n-----------------\n")
    time.sleep(1)
    print("equation: -"+Astr+"/"+Bstr+"x + "+ystr+"y = "+bstr)
    time.sleep(1)
    print("\n-----------------\n")
    time.sleep(1)
    ystr1 = str(y*B)
    bstr1 = str(b*B)
    print("final equation: -"+Astr+"x + "+ystr1+"y = "+bstr1)
    time.sleep(2)
    print("\n-----------------\n")
    time.sleep(2)
    start()

def ES():
    print("Ax + By = C")
    print("Ax + By = C")
    A1 = float(input("\nEnter A for first equation "))
    B1 = float(input("\nEnter B for first equation "))
    C1 = float(input("\nEnter C for first equation "))
    A2 = float(input("\nEnter A for second equation "))
    B2 = float(input("\nEnter B for second equation "))
    C2 = float(input("\nEnter C for second equation "))
    A1s = str(A1)
    B1s = str(B1)
    C1s = str(C1)
    A2s = str(A2)
    B2s = str(B2)
    C2s = str(C2)
    print("\nsystem: "+A1s+"x + "+B1s+"y = "+C1s)
    print("system: "+A2s+"x + "+B2s+"y = "+C2s)
    if A1 == -A2:
        B3 = B1 + B2
        C3 = C1 + C2
        B3s = str(B3)
        C3s = str(C3)
        print("\nEquation: "+B3s+"y = "+C3s)
        B1B = C3/B3
        B1Bs = str(B1B)
        print("\nEquation: y = "+B1Bs)
        start()

    elif B1 == -B2:
        A3 = A1 + A2
        C3 = C1 + C2
        A3s = str(A3)
        C3s = str(C3)
        print("\nEquation: "+A3s+"x = "+C3s)
        AC1 = C3/A3
        AC1s = str(AC1)
        print("\nEquation: x = "+AC1s)
        A1A = A1*AC1
        A1As = str(A1A)
        print("\nEquation: "+A1As+" + "+B1s+"y = "+C1s)
        C1C = C1 - A1A
        C1Cs = str(C1C)
        print("\nEquation: "+B1s+"y = "+C1Cs)
        BC1 = C1C/B1
        BC1s = str(BC1)
        print("\nEquation: y = "+BC1s)
        print("\nOrdered pair: ("+AC1s+", "+BC1s+")")
        start()




if __name__ == "__main__":
    start()
