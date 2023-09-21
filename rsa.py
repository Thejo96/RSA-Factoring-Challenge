import sys
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    x, y, d = 2, 2, 1
    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    if d == n:
        return None  # Failed to factorize
    else:
        return d, n // d

def main(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            n = int(line.strip())
            factors = pollards_rho(n)
            if factors:
                p, q = factors
                print(f"{n}={p}*{q}")
            else:
                print(f"Failed to factorize {n}")

    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    main(filename)

