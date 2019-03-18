from tkinter import *
from PIL import ImageGrab, Image, ImageDraw
from  utils import create_new_img, img2lsit, y2letter
from model import Model
import numpy as np


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 5
        self.setUI()
        self.im = Image.new('RGBA', (330, 250), (255, 255, 255, 255))
        self.drawn = ImageDraw.Draw(self.im)
        

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)
                              
        self.drawn.ellipse((event.x - self.brush_size, event.y - self.brush_size, 
                            event.x + self.brush_size, event.y + self.brush_size), 
                            fill=(0,0,0,255))

    def setUI(self):

        self.parent.title("Draw the letter")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")

        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)
                       
        self.canv.bind("<B1-Motion>", self.draw)

        self.answer_lab = Label(self, text="Answer")
        self.answer_lab.grid(row=0, column=0, padx=6)

        rec_btn = Button(self, text="Recognize", width=10,
                           command=lambda: self.recognize())
        rec_btn.grid(row=0, column=2)        
        
        clear_btn = Button(self, text="clear", width=10,
                           command=lambda: self.clear())
        clear_btn.grid(row=0, column=3)

    
    def clear(self):
        self.canv.delete("all")
        self.drawn.rectangle((0, 0, 330, 250), fill=(255, 255, 255, 255))
    
        
    def recognize(self):   
        self.im.save('img.png')
        
        create_new_img('img.png', '', '', 50)
        X = np.array(img2lsit('img.png'))
        X = np.expand_dims(X, axis=0)
        predict = model.predict(X)
        
        answer = y2letter(predict)
        
        self.answer_lab.config(text=answer)
        
        print('Answer:', answer)
        


model = Model()
model.load()

root = Tk()
root.geometry("330x250")
app = Paint(root)
root.mainloop()



