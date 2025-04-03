def fibonacci_dp(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    fib = [0] * (n + 1)
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

def main():
    n = int(input("Nhập số nguyên n: "))
    if n < 0:
        print("Vui lòng nhập số nguyên không âm.")
    else:
        print(f"Số Fibonacci thứ {n} là: {fibonacci_dp(n)}")

if __name__ == "__main__":
    main()
