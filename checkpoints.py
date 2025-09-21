def tim_cap_so(arr, tong_muc_tieu):
    ket_qua = []
    da_thay = set()
    
    for so in arr:
        can_tim = tong_muc_tieu - so
        if can_tim in da_thay:
            ket_qua.append((can_tim, so))
        da_thay.add(so)
    
    return ket_qua


num = [1,2,3,4,5,6,7,8,9]
tong = 10
print(tim_cap_so(num, tong))