def main():
    x = input("What's x? ")
    print(f"x squared is {square(x)}")

def square(n):
    return n * n

def division(a, b):
    if b == 0:
        return "Divisor can't be zero"
    return a/b

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
