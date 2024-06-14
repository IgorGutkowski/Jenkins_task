import sys

def multiply(x, y):
    return x * y

if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(multiply(num1, num2))
