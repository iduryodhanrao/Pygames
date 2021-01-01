import tkinter as tk
import feedparser
from tkinter import messagebox
def news(title,summary):
    window = tk.Tk()
    window.title(title)
    window.geometry('450x200')
    label1 = tk.Label(window, text=title, font=("Arial Bold",10), fg="white" , bg="blue", wraplength=450, justify="left")
    label2 = tk.Label(window, text=summary, font=("Arial Bold", 10), wraplength=450, justify="left")
    button1 = tk.Button(window,text="Not Interested?",command=clicked) #button to close the notifications

    #label1.configure(text=summary)
    #messagebox.showinfo(title,summary)  #message box
    label1.grid(column=0,row=0)
    label2.grid(column=0,row=1)
    button1.place(relx=0.5, rely=0.8, anchor="center")
    window.after(10000, lambda: window.destroy()) #closes the window after 10 seconds
    window.mainloop()

def clicked():
    exit(1)

f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
i=0
for newsitem in f['items']:
    #print(newsitem['title'])
    #print(newsitem['summary'])
    news(newsitem['title'],newsitem['summary'])
    i = i +1
    print("i=",i)
