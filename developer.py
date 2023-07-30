from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        title_lbl=Label(self.root, text="DEVELOPER",font=("times new roman", 25, "bold"), bg="red",fg="white")
        title_lbl.place(x=0, y=0,width=1330,height=40)

        img_top=Image.open(r"college_images/dev.jpg")
        img_top=img_top.resize( (1330, 720), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1330, height=720)

        # frame
        main_frame=Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=750, y=0,width=500,height=560)

        img_top1=Image.open(r"college_images/IMG_20201128_175727_396.jpg")
        img_top1=img_top1.resize( (200, 200), Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)

        # developer info
        dev_label=Label(main_frame, text="HELLO MY NAME IS ABHISHEK",font=("times new roman", 16, "bold"))
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame, text="THIS IS MY CONTACT INFO.",font=("times new roman", 16, "bold"))
        dev_label.place(x=0,y=150)

        img1=Image.open(r"college_images/Screenshot (108).png")
        img1=img1.resize((500, 300), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(main_frame, image=self.photoimg1)
        f_lbl.place(x=0, y=200,width=500,height=300)
        






if __name__ == "__main__":
  root=Tk()
  obj=Developer(root)
  root.mainloop()       