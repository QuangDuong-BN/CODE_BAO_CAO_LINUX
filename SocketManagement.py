import tkinter as tk
import subprocess

# Tạo một cửa sổ
root = tk.Tk()
root.geometry('800x600')

# Tạo một khu vực văn bản
text = tk.Text(root, height=30, width=100)
text.pack(side=tk.LEFT, fill=tk.BOTH)

# Thêm thanh cuộn
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Kết nối thanh cuộn và khu vực văn bản
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

# Chạy lệnh netstat -a và ghi kết quả vào khu vực văn bản
output = subprocess.check_output(['netstat', '-a'])
text.insert(tk.END, output)

# Bắt đầu vòng lặp chính của ứng dụng
root.mainloop()

