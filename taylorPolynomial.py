def exp_Taylor(n, x):
    fat = 1.0
    term = 1.0
    sum = term
    i = 1
    while i<=n:
        fat = fat * i
        term = term * x
        sum = sum + ter/fat
        i = i+1
    return sum

if __name__ == "__main__":
    n = int(raw_input("Digite n: "))
    x = float(raw_input("Digite x: "))