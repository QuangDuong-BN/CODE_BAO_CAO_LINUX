import tkinter as tk
import os

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Ứng dụng xóa và cài đặt package")

        # Thiết lập kích thước và vị trí của cửa sổ
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        window_width = 800
        window_height = 600
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # Tạo một label
        self.label = tk.Label(master, text="Danh sách các package có thể xóa:")
        self.label.pack(pady=10)

        # Hiển thị các package có thể xóa
        # Tạo một đối tượng Scrollbar và liên kết nó với Listbox
        scrollbar = tk.Scrollbar(self.master)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(self.master, height=20, width=80, yscrollcommand=scrollbar.set)
        self.listbox.pack(padx=20, pady=10)

        # Thiết lập phương thức cập nhật Scrollbar
        scrollbar.config(command=self.listbox.yview)

        
        # Tạo một label
        self.label2 = tk.Label(master, text="Nhập tên package cần xóa:")
        self.label2.pack(pady=10)

        # Ô nhập tên package cần xóa
        self.delete_entry = tk.Entry(master, width=50)
        self.delete_entry.pack(padx=20, pady=10)
        
        # Nút xóa package
        self.delete_button = tk.Button(master, text="Xóa package", command=self.delete_package)
        self.delete_button.pack(pady=10)

        # Tạo một label
        self.label3 = tk.Label(master, text="Nhập tên package cần cài đặt:")
        self.label3.pack(pady=10)

        # Ô nhập tên package cần cài đặt
        self.install_entry = tk.Entry(master, width=50)
        self.install_entry.pack(padx=20, pady=10)

        # Nút cài đặt package
        self.install_button = tk.Button(master, text="Cài đặt package", command=self.install_package)
        self.install_button.pack(pady=10)

        # Hiển thị danh sách các package
        self.show_package_list()

    def show_package_list(self):
        # Sử dụng lệnh shell để lấy danh sách các package có thể xóa
        cmd = "dpkg --list | grep ^ii | awk '{print $2}'"
        package_list = os.popen(cmd).read().split('\n')
        package_list.sort()

        # Hiển thị danh sách các package
        for package in package_list:
            self.listbox.insert(tk.END, package)

    def delete_package(self):
        # Lấy tên package từ ô nhập liệu
        package_name = self.delete_entry.get()

        # Sử dụng lệnh shell để xóa package
        cmd = "sudo apt-get -y remove " + package_name
        os.system(cmd)

        # Xóa nội dung ô nhập liệu
        self.delete_entry.delete(0, tk.END)

        # Cập nhật lại danh sách các package
        self.listbox.delete(0, tk.END)
        self.show_package_list()
        
    def install_package(self):
        # Lấy tên package từ ô nhập liệu
        package_name = self.install_entry.get()

        # Sử dụng lệnh shell để cài đặt package
        cmd = "sudo apt-get -y install " + package_name
        os.system(cmd)

        # Xóa nội dung ô nhập liệu
        self.install_entry.delete(0, tk.END)

        # Cập nhật lại danh sách các package
        self.listbox.delete(0, tk.END)
        self.show_package_list()

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()

       

