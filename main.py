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
        ImageFrame = CTkFrame(self,height=300,width=300,corner_radius=10,border_width=5,border_color="black",fg_color='white')
        self.img = CTkLabel(ImageFrame,text="",image=CTkImage(dark_image=Image.open("sample.jpeg"),light_image=Image.open("sample.jpeg"),size=(290,290)))
        self.img.place(x=5,y=5)
        ImageFrame.place(x=10,y=70)
        self.TextFrame = CTkTextbox(self,height=300,width=370,corner_radius=10,fg_color='white',text_color='black',font=CTkFont(family="sans-serif",size=15,weight="bold"))
        self.TextFrame.place(x=320,y=70)
        CTkButton(self,text="Select Image",font=CTkFont(family="sans-serif",size=15,weight="bold"),command=self.SelectImage).place(x=20,y=390)
        CTkButton(self,text="Hide Text",font=CTkFont(family="sans-serif",size=15,weight="bold"),command=self.HideText).place(x=190,y=390)
        CTkButton(self,text="Save Image",font=CTkFont(family="sans-serif",size=15,weight="bold"),command=self.SaveImage).place(x=360,y=390)
        CTkButton(self,text="Extract Text",font=CTkFont(family="sans-serif",size=15,weight="bold"),command=self.ExtractText).place(x=530,y=390)
        self.filepath,self.flag = None,False
        self.mainloop()
    
    def SelectImage(self):
        self.filepath = filedialog.askopenfilename(title="Select Image",filetypes=(("jpg files","*.jpg"),("jpeg files","*.jpeg"),("png files","*.png"),("all files","*.*")))
        if self.filepath:
            self.img.configure(image=CTkImage(dark_image=Image.open(self.filepath),light_image=Image.open(self.filepath),size=(290,290)))
            self.flag = False
    
    def HideText(self):
        if self.TextFrame.get(1.0,END).replace(" ","").replace("\n","") != "" and self.filepath != None:
            try:
                self.secret = lsb.hide(image=self.filepath,message=self.TextFrame.get(1.0,END))
                messagebox.showinfo("Success","Text Hidden Successfully")
                self.flag = True
            except Exception as e:messagebox.showerror("Error",str(e))
        else:messagebox.showwarning("Warning","Select Image And Enter Text To Hide")
    
    def SaveImage(self):
        if self.flag:
            filepath = filedialog.asksaveasfilename(title="Save Image",defaultextension=".png",initialfile="secret")
            if filepath:
                self.secret.save(filepath)
                messagebox.showinfo("Success","Image Saved Successfully")
        else:messagebox.showwarning("Warning","Select Image And Enter Text To Hide")
    
    def ExtractText(self):
        if self.filepath != None:
            try:
                text = lsb.reveal(Image.open(self.filepath))
                self.TextFrame.delete(1.0,END)
                self.TextFrame.insert(END,text)
                messagebox.showinfo("Success","Text Extracted Successfully")
                self.flag = False
            except IndexError:messagebox.showwarning("Warning","No Text To Extract")
            except Exception as e:messagebox.showerror("Error",str(e))
        else:messagebox.showwarning("Warning","Select Image To Extract Text")

if __name__ == "__main__":
    Main()