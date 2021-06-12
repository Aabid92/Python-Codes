import pygame
from tkinter import *

root = Tk()
root.title("Lets Play!")
root.geometry("600x400")


pygame.mixer.init()

def play():
    pygame.mixer.music.load('audio\music1.mp3')
    pygame.mixer.music.play(loops = 2)

def stop():
    pygame.mixer.music.stop()

def play2():
    pygame.mixer.music.load('audio\music2.mp3')
    pygame.mixer.music.play(loops=2)

mybutton = Button(root, text="Play Me!",font=("Helvetica", 30),command=play2)
mybutton.pack(padx=20)


mybutton = Button(root, text="Play Me!",font=("Helvetica", 30),command=play)
mybutton.pack(pady=20)

stop_butto = Button(root,text="Stop!",font=("Helvetica",15),command=stop)
stop_butto.pack(pady=22)

exit_button = Button(root,text="Exit", font=("Helvetica",15),command=exit)
exit_button.pack(pady=10)

mybutton = Button(root,text="Side Button",command=exit)
mybutton.pack(side=BOTTOM)

root.mainloop()