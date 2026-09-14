# Advanced math

def power(a,b):
    return a**b

def root(a):
    return a**0.5

def fact(x):
    if x <= 1:
        return 1
    else:
        return x* fact(x-1)


if __name__ == "__main__":
    print("----Test Cases----")
    print(power(2,3))
    print(root(16))
    print(fact(5))