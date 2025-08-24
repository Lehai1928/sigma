import time
with open("data.txt", "w", encoding="UTF-8") as f:
    for i in range(0, 100001, 1):
        f.write(str(i) + "\n")



def timkiem_tuanTu(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

def binary(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = []
with open("data.txt", "r", encoding="UTF-8") as f:
    for line in f:
        arr.append(int(line.strip()))

k = 99999

startTime = time.time()
ketqua1 = timkiem_tuanTu(arr, k)
endTime = time.time()
print("Tìm kiếm tuần tự:", endTime - startTime, "giây, Kết quả =", ketqua1)

startTime2 = time.time()
ketqua2 = binary(arr, k)
endTime2 = time.time()
print("Tìm kiếm nhị phân:", endTime2 - startTime2, "giây, Kết quả =", ketqua2)
