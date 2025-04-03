def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Nhập số nguyên không âm
n = int(input("Nhập số nguyên: "))
if n < 0:
    print("Vui lòng nhập một số nguyên không âm.")
else:
    print(f"{n}! = {factorial(n)}")
