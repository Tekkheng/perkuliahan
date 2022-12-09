import tkinter as tk
from tkinter import ttk

def klik_tes():
    # tulip = ttk.Button(frm, text="9.Tulip")
    # tulip.pack(padx=10,pady=5,fill="x",expand=True)
    print(nama.get())

# test = tk.Label(text="hello")
# test.pack()
# # window = tk.Tk()


# window = tk.Tk()
# window.mainloop()

# root = tk.Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

# window sebagai webny
window = tk.Tk()
# ganti background website :
window.configure(bg="DarkSlateGrey")
# mengatur ukuran default websiteny:
window.geometry("450x500")
# membuat website tidak bisa di resize dengan mouse:
window.resizable(False,False) #=> (x,y)
# membuat judul pada website : 
window.title("Tugas PBO Garden")
# membuat frame di website mirip box:
frm = ttk.Frame(window, padding=10)
# penempatan Grid,Pack,Place
#label
nama_label = ttk.Label(frm, text="Nama : ")
nama_label.pack(padx=10,fill="x",expand=True)

# input ke var nama
nama = tk.StringVar()
nama_entry = ttk.Entry(frm, textvariable = nama)
nama_entry.pack(padx=10,pady=5,fill="x",expand=True)

# button
anggrek = ttk.Button(frm, text="1.Anggrek")
anggrek.pack(padx=10,pady=5,fill="x",expand=True)

mawar = ttk.Button(frm, text="2.Mawar")
mawar.pack(padx=10,pady=5,fill="x",expand=True)

melati = ttk.Button(frm, text="3.Melati")
melati.pack(padx=10,pady=5,fill="x",expand=True)

exit = ttk.Button(frm, text="4.Exit",command=window.destroy)
exit.pack(padx=10,pady=5,fill="x",expand=True)

tes = ttk.Button(frm, text="?.Panggil Nama",command = klik_tes)
tes.pack(padx=10,pady=5,fill="x",expand=True)
# frm.grid()
# ttk.Label(frm, text="Menu").grid(column=0, row=0)
# ttk.Button(frm, text="1.Anggrek").grid(column=0, row=0)
# ttk.Button(frm, text="2.Mawar").grid(column=0, row=0)
# ttk.Button(frm, text="3.Melati").grid(column=0, row=0)
# ttk.Button(frm, text="4.Exit",command=window.destroy).grid(column=0, row=0)

frm.pack(padx=80,pady=0,fill="x",expand=True)

# menjalankan website : 
window.mainloop() 