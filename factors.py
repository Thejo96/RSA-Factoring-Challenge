import sys
import math

def factorize(number):
    factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

def main(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                number = int(line.strip())
                factors = factorize(number)
                if len(factors) >= 2:
                    p, q = factors[0], factors[1]
                    outfile.write(f"{number}={p}*{q}\n")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python factors.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)

