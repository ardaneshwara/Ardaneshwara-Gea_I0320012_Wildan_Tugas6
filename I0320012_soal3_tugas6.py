print("PROGRAM UNTUK MENAMPILKAN BILANGAN PRIMA")
print()
lower = 10
upper = 24

for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num, "bukan prima")
                break
        else:
            print(num, "adalah bilangan prima")