from PIL import Image

def convert_to_grayscale(image_path):
    # Mở hình ảnh
    img = Image.open(image_path)
    
    # Chuyển đổi sang chế độ "L" (xám đen)
    img_gray = img.convert('L')
    
    # Lưu hình ảnh mới
    img_gray.save('gray_image.jpg')

# Thực hiện chuyển đổi trên một hình ảnh cụ thể
convert_to_grayscale('Hoa.jpg')
