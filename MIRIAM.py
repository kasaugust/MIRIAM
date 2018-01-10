from tkinter import *

import os

import mikrofon
import speaker
import sarmata
import subprocess
from pathlib import Path


global count
count = 1


def decide():

    informacja_semantyczna = sarmata.run()

    if informacja_semantyczna == "opis":
        speaker.ask_description()
        mikrofon.record()
        informacja_semantyczna2 = sarmata.run()
        film_path = Path("filmoteka/" + informacja_semantyczna2 + ".txt")
        if film_path.is_file():
            f = open(os.path.relpath(film_path), 'r')
            label2 = Label(root, text=f.read(), bg="White", font="Times 12")
            label2.pack(side=TOP, fill=BOTH)
            f.close()
        else:
            speaker.misunderstand()
            mikrofon.record()
            decide()

    elif informacja_semantyczna == "ogladanie":
        speaker.ask_watch()
        mikrofon.record()
        informacja_semantyczna2 = sarmata.run()
        film_path = Path("filmoteka/" + informacja_semantyczna2 + ".avi")
        print(informacja_semantyczna2 + " MIRIAM ")
        if film_path.is_file():
            subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe", os.path.relpath(film_path)])
        else:
            speaker.misunderstand()
            mikrofon.record()
            decide()

    else:
        speaker.misunderstand()
        mikrofon.record()
        decide()


def if_pressed():
    speaker.say_hello()
    mikrofon.record()
    decide()


speaker.load_answers()
root = Tk()
root.title("Filmoteka")
labelx = Label(root, text="Spis Twoich Filmów:", bg="LightBLUE", font="Times 14 underline")
labely = Label(root,
               text="1.Edward Nożycoręki\n 2.Gnijąca panna młoda\n 3.Iluzjonista\n 4.Mroczne Cienie\n 5.Nietykalni\n 6.Planeta Małp\n 7.Podaj Dalej\n8. Niebo istnieje naprawdę\n9. Piękna i Bestia\n10. Jak zostać królem",
               bg="LightBlue", font="Times 12")

b = Button(root, text=" MIRIAM", command=if_pressed, bg="RED", font="Times 18")
label1 = Label(root, text="Aby uruchomić program wciśnij przycisk MIRIAM", bg="White", font="Times 12")
b.pack(side=TOP)
labelx.pack()
labely.pack()
label1.pack(side=BOTTOM, fill=BOTH)
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=BOTH, padx=5, pady=5)
root.mainloop()
