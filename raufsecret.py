import pyAesCrypt
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
root.title('SecretX By Rauf')


def buka_file():
    global letak
    fileName = askopenfilename(parent=root, title='Pilih File')
    file = Label(root, text=fileName)
    file.pack()
    letak = file.cget("text")
    
    
mylabel3=Label(root, text="Pilih file yang akan dilakukan encrypt/decrypt")
mylabel3.pack()
browse = Button(root, text="Pilih File", command=buka_file)
browse.pack()



mylabel2=Label(root, text="Nama File")
mylabel2.pack()

f = Entry(root, width=30)
f.pack()

mylabel=Label(root, text="Password")
mylabel.pack()

e = Entry(root, width=30)
e.pack()

mylabel4=Label(root, text="Catatan : Pastikan anda mengingat format file yang di encrypt/decrypt atau anda dapat menyertakan format file pada nama file")
mylabel4.pack()

def myDecrypt():

    bufferSize = 256 * 1024
    password=e.get()
    
    pyAesCrypt.decryptFile(letak, f.get(), password, bufferSize)

def myEncrypt():
    bufferSize = 256 * 1024
    password=e.get()
    pyAesCrypt.encryptFile(letak, f.get(), password, bufferSize)
    
myButton = Button(root, text="Encrypt", width=30, command=myEncrypt)
myButton.pack()



myButton2 = Button(root, text="Decrypt", width=30, command=myDecrypt)
myButton2.pack()
    

root.mainloop()

