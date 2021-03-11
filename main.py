from tkinter import *
from tkinter import filedialog
import cv2


#Functions
def extractor():
    try:
        vidcap = cv2.VideoCapture(pathIn)
        success, image = vidcap.read()
        count = 0
        while success:
            cv2.imwrite(pathOut + "\\frame%d.jpg" % count, image)  # save frame as JPEG file
            success, image = vidcap.read()
            #print('Read a new frame: ', success)
            count += 1
        Label(master, text="Download Complete", fg="#e31e1e", font=("Calibri", 12)).grid(sticky=N, row=7, pady=15)
    except Exception as e:
        print(e)


def pathinfile():
    global pathIn
    pathIn = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("mp4 Files", "*.mp4"), ("all files", "*.*")))

def pathoutfile():
    global pathOut
    pathOut = filedialog.askdirectory()

#Main Screen
master = Tk()
master.title("Video frame Extractor")

#Labels
Label(master, text="Video frame Extractor", fg="#e31e1e", font=("Calibri", 15)).grid(sticky=N, padx=100, row=0)
notif = Label(master, font=("Calibri", 12))
notif.grid(sticky=N, pady=1, row=4)

#Vars

#Entry

#Button
Button(master, width=30, text="Select a video", font=("Calibri", 12), command=pathinfile).grid(sticky=N, row=2, pady=30)
Button(master, width=30, text="Select a folder", font=("Calibri", 12), command=pathoutfile).grid(sticky=N, row=4, pady=15)
Button(master, width=10, text="Extract", font=("Calibri", 12), command=extractor).grid(sticky=N, row=6, column=0, pady=15)
Button(master, width=10, text="Quit", font=("Calibri", 12), command=master.quit).grid(sticky=N, row=6, column=1, pady=15, padx=10)
master.mainloop()
