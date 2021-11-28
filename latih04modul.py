A=[1,2,3,"bulan","matahari","rembulan"]
print(A)
print()
#tampilkan elemen ke 3
print("elemen ketiga=> ",A[3])
print(A)
print("elemen ke 2 s/d 4 => ",A[2:4])
print(A)
print("elemen terakhir=> ",A[-1])
print(A)
print("=====perubahan elemen====")
print("mengubah dingin jadi hangat")
A[4]="hangat"
print(A)
#ubah elemen ke 4 sampai dengan elemen terakhir
A[4],A[5]="dingin","hangat"
print("perubahan elemen 4-akhir=> ",A)
print(A)
print()
A.extend([3,4,5])
B=["dragon frut","nanas","kecapi"]
B.append([1000,2000,3000])
element=A+B
print("gabungan elemen A dan B")
print(element)