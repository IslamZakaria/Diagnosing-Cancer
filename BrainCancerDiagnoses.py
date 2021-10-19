from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import keras
import os
import cv2
import numpy as np
from keras.models import load_model
import playsound

def run_model(x):
    if os.path.exists('BrainCancerModel2.h5'):
        img = cv2.imread(x)
        sizeNew = 224, 224
        inputs = []
        resized = cv2.resize(img, sizeNew)
        inputs.append(np.array(resized))
        model = keras.models.load_model('BrainCancerModel2.h5')
        d = keras.optimizers.SGD(lr=0.001)
        preds = model.predict(np.array(inputs))
        y_classes = preds.argmax(axis=-1)

        if y_classes == 0:
            y_classes='Axial Normal'
        elif y_classes == 1:
            y_classes='Coronal Normal'
        elif y_classes == 2:
            y_classes='Sagittal Normal'
        elif y_classes == 3:
            y_classes='Axial Glioma'
        elif y_classes == 4:
            y_classes='Coronal Glioma'
        elif y_classes == 5:
            y_classes = 'Sagittal Glioma'
        elif y_classes == 6:
            y_classes = 'Axial MeninGlioma'
        elif y_classes == 7:
            y_classes = 'Coronal MeninGlioma'
        elif y_classes == 8:
            y_classes = 'Sagittal MeninGlioma'
        elif y_classes == 9:
            y_classes = 'Axial Pituitary'
        elif y_classes == 10:
            y_classes = 'Corona Pituitary'
        elif y_classes == 11:
            y_classes = 'Sagittal Pituitary'

        image_label = Label(root, bg="#FFFFFF", text=y_classes)
        image_label.place(x=90, y=550)
        image_label.config(font=("Courier",30))

res = []
def open_file():
    result =  filedialog.askopenfilenames(initialdir="/", title="select file", filetypes=(("images", ".png"), ("all files", ".")))
    for c in result:
        panel =tk.Label ()
        i =0
        for y in root.pack_slaves():
            if i >= 0:
                y.destroy()
            i+=1

        img = Image.open(c).convert('RGBA')
        background = Image.open("background.jpg").convert('RGBA')
        background.paste(img, (135, 280),img)
        background.save("dynamic.png")
        canvas = Canvas(root, width=1600, height=983)
        helv36 = tkFont.Font(family='Helvetica', size=14, weight='bold')
        button = Button(root, height=5, width=20, text="Choose Image to Predict", command=open_file, font=helv36).place(x=155, y=80)
        image = ImageTk.PhotoImage(Image.open("dynamic.png").convert('RGBA'))
        canvas.create_image(0, 0, anchor=NW, image=image)
        image_label = Label(root, bg="#FFFFFF", text="Image")
        image_label.place(x=200, y=210)
        image_label.config(font=("Courier", 30))

        canvas.pack()
        run_model(c)
        playsound.playsound('MR sound.mp3', True)
        root.mainloop()
root = Tk()

canvas = Canvas(root, width=1600, height=900)
image=ImageTk.PhotoImage(Image.open("background.jpg").convert('RGBA'))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

root.title("Brain Cancer Diagnoses")
root.geometry('900x450')
root.state('zoomed')

style = tk.ttk.Style()
style.configure('my.TButton',font=('bold'), bordercolor="red")

helv36 = tkFont.Font(family='Helvetica', size=14, weight='bold')
button = Button(root, height=5, width=20, text="Choose Image to Predict", command=open_file, font=helv36).place(x=155, y=80)
root.mainloop()