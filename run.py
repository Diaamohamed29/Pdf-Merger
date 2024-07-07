from PIL import Image
import customtkinter as ct 
import os
from tkinter import BOTTOM
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox
import threading
from PyPDF2 import PdfMerger
from PIL import Image, ImageTk



def select_files():
    global files
    files = askopenfilenames(title='Select PDF Files', filetypes=[("PDF files", "*.pdf")])
    print(files)

def merge_pdfs():
    if not files:
        messagebox.showerror("Error", "No PDF files selected")
        return
    
    merger = PdfMerger()
    output_file = os.path.join(os.path.dirname(files[0]), 'merged.pdf')
    
    for file in files:
        merger.append(file)
        
    merger.write(output_file)
    merger.close()
    print('Done Merging')
    messagebox.showinfo("Success", "PDFs merged successfully!")

def start_thread(target):
    threading.Thread(target=target).start()


ct.set_appearance_mode("light")
app = ct.CTk()
app.geometry("400x580")
app.resizable(False, False)
app.configure(fg_color='white')
app.title('PDF Merge')
app.iconbitmap('assets//pdf.ico')
frame_1 = ct.CTkFrame(master=app, fg_color='white')
frame_1.pack(pady=20, padx=60, fill='both', expand=True)


IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100
IMAGE_PATH = 'assets//pdf.png'




your_image = ct.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)), size=(IMAGE_WIDTH , IMAGE_HEIGHT))

label = ct.CTkLabel(frame_1, image=your_image, text='')
label.pack()

header_title_lbl = ct.CTkLabel(frame_1, text='PDF Merger', font=('calbri', 14, 'bold'))
header_title_lbl.pack(pady=10, padx=20)

select_btn = ct.CTkButton(frame_1, text='Select Files', width=160, command=lambda: start_thread(select_files))
select_btn.pack(pady=30, padx=20)

merge_btn = ct.CTkButton(frame_1, text='Merge', width=160, command=lambda: start_thread(merge_pdfs))
merge_btn.pack(pady=30, padx=20)

authlabel = ct.CTkLabel(frame_1, text='Made By Diaa Mohamed', font=('calbri', 12, 'bold'))
authlabel.pack(side=BOTTOM)

app.mainloop()
