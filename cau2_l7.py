def bubble_sort(A):
    n = len(A)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
        if not swapped:
            break
    return A

def binary(A, k):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == k:
            return mid
        elif A[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1

A = [3, 29, 10, 41, 5, 6, 74, 48, 45, 36, 4, 7, 54, 45, 69, 21, 28, 85, 4, 23, 46, 365, 64, 59, 78]
ketqua = bubble_sort(A)

queries = list(map(int, input("Nhập dãy truy vấn (cách nhau bởi dấu cách): ").split()))

for Q in queries:
    pos = binary(ketqua, Q)
    if pos != -1:
        print(f"Đã tìm thấy {Q} ở vị trí thứ {pos}.")
    else:
        print(f"{Q} không xuất hiện trong dãy A.")
