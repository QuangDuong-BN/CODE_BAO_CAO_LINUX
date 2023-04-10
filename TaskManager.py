import tkinter as tk
from crontab import CronTab
import os
class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")
        
        # Khởi tạo đối tượng CronTab
        self.cron = CronTab(user='duong')
        
        # Tạo các widget
        tk.Label(self.master, text="Task Name").grid(row=0, column=0)
        self.task_name_entry = tk.Entry(self.master)
        self.task_name_entry.grid(row=0, column=1)
        
        tk.Label(self.master, text="Command").grid(row=1, column=0)
        self.command_entry = tk.Entry(self.master)
        self.command_entry.grid(row=1, column=1)
        
        tk.Label(self.master, text="Schedule").grid(row=2, column=0)
        self.schedule_entry = tk.Entry(self.master)
        self.schedule_entry.grid(row=2, column=1)
        
        self.create_button = tk.Button(self.master, text="Create Task", command=self.create_task)
        self.create_button.grid(row=3, column=0)
        
        self.list_button = tk.Button(self.master, text="List Tasks", command=self.list_tasks)
        self.list_button.grid(row=3, column=1)
        
        self.remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=3, column=2)
        
        self.edit_button = tk.Button(self.master, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=3, column=3)
        
        self.output_text = tk.Text(self.master, height=10, width=80)
        self.output_text.grid(row=4, column=0, columnspan=4)
        
    def create_task(self):
        # Lấy thông tin từ các widget
        task_name = self.task_name_entry.get()
        command = self.command_entry.get()
        schedule = self.schedule_entry.get()
        
        # Tạo một tác vụ mới
        job = self.cron.new(command=command)
        job.setall(schedule)
        job.set_comment(task_name)
        
        # Lưu tác vụ vào lịch trình cron
        self.cron.write()
        
        # Xóa nội dung của các widget
        self.task_name_entry.delete(0, tk.END)
        self.command_entry.delete(0, tk.END)
        self.schedule_entry.delete(0, tk.END)
        
        # Hiển thị thông báo thành công
        self.output_text.insert(tk.END, "Task created successfully!\n")
        
    def list_tasks(self):
    	#os.system('crontab -e')
        # Lấy danh sách tất cả các tác vụ
        jobs = self.cron.find_comment('*')
        
        # Hiển thị danh sách các tác vụ
        self.output_text.delete('1.0', tk.END)
        for job in self.cron:
            self.output_text.insert(tk.END, f"Task Name: {job.comment}\n")
            self.output_text.insert(tk.END, f"Command: {job.command}\n")
            self.output_text.insert(tk.END, f"Schedule: {str(job)}\n\n")
        
    def remove_task(self):
        # Lấy tên tác vụ muốn xóa
        task_name = self.task_name_entry.get()

        # Tìm tác vụ theo tên
        job = list(self.cron.find_comment(task_name))

        if job:
            # Xóa tác vụ
            self.cron.remove(job[0])
            self.cron.write()

            # Xóa nội dung của các widget
            self.task_name_entry.delete(0, tk.END)

            # Hiển thị thông báo thành công
            self.output_text.insert(tk.END, "Task removed successfully!\n")
        else:
            self.output_text.insert(tk.END, "Task not found!\n")

        
    def edit_task(self):
	    # Lấy tên tác vụ muốn sửa đổi
        task_name = self.task_name_entry.get()
	    
	    # Tìm tác vụ theo tên
        job = None
        for task in self.cron:
            if task.comment == task_name:
                job = task
                break
	    
	    # Hiển thị thông tin tác vụ trong các widget
        if job is not None:
            self.task_name_entry.delete(0, tk.END)
            self.task_name_entry.insert(0, job.comment)
            self.command_entry.delete(0, tk.END)
            self.command_entry.insert(0, job.command)
            
            self.schedule_entry.delete(0, tk.END)
            
            self.schedule_entry.insert(0, str(job))
		
		# Xóa tác vụ
            self.cron.remove(job)
            self.cron.write()
            
		
		# Hiển thị thông báo thành công
            self.output_text.insert(tk.END, "Task edit successfully!\n")
        else:
            self.output_text.insert(tk.END, "Task not found!\n")    
     
root = tk.Tk()
app = TaskManager(root)
root.mainloop()

