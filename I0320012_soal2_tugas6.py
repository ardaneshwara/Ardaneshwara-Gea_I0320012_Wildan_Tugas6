print("PROGRAM MENGHITUNG NILAI RATA-RATA")

# masukkan banyak data yang akan dihitung

n = int(input("\nBanyaknya Data: "))
print()
data = []
jum = 0

for i in range(0, n):
    temp = int(input("Masukkan data ke-%d: " % (i + 1)))
    data.append(temp)
    jum += data[i]
    rata2 = jum / n

print("\nRata-rata dari keseluruhan data adalah %0.2f" % rata2)
