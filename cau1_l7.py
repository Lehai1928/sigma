def so_chan_hoan_hao(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            tong += i
    return tong == n

for num in range(1, 101):
    if so_chan_hoan_hao(num):
        print(num, "là số đặc biệt")
