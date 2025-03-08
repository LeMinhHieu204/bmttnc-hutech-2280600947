from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:  # Sửa while (1 == 1) thành while True cho gọn
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU**************************")
    print("** 1. Them sinh vien. **")
    print("** 2. Cap nhat thong tin sinh vien boi ID. **")
    print("** 3. Xoa sinh vien boi ID. **")
    print("** 4. Tim kiem sinh vien theo ten. **")
    print("** 5. Sap xep sinh vien theo diem trung binh. **")
    print("** 6. Sap xep sinh vien theo ten. **")  # Sửa "theo ten chuyen nganh" thành "theo ten" cho đúng với sortByNAME
    print("** 7. Hien thi danh sach sinh vien. **")
    print("** 8. Thoat **")
    print("******************************************************")

    key = int(input("Nhap tuy chon: "))
    if key == 1:
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nTHEM SINH VIEN THANH CONG!")
    elif key == 2:
        if qlsv.soluongSinhVien() > 0:  # Sửa soLuongSinhVien thành soluongSinhVien
            print("\n2. Cap nhat thong tin sinh vien.")
            ID = int(input("Nhap ID: "))
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 3:
        if qlsv.soluongSinhVien() > 0:  # Sửa soLuongSinhVien thành soluongSinhVien
            print("\n3. Xoa sinh vien.")
            ID = int(input("Nhap ID: "))
            if qlsv.deleteById(ID):
                print(f"\nSinh vien co id = {ID} da bi xoa.")
            else:
                print(f"\nSinh vien co id = {ID} khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 4:
        if qlsv.soluongSinhVien() > 0:  # Sửa soLuongSinhVien thành soluongSinhVien
            print("\n4. Tim kiem sinh vien theo ten...")
            name = input("Nhap ten de tim kiem: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 5:
        if qlsv.soluongSinhVien() > 0:  # Sửa soLuongSinhVien thành soluongSinhVien
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDIEMTB()  # Sửa sortByDiemTB thành sortByDIEMTB
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 6:
        if qlsv.soluongSinhVien() > 0:  # Sửa SOLUONGSINHVIEN thành soluongSinhVien
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByNAME()  # Sửa sortByName thành sortByNAME
            qlsv.showSinhVien(qlsv.getListSinhVien())  # Sửa showSINHVIEN thành showSinhVien
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 7:
        if qlsv.soluongSinhVien() > 0:  # Sửa SOLUONGSINHVIEN thành soluongSinhVien
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())  # Sửa showSINHVIEN thành showSinhVien
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 8:  # Sửa key == 0 thành key == 8 để khớp với menu
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")