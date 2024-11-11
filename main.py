from customtkinter import *
from tkinter import messagebox,filedialog
from PIL import Image
from stegano import lsb

class Main(CTk):
    def __init__(self):
        super().__init__()
        self.title("Image Steganography")
        self.geometry("700x440")
        self.resizable(False,False)
        self.configure(fg_color="gray")
        CTkLabel(self,text="Hide Text In Image",font=CTkFont(family="sans-serif",size=40,weight="bold",slant="italic",underline=True),text_color="white").pack(pady=10)
        ImageFrame = CTkFrame(self,height=300,width=300,corner_radius=10,border_width=3,border_color="black",fg_color='white')
        self.img = CTkLabel(ImageFrame,text="",image=CTkImage(dark_image=Image.open("sample.png"),light_image=Image.open("sample.png"),size=(300,300)))
        self.img.place(x=0,y=0)
        ImageFrame.place(x=10,y=70)
        TextFrame = CTkTextbox(self,height=300,width=370,corner_radius=10,fg_color='white',text_color='black',font=CTkFont(family="sans-serif",size=15,weight="bold"))
        TextFrame.place(x=320,y=70)
        CTkButton(self,text="Select Image",font=CTkFont(family="sans-serif",size=15,weight="bold"),command=self.SelectImage).place(x=20,y=390)
        CTkButton(self,text="Hide Text",font=CTkFont(family="sans-serif",size=15,weight="bold"),command=self.HideText).place(x=190,y=390)
        CTkButton(self,text="Save Image",font=CTkFont(family="sans-serif",size=15,weight="bold"),command=self.SaveImage).place(x=360,y=390)
        CTkButton(self,text="Extract Text",font=CTkFont(family="sans-serif",size=15,weight="bold"),command=self.ExtractText).place(x=530,y=390)
        self.mainloop()
    
    def SelectImage(self):
        print("select image")
    
    def HideText(self):
        print("hide text")
    
    def SaveImage(self):
        print("save image")
    
    def ExtractText(self):
        print("extract text")


if __name__ == "__main__":
    Main()