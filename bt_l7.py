# BT1
def tong_chan(arr):
    tong = 0
    for x in arr:
        if x % 2 == 0:
            tong += x
    return tong

n = [1, 7, 4, 6, 9]
print(f"tổng số chẵn là: {tong_chan(n)}") 

# BT2
def tong_le(arr):
    tong = 0
    for x in arr:
        if x % 2 == 1:
            tong += x
    return tong

n = [1, 7, 4, 6, 9]
print(f"tổng số le là: {tong_le(n)}") 

# BT3
def timkiem(arr):
    return max(arr)
arr = [1,2,3,4,5,6,7,8,9]
ketqua = timkiem(arr)
print(f"số lớn nhất là: {ketqua}")

# BT4
def data(arr):
    chan=0
    for x in arr:
        if x % 2 == 0:
            chan += x
    return chan
arr = [1,2,3,4,5,6,7,8,9]
ketqua = data(arr)

if ketqua == 0:
    print("số nguyên dương n toàn lẻ")
else:
    print("có số chẵn")

# BT5
def so_lon_nhat(arr):
    return max(a,b,c)
a,b,c = 6,2,8
ketqua = so_lon_nhat(arr)
print(f"số lớn nhất là: {ketqua}")

# BT6
