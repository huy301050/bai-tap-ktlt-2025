print("Sinh Viên : Hoang Nghia Huy")
print("MSSV : 235752020710001")
j = []
for i in range(500, 1200):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))
