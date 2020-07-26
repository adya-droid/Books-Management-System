from tkinter import *
root=Tk()
root.title("Simple Inventory System")
root.geometry('900x500')
Label(root, text="Inventory System", font=("Harlow solid italic", 20), width=28, fg='black', bg='#870006').place(x=300,
                                                                                                              y=60)
Label(root, text="Name: Adya Singh", font=("Harlow solid italic", 15)).place(x=300, y=120)
Label(root, text="Enroll No: XYZ    ", font=("New Times Roman", 15)).place(x=300, y=150)
Label(root, text="Batch: A1                  ", font=("Harlow solid italic", 15)).place(x=300, y=180)
Label(root, text="About : ", font=("Harlow solid italic", 10), fg='white', bg='#870006').place(x=300, y=230)
Label(root, text="This project focus on the inventory system", font=("Harlow solid italic", 15)).place(x=300, y=260)
Label(root, text="of the Library books management which uses ", font=("Harlow solid italic", 15)).place(x=300, y=290)
Label(root, text="python tkinter module for GUI,PIL for image ", font=("Harlow solid italic", 15)).place(x=300, y=320)
Label(root, text="sqlite3 for database,smtplib for mail, ", font=("Harlow solid italic", 15)).place(x=300, y=350)
Label(root, text="pyttsx3 for text to speech ", font=("Harlow solid italic", 15)).place(x=300, y=380)


root.mainloop()