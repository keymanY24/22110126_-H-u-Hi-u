def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = list(map(int, input("Nhập mảng các số nguyên, cách nhau bởi dấu cách: ").split()))
    bubble_sort(arr)
    print("Mảng sau khi sắp xếp:", arr)

if __name__ == "__main__":
    main()
