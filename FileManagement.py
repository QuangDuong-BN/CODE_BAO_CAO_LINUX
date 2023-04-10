import tkinter as tk
from tkinter import ttk
import os
import tkinter.filedialog as filedialog
from tkinter import messagebox

class ProcessManager(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("File Management")
        self.master.geometry("800x600")
        self.file_path = tk.StringVar() # define file_path as an instance variable
        self.create_widgets()
        

    def create_widgets(self):
        
        # Tạo Notebook
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(side="left", fill="both", expand=True)

        # Tạo tab1
        self.tab1 = tk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Create, Open, and Delete file")

        self.createFileButton = tk.Button(self.tab1, text="Create file", command=self.create_file,font=("Helvetica", 20))
        self.createFileButton.pack(pady=30,padx=10)

        self.openFileButton = tk.Button(self.tab1, text="Open file", command=self.open_file, font=("Helvetica", 20))
        self.openFileButton.pack(pady=30)

        self.deleteFileButton = tk.Button(self.tab1, text="Delete file", command=self.delete_file, font=("Helvetica", 20))
        self.deleteFileButton.pack(pady=30)

        # Tạo tab2 để tùy biến
        self.tab2 = tk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Rename file")

        self.label3 = tk.Label(self.tab2, text="Chon file can thay doi ten:", font=("Helvetica", 30))
        self.label3.pack(pady=10)
        
        self.inputName_label = tk.Label(self.tab2, width=50,text="Duong dan file",font=("Helvetica", 20))
        self.inputName_label.pack(padx=20, pady=10)
	
        self.choose_button = tk.Button(self.tab2, text="choose", command=self.choose_file, font=("Helvetica", 25))
        self.choose_button.pack(pady=10)
	
        self.label4 = tk.Label(self.tab2, text="Nhap ten moi ma ban muon doi:", font=("Helvetica", 25))
        self.label4.pack(pady=10)
        	
        self.inputReame_entry = tk.Entry(self.tab2, width=50, font=("Helvetica", 20))
        self.inputReame_entry.pack(padx=20, pady=10)
                
        self.rename_button = tk.Button(self.tab2, text="Rename", command=self.rename_file, font=("Helvetica", 25))
        self.rename_button.pack(pady=10)


    # Hàm tạo mới tệp tin
    def create_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write("")
            self.file_path.set(file_path)

    # Hàm mở tệp tin
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            os.system("gedit " + file_path)

    # Hàm lưu tệp tin
    def save_file(self):
        file_path = self.file_path.get()
        if file_path:
            with open(file_path, "w") as file:
                contents = file.write("Hello World")

    # Hàm xóa tệp tin
    def delete_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            os.remove(file_path)
            
            
    def choose_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            self.file_path.set(file_path)
            self.inputName_label.config(text=file_path)
        
    # Hàm rename tệp tin
    def rename_file(self):
        file_path = self.file_path.get()
        input_rename= self.inputReame_entry.get()
        cmd = "mv " + file_path + " " + input_rename
        exit_status = os.system(cmd)
        if os.WEXITSTATUS(exit_status) == 0:
            messagebox.showinfo("Rename", "Rename successful!")
        else:
            messagebox.showerror("Rename", "Rename failed!")


def main():
    root = tk.Tk()
    app = ProcessManager(root)
    root.mainloop()


if __name__ == '__main__':
    main()
