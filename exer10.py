import pandas as bear

data = bear.DataFrame([
    [10, 20, 5],
    [30, 10, 7],
    [35, 20, 10],
    [8, 7, 9],
    [14, 28, 10],
    [10, 20, 5],
    [5, 7, 8]],
    columns=["HP", "Laptop", "Komputer"],
    index=["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])

print(data,"\n")
print("Total penjualan untuk setiap produk")
print(data.sum(axis=0),"\n")
print("Total penjualan setiap hari")
print(data.sum(axis=1),"\n")
print("Produk dengan penjualan terbanyak selama seminggu")
print(data.sum(axis=0).idxmax(),data.sum(axis=0).max(),"\n")
print("Hari dengan penjualan tertinggi untuk setiap produk")
print(data.idxmax(axis=0))