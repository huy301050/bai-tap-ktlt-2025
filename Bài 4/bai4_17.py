n = int(input('Nhập số  n: '))
def tong_uw(x):
    tong = 0
    for i in range(1, x):
        if x % i == 0:  
            tong += i
    return tong
for x in range(1, n):
    if tong_uw(x) > x:
        print(x)
print("Hoàng Nghĩa Huy")
print("MSSV:235752020710001")