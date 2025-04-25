print("Sinh Vien: Hoang Nghia Huy")
print("MSSV:235752020710001")
str=input("Nhập một chuỗi:")
dict = { }
for n in str:
    keys = dict.keys()
    if n in keys:
        dict [n] += 1
    else:
        dict [n] = 1
print (dict)
