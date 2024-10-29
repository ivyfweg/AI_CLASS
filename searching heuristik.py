
A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
x = int(input("Masukkan nilai x: "))
count_x = A.count(x)
indices_x = [index for index, value in enumerate(A) if value == x]
print(f"Nilai {x} muncul sebanyak {count_x} kali pada indeks: {indices_x}")
