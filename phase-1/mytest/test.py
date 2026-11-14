#import re

"""def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)"""

"""thislist = [100, 50, 65, 82, 23]
mean = statistics.mean(thislist)
print(mean)
median = statistics.median(thislist)
print(median)
mode = statistics.mode(thislist)
print(mode)
"""
"""import csv
with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)"""
# import os

# print(os.getcwd())

# #print(help(os))


# import sys

# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# print("Sum:", num1 + num2)
# import sys

# sys.stdout.write("Hello\n")
# sys.stderr.write("Error!\n")

# import urllib.request
# import urllib.error

# url = "http://example.com"
# headers = {'User-Agent': 'Mozilla/5.0'}

# try:
#     req = urllib.request.Request(url, headers=headers)
#     response = urllib.request.urlopen(req)
#     html = response.read().decode("utf-8")
#     print("Page length:", len(html), "characters")
# except urllib.error.URLError as e:
#     print("Failed to reach the server:", e.reason)

# text = "My numbers are 123 and 456"
# result = re.search(r'\d+', text)
# print(result)
# import urllib.request
# import urllib.parse
# import re

# url = 'http://pythonprogramming.net'

# try:
#     req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#     resp = urllib.request.urlopen(req)
#     respData = resp.read()

#     paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

#     for p in paragraphs:
#         print(p)

# except Exception as e:
#     print("Error:", e)
# import tkinter as tk

# def show_input():
#     text = entry.get()        # يجيب اللي كتبه المستخدم
#     label = tk.Label(window, text=text)
#     label.pack()

#     print("You typed:", text)

# def say_hello():
#     window = tk.Tk()
#     window.title("My First App")      # عنوان النافذة
#     window.geometry("400x300")        # الحجم: عرض x ارتفاع
#     label = tk.Label(window, text="Hello, World!")
#     label.pack()
#     button = tk.Button(window, text="Click Me", command=say_hello)
#     button.pack()
#     print("Button clicked!")

# window = tk.Tk()
# window.title("My First App")      # عنوان النافذة
# window.geometry("400x300")        # الحجم: عرض x ارتفاع
# label = tk.Label(window, text="Hello, World!")
# label.pack()
# button = tk.Button(window, text="Click Me", command=say_hello)
# button.pack()
# entry = tk.Entry(window)      # حقل إدخال
# entry.pack()

# button = tk.Button(window, text="Submit", command=show_input)
# button.pack()

# window.mainloop()
# import tkinter as tk

# def greet():
#     name = entry.get()
#     label.config(text="Hello, " + name + "!")    # يغيّر نص الـ label

# window = tk.Tk()
# window.title("Greeting App")
# window.geometry("300x200")

# label = tk.Label(window, text="Enter your name:")
# label.pack()

# entry = tk.Entry(window)
# entry.pack()

# button = tk.Button(window, text="Greet", command=greet)
# button.pack()

# window.mainloop()from tkinter import *
# from tkinter import *

# class Window(Frame):

#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.init_window()

#     def init_window(self):
#         self.master.title("GUI")
#         self.pack(fill=BOTH, expand=1)

#         quitButton = Button(self, text="Quit", command=self.client_exit)
#         quitButton.place(x=0, y=0)

#     def client_exit(self):
#         exit()


# root = Tk()
# root.geometry("400x300")

# app = Window(root)

# root.mainloop()
# import tkinter as tk

# window = tk.Tk()
# window.geometry("400x300")

# canvas = tk.Canvas(window, width=400, height=300, bg="white")

# canvas.pack()
# canvas.create_text(200, 50, text="Hello World", font=("Arial", 24), fill="blue")
# canvas.create_line(0, 0, 400, 300, fill="red", width=3)        # خط
# canvas.create_rectangle(50, 50, 150, 120, fill="lightgreen")   # مستطيل
# canvas.create_oval(200, 100, 300, 200, fill="orange")
# window.mainloop()
# import threading
# import time

# def long_task():
#     print("Task started...")
#     time.sleep(1)                      # يحاكي مهمة تاخد 5 ثواني
#     print("Task finished!")

# # ننشئ خيط ونعطيه الدالة
# thread = threading.Thread(target=long_task)
# thread.start()                         # نبدأ الخيط

# print("This prints immediately!")


# def greet(name, times):
#     for i in range(times):
#         print("Hello,", name)

# thread = threading.Thread(target=greet, args=("Yousef", 3))
# thread.start()
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# plt.style.use("seaborn-v0_8-darkgrid")

# plt.plot(x, y, color="red", linewidth=2, marker="o")
# plt.plot(x, y)          # ارسم خط

# days = [1, 2, 3, 4, 5, 6, 7]
# temperature = [22, 24, 19, 23, 25, 28, 26]
# x = [1, 2, 3, 4, 5]
# sales_2024 = [100, 120, 90, 150, 130]
# sales_2025 = [110, 140, 130, 160, 180]

# plt.plot(x, sales_2024, label="2024")      # اسم الخط الأول
# plt.plot(x, sales_2025, label="2025")      # اسم الخط الثاني


# plt.plot(days, temperature)

# plt.title("Weekly Temperature")        # عنوان الرسمة
# plt.xlabel("Day")                      # تسمية المحور الأفقي
# plt.ylabel("Temperature (°C)")         # تسمية المحور العمودي
# plt.legend()
# plt.grid(True)


# days = [1, 2, 3, 4, 5, 6, 7]
# temp = [22, 24, 19, 23, 25, 28, 26]

# plt.plot(days, temp, color="orange", marker="o", label="Temperature")

# plt.title("Weekly Temperature", fontsize=16, fontweight="bold")
# plt.xlabel("Day of Week")
# plt.ylabel("Temperature (°C)")
# plt.legend()
# plt.grid(True)

# with plt.style.context("dark_background"):
#     plt.plot([1, 2, 3], [4, 5, 6])
#     plt.show()


# plt.style.use("seaborn-v0_8")        # ثيم عصري

# days = [1, 2, 3, 4, 5, 6, 7]
# temp = [22, 24, 19, 23, 25, 28, 26]

# plt.plot(days, temp, marker="o", label="Temperature")

# plt.title("Weekly Temperature")
# plt.xlabel("Day")
# plt.ylabel("°C")
# plt.legend()

# plt.show()
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# product_a = [10, 15, 13, 18, 20]
# product_b = [8, 12, 16, 14, 19]
# product_c = [5, 9, 11, 13, 15]

# plt.plot(x, product_a, marker="o", label="Product A")
# plt.plot(x, product_b, marker="s", label="Product B")
# plt.plot(x, product_c, marker="^", label="Product C")

# plt.title("Product Sales")
# plt.xlabel("Month")
# plt.ylabel("Units Sold")

# plt.legend(loc="best", title="Products", shadow=True)

# plt.show()
# from ftplib import FTP
# ftp = FTP('www..google.com')          # عنوان السيرفر
# ftp.login()     # تسجيل الدخول

# print(ftp.getwelcome())
# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(("www.google.com", 80))     # نتصل بجوجل على منفذ 80
# request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
# s.send(request.encode())
# response = s.recv(4096)               # نستقبل حتى 4096 بايت
# print(response.decode())
# print("Connected!")
# s.close()
import socket

target = "127.0.0.1"

print(f"Scanning {target}...")

for port in range(1, 1025):              # نفحص المنافذ من 1 لـ 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)                      # مهلة ثانية لكل منفذ

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("Scan complete")

target = "192.168.1.50"        # IP الإنفرتر (مثال)
port = 80                       # منفذ مفتوح لقيته

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)

try:
    s.connect((target, port))
    banner = s.recv(1024)              # نستقبل الرسالة الترحيبية
    print("Banner:", banner.decode(errors="ignore"))
except Exception as e:
    print("Error:", e)
finally:
    s.close()
