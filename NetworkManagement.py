import subprocess
import tkinter as tk
from tkinter import ttk
import os


class ProcessManager(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Network Management")
        self.master.geometry("700x600")
        self.create_widgets()

    def create_widgets(self):
        # Tạo Notebook
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(side="left", fill="both", expand=True)

        # Tạo tab1
        self.tab1 = tk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="List usb device")

        # Tạo Listbox để hiển thị thông tin các process trong tab1
        self.listbox = tk.Listbox(self.tab1, height=20, width=80)
        self.listbox.pack(pady=10)

        # Nút Reload để cập nhật lại danh sách USB
        self.reload_button = tk.Button(self.tab1, text="Reload", command=self.update_usb_devices)
        self.reload_button.pack(pady=10)

        # Tạo tab2 để tùy biến
        self.tab2 = tk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="WIFI, BlueTooth setting and Airplane mode")

        self.label3 = tk.Label(self.tab2, text="WIFI setting:")
        self.label3.pack(pady=10)

        self.turnOnWIFI = tk.Button(self.tab2, text="turn On WIFI", command=self.defTurnOnWIFI)
        self.turnOnWIFI.pack(pady=10)

        self.turnOffWIFI = tk.Button(self.tab2, text="turn Off WIFI", command=self.defTurnOffWIFI)
        self.turnOffWIFI.pack(pady=10)

        self.label4 = tk.Label(self.tab2, text="BlueTooth setting:")
        self.label4.pack(pady=10)

        self.turnOnBlueTooth = tk.Button(self.tab2, text="Turn On BlueTooth", command=self.defTurnOnBlueTooth)
        self.turnOnBlueTooth.pack(pady=10)

        self.turnOffBlueTooth = tk.Button(self.tab2, text="Turn Off BlueTooth", command=self.defTurnOffBlueTooth)
        self.turnOffBlueTooth.pack(pady=10)

        self.label5 = tk.Label(self.tab2, text="Airplane mode setting:")
        self.label5.pack(pady=10)

        self.turnOnAirplane = tk.Button(self.tab2, text="Turn On Airplane", command=self.defTurnOnAirplane)
        self.turnOnAirplane.pack(pady=10)

        self.turnOffAirplane = tk.Button(self.tab2, text="Turn Off Airplane", command=self.defTurnOffAirplane)
        self.turnOffAirplane.pack(pady=10)


        # Hiển thị danh sách USB ban đầu
        self.update_usb_devices()

    def defTurnOnAirplane(self):
        cmd = "nmcli radio all off"
        os.system(cmd)
        cmd1 = "sudo rfkill block bluetooth"
        os.system(cmd1)

    def defTurnOffAirplane(self):
        cmd = "nmcli radio all on"
        os.system(cmd)
        cmd1 = "sudo rfkill unblock bluetooth"
        os.system(cmd1)

    def get_usb_devices(self):
        # Thực hiện lệnh lsusb và lấy kết quả trả về
        output = subprocess.check_output("lsusb").decode("utf-8")
        devices = output.splitlines()
        return devices

    def update_usb_devices(self):
        # Xóa danh sách USB hiện tại
        self.listbox.delete(0, tk.END)
        # Lấy danh sách USB mới
        devices = self.get_usb_devices()
        # Hiển thị danh sách USB mới trên Listbox
        for device in devices:
            self.listbox.insert(tk.END, device)

    def defTurnOnWIFI(self):
        cmd = "nmcli radio wifi on"
        os.system(cmd)

    def defTurnOffWIFI(self):
        cmd = "nmcli radio wifi off"
        os.system(cmd)

    def defTurnOnBlueTooth(self):
        cmd = "sudo rfkill unblock bluetooth"
        os.system(cmd)

    def defTurnOffBlueTooth(self):
        cmd = "sudo rfkill block bluetooth"
        os.system(cmd)


def main():
    root = tk.Tk()
    app = ProcessManager(root)
    root.mainloop()


if __name__ == '__main__':
    main()
