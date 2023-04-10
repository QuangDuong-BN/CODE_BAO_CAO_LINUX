import subprocess
import tkinter as tk
from tkinter import ttk
import os

class ProcessManager(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Process Manager")
        self.master.geometry("700x400")
        self.create_widgets()

    def create_widgets(self):
        # Tạo Notebook
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(side="left", fill="both", expand=True)

        # Tạo tab1
        self.tab1 = tk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="List Processes")

        # Tạo Listbox để hiển thị thông tin các process trong tab1
        self.process_listbox = tk.Listbox(self.tab1, height=20)
        self.process_listbox.pack(side="left", fill="both", expand=True)

        # Thêm các cột vào Listbox
        self.process_listbox.insert(0, "PID --- User --- CPU --- Memory --- Name")

        # Cập nhật danh sách process sau mỗi giây
        self.update_process_list()

        # Tạo tab2 để tùy biến
        self.tab2 = tk.Frame(self.notebook)
        self.notebook.add(self.tab2,text="Kill Processs")
        
        
        self.label3 = tk.Label(self.tab2,text="Nhập PID(Processs ID) muốn kill:")
        self.label3.pack(pady=10)
        
        #input
        self.inputPID = tk.Entry(self.tab2, width=50)
        self.inputPID.pack(padx=20, pady=10)

        # Nút cài đặt package 
        self.install_button = tk.Button(self.tab2,text="Kill Processs",command=self.killProcess)
        self.install_button.pack(pady=10)
        

    def update_process_list(self):
        # Xóa các dòng cũ trong Listbox
        self.process_listbox.delete(1, tk.END)

        # Lấy danh sách các process đang chạy
        process_output = subprocess.check_output(["ps", "aux"]).decode("utf-8")
        process_list = process_output.strip().split("\n")[1:]

        # Thêm thông tin các process vào Listbox
        for process in process_list:
            process_items = process.split()
            process_pid = process_items[1]
            process_user = process_items[0]
            process_cpu = process_items[2]
            process_memory = process_items[3]
            process_name = process_items[10]
            process_item = f"{process_pid} --- {process_user} --- {process_cpu}% --- {process_memory}% --- {process_name}"
            self.process_listbox.insert(tk.END, process_item)

        # Cập nhật danh sách sau mỗi giây
        self.master.after(10000, self.update_process_list)
        
    def killProcess(self):
        #Lấy tên package từ ô nhập liệu
        PID = self.inputPID.get()

        #Sử dụng lệnh shell để cài đặt package
        cmd = "kill " + PID
        os.system(cmd)
    
def main():
    root = tk.Tk()
    app = ProcessManager(root)
    root.mainloop()

if __name__ == '__main__':
    main()

