from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
from tkinter import filedialog

def openFile():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    label=Label(root,text=root.filename).pack()
    x=root.filename
    return x

root=Tk()
root.geometry('300x300')
root.title("Pupil extraction")
Button(root,text="Select Image",command=openFile).pack()
root.mainloop()
r'L:\PUPIL-Detection-using-OpenCV\eye3.jpg'
