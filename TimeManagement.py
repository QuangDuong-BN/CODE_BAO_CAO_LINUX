import tkinter as tk
from tkinter import ttk
import subprocess
import time


def get_system_time():
    return subprocess.check_output("date '+%H:%M:%S'", shell=True).decode().strip()


def get_system_date():
    return subprocess.check_output("date '+%Y-%m-%d'", shell=True).decode().strip()


def set_system_time():
    time_input = time_entry.get()
    subprocess.run(f"sudo date -s {time_input}", shell=True)
    update_time()


def set_system_date():
    date_input = date_entry.get()
    subprocess.run(f"sudo date -s {date_input}", shell=True)
    update_date()


def update_time():
    time_label.config(text=get_system_time())
    root.after(1000, update_time)


def update_date():
    date_label.config(text=get_system_date())


def turn_on_timeauto():
    subprocess.run(f"sudo timedatectl set-ntp true", shell=True)


def turn_off_timeauto():
    subprocess.run(f"sudo timedatectl set-ntp false", shell=True)


root = tk.Tk()
root.title("Thời gian hệ thống")
root.geometry("500x400")

frame = ttk.Frame(root)
frame.pack(pady=20)

time_label = ttk.Label(frame, text=get_system_time(), font=("Helvetica", 20))
time_label.pack()

date_label = ttk.Label(frame, text=get_system_date(), font=("Helvetica", 16))

date_label.pack(pady=10)

time_entry_label = ttk.Label(frame, text="Nhập thời gian (giờ:phút:giây):", font=("Helvetica", 12))
time_entry_label.pack(pady=5)

time_entry = ttk.Entry(frame)
time_entry.pack(pady=5)

time_set_button = ttk.Button(frame, text="Đặt giờ", command=set_system_time)
time_set_button.pack(pady=5)

date_entry_label = ttk.Label(frame, text="Nhập ngày (năm-tháng-ngày):", font=("Helvetica", 12))
date_entry_label.pack(pady=5)

date_entry = ttk.Entry(frame)
date_entry.pack(pady=5)

date_set_button = ttk.Button(frame, text="Đặt ngày", command=set_system_date)
date_set_button.pack(pady=5)

turnOnAuto = ttk.Button(frame, text="Bật tự động cập nhật thời gian từ máy chủ NTP", command=turn_on_timeauto)
turnOnAuto.pack(pady=10)

turnOffAuto = ttk.Button(frame, text="Tắt tự động cập nhật thời gian từ máy chủ NTP", command=turn_off_timeauto)
turnOffAuto.pack(pady=10)

update_time()
root.mainloop()
