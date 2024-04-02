import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageFont, ImageDraw

# Add comment indicating ownership
# "This code belongs to ShortTemperd007"

def encrypt_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        width, height = image.size

        # Iterate through each pixel and swap RGB values
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                image.putpixel((x, y), (g, b, r))  # Swapping RGB values

        encrypted_image_path = file_path.split('.')[0] + "_encrypted.png"
        image.save(encrypted_image_path)
        messagebox.showinfo("Success", "Image encrypted successfully.\nEncrypted image saved as: " + encrypted_image_path, font=('Helvetica', 12))

def decrypt_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        width, height = image.size

        # Iterate through each pixel and swap RGB values back to original
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                image.putpixel((x, y), (b, r, g))  # Swapping RGB values back to original

        decrypted_image_path = file_path.split('_encrypted')[0] + "_decrypted.png"
        image.save(decrypted_image_path)
        messagebox.showinfo("Success", "Image decrypted successfully.\nDecrypted image saved as: " + decrypted_image_path, font=('Helvetica', 12))

# Create main window
root = tk.Tk()
root.title("Image Encryption Tool")

# Create label for your name in big and amazing font
label_name = tk.Label(root, text="ShortTemperd", font=('Comic Sans MS', 24))
label_name.pack(pady=10)

# Create buttons
encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_image, font=('Helvetica', 12))
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_image, font=('Helvetica', 12))
decrypt_button.pack(pady=10)

# Start the GUI
root.mainloop()
