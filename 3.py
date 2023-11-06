import tkinter as tk
from tkinter import ttk
import pandas as pd
import requests
from io import BytesIO
from requests.auth import HTTPBasicAuth



sever_id = "http://117.2.91.179"
path = "CT89/data/DSKHMOI.xlsx"
url = f'{sever_id}/{path}'
user_name = "crawler"
pass_word = "Dung28032016@"
# đăng nhập:
auth = HTTPBasicAuth(user_name, pass_word)
# tải file:
response = requests.get(url, auth=auth)
def search_info():
    # Đọc dữ liệu từ tệp Excel
    # file_path = "data/DSKHMOI.xlsx"  # Thay đổi đường dẫn đến tệp Excel của bạn
    # df = pd.read_excel(file_path)
    if response.status_code ==200:
        data = response.content
        df = pd.read_excel(BytesIO(data))
    
    # Lấy giá trị từ trường nhập liệu
    search_value = input_entry.get()
    
    # Tìm các thông tin trong dòng chứa giá trị tương ứng
    result = df[(df['TEN_KHANG'] == search_value) | (df['DIA_CHI'] == search_value) | (df['SO_DIEN_THOAI'] == search_value)]
    
    if not result.empty:
        result_label.config(text=f"Tên: {result['TEN_KHANG'].values[0]}\nĐịa chỉ: {result['DIA_CHI'].values[0]}\nSố điện thoại: {result['SO_DIEN_THOAI'].values[0]}")
    else:
        result_label.config(text="Không tìm thấy thông tin.")

# Tạo giao diện tkinter
root = tk.Tk()
root.title("Tìm thông tin từ Excel")

# Tạo và cấu hình các thành phần giao diện
label = tk.Label(root, text="Nhập thông tin tìm kiếm:")
input_entry = tk.Entry(root)
search_button = tk.Button(root, text="Tìm", command=search_info)
result_label = tk.Label(root, text="Kết quả sẽ được hiển thị ở đây")

label.pack()
input_entry.pack()
search_button.pack()
result_label.pack()

root.mainloop()
