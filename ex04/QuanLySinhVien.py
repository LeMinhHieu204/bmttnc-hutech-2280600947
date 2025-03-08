from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxID = 1
        if self.soluongSinhVien() > 0:
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxID < sv._id:
                    maxID = sv._id
            maxID = maxID + 1
        return maxID

    def soluongSinhVien(self):
        return len(self.listSinhVien)  # Sử dụng len() thay cho __len__()

    def nhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xeploaiHocLuc(sv)  # Sửa thành xeploaiHocLuc để khớp với định nghĩa
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")  # Sửa int thành input vì major là chuỗi
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xeploaiHocLuc(sv)  # Sửa thành xeploaiHocLuc để khớp với định nghĩa

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)  # Sửa _listSinhVien thành listSinhVien

    def sortByNAME(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)  # Sửa _listSinhVien thành listSinhVien

    def sortByDIEMTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)  # Sửa _listSinhVien thành listSinhVien

    def findByID(self, ID):
        for sv in self.listSinhVien:  # Sửa _listSinhVien thành listSinhVien
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        listSV = []
        for sv in self.listSinhVien:  # Sửa _listSinhVien thành listSinhVien
            if keyword.upper() in sv._name.upper():
                listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)  # Sửa _listSinhVien thành listSinhVien
            return True
        return False

    def xeploaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"  # Sửa _HOCLUC thành _hocLuc
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung bình"  # Sửa _HOCLUC thành _hocLuc
        else:
            sv._hocLuc = "Yếu"  # Sửa _HOCLUC thành _hocLuc

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if len(listSV) > 0:  # Sử dụng len() thay cho __len__()
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(
                    sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))  # Sửa truy cập thuộc tính
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien