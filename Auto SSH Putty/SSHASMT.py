from tkinter import *
from tkinter import ttk
from subprocess import Popen
import os
import sys
import base64

master = Tk()
master.geometry("250x130")
password = ""
variable = StringVar(master)

variable.set("Select a server") # default value

with open(os.path.join(sys.path[0], "servers.txt"), "r") as f:  # opens name of your file
    array = [line.strip() for line in f]  # puts values of file in array. each line = one part of array
f.close()
array.sort()

with open(os.path.join(sys.path[0], "password.txt"), "r") as f:
    password = f.readline()
f.close()

base64_bytes = password.encode('utf-8')
message_bytes = base64.b64decode(base64_bytes)
password = message_bytes.decode('utf-8')

w = ttk.Combobox(master, textvariable=variable, values=array)
w.pack()

def ok(event):
    server = w.get()
    Popen(f"powershell putty.exe <USERNAME>@{server} -pw {password}")

master.bind('<Return>', ok)

button = Button(master, text="OK")
button.bind('<Button-1>', ok)
button.pack(pady=20)

exit_button = Button(master, text="Exit", command=master.destroy)
exit_button.pack(pady=5)

master.mainloop()