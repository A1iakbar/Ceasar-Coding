
import tkinter as tk

def sifrele(metn,acar):
    cvb=""
    for i in metn:
        if (i==" "):
            cvb+=i
        else:
            cvb+=chr(ord(i)+acar)
    return cvb

def deSifrele(metn,acar):
    cvb=""
    for i in metn:
        if (i==" "):
            cvb+=i
        else:
            cvb+=chr(ord(i)-acar)
    return cvb


def encrtpy_button():
    n_metn_e.delete(0,tk.END)
    metn=metn_e.get()
    acar=int(acar_e.get())
    n_metn_e.insert(0,sifrele(metn,acar))

def resolve_button():
    metn_e.delete(0,tk.END)
    metn=n_metn_e.get()
    acar=int(acar_e.get())
    metn_e.insert(0,deSifrele(metn,acar))


panel=tk.Tk()
panel.title('Ceasar Coding')
panel.geometry('755x250')
panel.configure(background = "grey70")
panel.resizable(width = False, height = False)



metn_l=tk.Label(panel,text="Solved Text: ", fg="white", bg="blue", width = 20, height = 3)
metn_l.grid(row=0, column=0, padx = 5, pady =5)

metn_e=tk.Entry(panel,bg="deepskyblue", width = 10, font=('Georgia 14'))
metn_e.grid(row=0,column=1,ipadx = 10, ipady = 10)

acar_l=tk.Label(panel,text="    Value of Ceasar :   ", fg="black",bg="yellow", width = 20, height = 3)
acar_l.grid(row=1,column=1)

acar_e=tk.Entry(panel,bg="khaki1", width = 10, font=('Georgia 14'))
acar_e.grid(row=1,column=2, padx = 5, ipadx = 10, ipady = 10)

ox=tk.Label(panel,text="<------------------>", font=('Georgia 14'), bg="white" , fg="black")
ox.grid(row=0,column=2)

n_metn_l=tk.Label(panel,text="Encrypted text: ",fg="white",bg="red", width = 20, height = 3)
n_metn_l.grid(row=0,column=3)

n_metn_e=tk.Entry(panel,bg="pink", width = 10, font=('Georgia 14'))
n_metn_e.grid(row=0,column=4, padx = 5, ipadx = 10, ipady = 10)

button_e=tk.Button(panel, text = "Encrypt", command = encrtpy_button,width = 6, height = 2, padx = 30, bg = "green2", fg = "black")
button_e.grid(row = 3, column = 2)

button_r=tk.Button(panel,text="Resolve", command = resolve_button,width = 6, height = 2,  padx=30, bg = "orange", fg = "black")
button_r.grid(row=4,column=2)

button_quit=tk.Button(panel,text="Quit Program",width = 6, height = 2, padx= 30,bg = "black", fg = "white", command=panel.destroy)
button_quit.grid(row=6,column=4)


panel.mainloop()
