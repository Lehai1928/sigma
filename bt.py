class book:
    def __init__(self,id,name,author,nam_xuat_ban):
        self._name = name 
        self._id = id
        self._author = author
        self._nam_xuat_ban = nam_xuat_ban
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._id

    def set_name(self, id):
        self._id = id

    def get_name(self):
        return self._author

    def set_name(self, author):
        self._author = author

    def get_name(self):
        return self._name

    def set_name(self, nam_xuat_ban):
        self._nam_xuat_ban = nam_xuat_ban

    @abstractmethod
    def display_info(self):
        pass
class  physicalBook(book):
    def __init__(self, id, name, author, nam_xuat_ban,so_luong,vi_tri):
        super().__init__(id, name, author, nam_xuat_ban)
        self._so_luong = so_luong
        self._vi_tri = vi_tri
    def get_so_luong(self):
        return self.get_so_luong
    
    def set_so_luong(self,so_luong):
        self._so_luong = so_luong

    def get_vi_tri(self):
        return self.get_vi_tri
    
    def set_vi_tri(self,vi_tri):
        self._vi_tri = vi_tri
    
    def display_info(self):
        print(f"[Sách giấy] Mã: {self.get_id()}, Tên:{self.get_name()},"
              f"Tác giả: {self.get_author()}, Năm: {self.get_nam_xuat_ban()}"
              f"Số lượng: {self.get_so_luong()}, Vị trí: {self.get_vi_tri()}")
        
class  eBook(book):
    def __init__(self, id, name, author, nam_xuat_ban,dung_luong,dinh_dang):
        super().__init__(id, name, author, nam_xuat_ban)
        self._dung_luong = dung_luong
        self._dinh_dang = dinh_dang
    def get_dung_luong(self):
        return self.get_dung_luong
    
    def set_dung_luong(self,dung_luong):
        self._dung_luong = dung_luong

    def get_dinh_dang(self):
        return self.get_dinh_dang
    
    def set_dinh_dang(self,dinh_dang):
        self._dinh_dang = dinh_dang
    
    def display_info(self):
        print(f"[E-book] Mã: {self.get_id()}, Tên:{self.get_name()},"
              f"Tác giả: {self.get_author()}, Năm: {self.get_nam_xuat_ban()}"
              f"Dung lượng: {self.get_dung_luong()}MB, Định dạng: {self.get_dinh_dang()}")
        
class library:
    def __init__(self):
        self.book = []
    def add_book(self,book):
        self.book.append(book)
        print("Thêm sách thành công")

    def display_all_books(self):
        if not self.books:
            print("Thư viện trống!")
        else:
            for book in self.books:
                book.display_info()
    def find_book_by_id()
            