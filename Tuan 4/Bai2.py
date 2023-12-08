import numpy as np
from PIL import Image

def grayscale_to_rgb(image_path):
    # Mở hình ảnh xám đen
    img_gray = Image.open(image_path)
    
    # Chuyển đổi thành mảng numpy
    img_array = np.array(img_gray)
    
    # Tạo ma trận màu
    img_rgb = np.zeros((img_array.shape[0], img_array.shape[1], 3), dtype=np.uint8)
    
    # Gán giá trị màu giống nhau cho cả ba kênh
    img_rgb[:,:,0] = img_array
    img_rgb[:,:,1] = img_array
    img_rgb[:,:,2] = img_array
    
    # Chuyển đổi thành hình ảnh PIL
    img_color = Image.fromarray(img_rgb, 'RGB')
    
    # Lưu hình ảnh màu
    img_color.save('matran3.jpg')

# Thực hiện chuyển đổi trên một hình ảnh xám đen cụ thể
grayscale_to_rgb('gray_image.jpg')
