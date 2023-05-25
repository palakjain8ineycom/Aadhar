import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import re


# def perform_ocr():
#     image_path = filedialog.askopenfilename(title="Select Aadhar Card Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
#     image = Image.open(image_path)
#     aadhar_number = pytesseract.image_to_string(image)
#     # aadhar_number = "".join(aadhar_number.split())
#     text_box.delete(1.0, tk.END)
#     text_box.insert(tk.END, "Aadhar Number: " + aadhar_number)


# def perform_ocr():
#     image_path = filedialog.askopenfilename(title="Select Aadhar Card Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
#     image = Image.open(image_path)
#     aadhar_number = pytesseract.image_to_string(image)
#     whole_text=aadhar_number
#     aadhar_number = "".join(aadhar_number.split())
#     start_index = aadhar_number.find("YourAadhaarNo.") + len("YourAadhaarNo.")
#     aadhar_number = aadhar_number[start_index:start_index + 12]
#     text_box.delete(1.0, tk.END)
#     text_box.insert(tk.END, "Image Data\n" + whole_text)
    
#     text_box2.delete(1.0, tk.END)
#     text_box2.insert(tk.END,"Aadhar Number: " + aadhar_number)

def perform_ocr():
    image_path = filedialog.askopenfilename(title="Select Aadhar Card Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    image = Image.open(image_path)
    aadhar_number = pytesseract.image_to_string(image)
    whole_text=aadhar_number
    # aadhar_number = "".join(aadhar_number.split())
    pattern = r"\b\d{4}\s\d{4}\s\d{4}\b"
    matches = re.findall(pattern, aadhar_number)
    
    text_box.delete(1.0, tk.END)
    if matches:
        text_box.insert(tk.END,"Aadhar Number: " + matches[0].replace(" ", ""))
    else:
        return ("Not found")
    
    text_box2.delete(1.0, tk.END)
    text_box2.insert(tk.END, whole_text)
    
    

#main window
window = tk.Tk()
window.title("Aadhar Card OCR")
window.geometry("1920x1080")

#button
ocr_button = tk.Button(window, text="Select Image", command=perform_ocr)
ocr_button.pack(pady=20)
ocr_button.configure(highlightthickness=1, highlightbackground="black")


text_box = tk.Text(window, height=10, width=100)
text_box.pack(pady=10)
text_box.configure(highlightthickness=0.5, highlightbackground="black")

#space
space_label = tk.Label(window, text="", height=1)
space_label.pack()

text_box2 = tk.Text(window, height=20, width=100)
text_box2.pack(pady=10)
text_box2.configure(highlightthickness=0.5, highlightbackground="black")


window.mainloop()
