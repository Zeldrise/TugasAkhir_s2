def input_data(books):
    print("=" * 35)
    print("      INPUT DATA 10 BUKU")
    print("=" * 35)
    
    for i in range(10):
        print(f"\n-> Buku ke-{i+1}:")
        judul = input("Judul Buku      : ")
        pengarang   = input("Nama Pengarang  : ")
        
        # Validasi Harga (> 0)
        while True:
            try:
                harga = int(input("Harga (Rp)      : "))
                if harga > 0:
                    break
                print("Harga harus lebih dari Rp 0!")
            except ValueError:
                print("Masukkan angka yang valid!")
                
        while True:
            try:
                stok = int(input("Stok            : "))
                if stok >= 0:
                    break
                print("Stok tidak boleh bernilai negatif!")
            except ValueError:
                print("Masukkan angka yang valid!")
                
        books.append({
            "judul": judul,
            "pengarang": pengarang,
            "harga": harga,
            "stok": stok
        })
    print("\nData 10 buku berhasil dimasukkan!")

def tampilkan_semua(books):
    if not books:
        print("\nData buku belum tersedia. Silakan input data terlebih dahulu.")
        return
        
    print("\n" + "=" * 70)
    print("                         DAFTAR SEMUA BUKU")
    print("=" * 70)
    print(f"{'No':<3} | {'Judul Buku':<25} | {'Pengarang':<15} | {'Harga':<12} | {'Stok':<5}")
    print("-" * 70)
    
    for i, buku in enumerate(books, start=1):
        print(f"{i:<3} | {buku['judul']:<25} | {buku['pengarang']:<15} | Rp {buku['harga']:<10} | {buku['stok']:<5}")
    
    print("-" * 70)

def hitung_total_nilai_stok(books):
    total_nilai = 0
    for buku in books:
        total_nilai += (buku['harga'] * buku['stok'])
    return total_nilai

def bubble_sort_harga(books):
    n = len(books)
    for i in range(n):
        for j in range(0, n - i - 1):
            if books[j]['harga'] > books[j + 1]['harga']:
                # Tukar posisi
                books[j], books[j + 1] = books[j + 1], books[j]

def binary_search_harga(books, target_harga):
    low = 0
    high = len(books) - 1
    ditemukan_indeks = []
    
    while low <= high:
        mid = (low + high) // 2
        if books[mid]['harga'] == target_harga:
            left = mid
            while left >= 0 and books[left]['harga'] == target_harga:
                ditemukan_indeks.append(left)
                left -= 1
            right = mid + 1
            while right < len(books) and books[right]['harga'] == target_harga:
                ditemukan_indeks.append(right)
                right += 1
            break
        elif books[mid]['harga'] < target_harga:
            low = mid + 1
        else:
            high = mid - 1
            
    return [books[i] for i in sorted(list(set(ditemukan_indeks)))]

def insertion_sort_stok(books):
    for i in range(1, len(books)):
        key = books[i]
        j = i - 1
        while j >= 0 and books[j]['stok'] < key['stok']:
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = key

def laporan_stok_menipis(books):
    stok_kritis = []
    for buku in books:
        if buku['stok'] <= 3:
            stok_kritis.append(buku)
    return stok_kritis

def main():
    data_buku = []
    
    input_data(data_buku)
    
    while True:
        print("\n" + "=" * 45)
        print("          MENU UTAMA TOKO BUKU")
        print("=" * 45)
        print("1. Tampilkan Semua Buku")
        print("2. Hitung Total Nilai Stok")
        print("3. Urutkan Buku Berdasarkan Harga (Termurah)")
        print("4. Cari Buku Berdasarkan Harga")
        print("5. Urutkan Buku Berdasarkan Stok (Terbanyak)")
        print("6. Laporan Stok Menipis (≤ 3)")
        print("7. Keluar")
        print("=" * 45)
        
        pilih = input("Pilih menu (1-7): ")
        
        if pilih == "1":
            tampilkan_semua(data_buku)
            
        elif pilih == "2":
            total = hitung_total_nilai_stok(data_buku)
            print(f"\nTotal nilai keseluruhan stok buku saat ini adalah: Rp {total:,}")
            
        elif pilih == "3":
            bubble_sort_harga(data_buku)
            print("\nData buku telah diurutkan berdasarkan harga (Termurah - Termahal):")
            tampilkan_semua(data_buku)
            
        elif pilih == "4":
            bubble_sort_harga(data_buku)
            try:
                target = int(input("\nMasukkan harga buku yang dicari (Rp): "))
                hasil_cari = binary_search_harga(data_buku, target)
                
                if hasil_cari:
                    print(f"\nDitemukan {len(hasil_cari)} buku dengan harga Rp {target:,}:")
                    print("-" * 50)
                    for idx, b in enumerate(hasil_cari, 1):
                        print(f"{idx}. Judul: {b['judul']} | Pengarang: {b['pengarang']} | Stok: {b['stok']}")
                    print("-" * 50)
                else:
                    print(f"\nTidak ditemukan buku dengan harga Rp {target:,}.")
            except ValueError:
                print("Masukkan angka harga berupa integer!")
                
        elif pilih == "5":
            insertion_sort_stok(data_buku)
            print("\nData buku telah diurutkan berdasarkan stok (Terbanyak - Tersedikit):")
            tampilkan_semua(data_buku)
            
        elif pilih == "6":
            kritis = laporan_stok_menipis(data_buku)
            print(f"\nLAPORAN STOK MENIPIS (≤ 3 pcs): Ditemukan {len(kritis)} buku.")
            if kritis:
                print("-" * 60)
                print(f"{'Judul Buku':<25} | {'Pengarang':<15} | {'Sisa Stok':<5}")
                print("-" * 60)
                for b in kritis:
                    print(f"{b['judul']:<25} | {b['pengarang']:<15} | {b['stok']:<5}")
                print("-" * 60)
            else:
                print("Semua stok buku masih dalam kondisi aman.")
                
        elif pilih == "7":
            print("\nTerima kasih telah menggunakan sistem Toko Buku Aksara. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-7.")

if __name__ == "__main__":
    main()