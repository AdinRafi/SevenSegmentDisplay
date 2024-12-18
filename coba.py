import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

def tampilkan_angka():
    tangani_input()
    
#UI INPUT
ctk.set_appearance_mode("light")

app = ctk.CTk()

app.title("Seven Segment Display")
app.geometry("325x370")

input_frame = ctk.CTkFrame(master=app, width=200, height=50, corner_radius=10, fg_color="white")
input_frame.pack(pady=10, padx=10)

label_W = ctk.CTkLabel(master=input_frame, text="W", width=10, text_color="black")
label_W.grid(row=0, column=0, padx=(10,2), pady=10)

entry_W = ctk.CTkEntry(master=input_frame, width=10, height=40, corner_radius=10, fg_color="white", text_color="black")
entry_W.grid(row=0, column=1, padx=(0,5), pady=10)

label_X = ctk.CTkLabel(master=input_frame, text="X", width=10, text_color="black")
label_X.grid(row=0, column=2, padx=(5,2), pady=10, sticky="e")

entry_X = ctk.CTkEntry(master=input_frame, width=10, height=40, corner_radius=10, fg_color="white", text_color="black")
entry_X.grid(row=0, column=3, padx =(0,5), pady=10)

label_Y = ctk.CTkLabel(master=input_frame, text="Y", width=10, text_color="black")
label_Y.grid(row=0, column=4, padx=(5,2), pady=10)

entry_Y = ctk.CTkEntry(master=input_frame, width=10, height=40, corner_radius=10, fg_color="white", text_color="black")
entry_Y.grid(row=0, column=5, padx=(0,5), pady=10)

label_Z = ctk.CTkLabel(master=input_frame, text="Z", width=10, text_color="black")
label_Z.grid(row=0, column=6, padx=(5,2), pady=10, sticky="e")

entry_Z = ctk.CTkEntry(master=input_frame, width=10, height=40, corner_radius=10, fg_color="white", text_color="black")
entry_Z.grid(row=0, column=7, padx =(0,5), pady=10)

button = ctk.CTkButton(master=input_frame,text="Tampilkan",width=10, height=40, fg_color="red", text_color="black", hover_color="dark red", command=tampilkan_angka)
button.grid(row=0, column=8, padx=(0,10), pady=10)

#UI INPUT BIND
entry_W.bind("<KeyRelease>", lambda event: input_ada(event, entry_X, None))
entry_X.bind("<KeyRelease>", lambda event: input_ada(event, entry_Y, entry_W))
entry_Y.bind("<KeyRelease>", lambda event: input_ada(event, entry_Z, entry_X))
entry_Z.bind("<KeyRelease>", lambda event: input_ada(event, None, entry_Y))

#MENGGABUNGKAN ENTRY
def input_ada(event, entry_selanjutnya, entry_sebelumnya):
    global jumlah_backspace
    input_masuk = event.widget
    nilai_input = input_masuk.get().strip() 

    if len(nilai_input) > 1:
        input_kedua = nilai_input[1]
        input_masuk.delete(0, ctk.END)
        input_masuk.insert(0, input_kedua)

    if nilai_input:
        if entry_selanjutnya is not None:
            entry_selanjutnya.focus()
            jumlah_backspace = 0

    elif jumlah_backspace > 0:
        if entry_sebelumnya is not None:
            entry_sebelumnya.focus()
            jumlah_backspace = 0

    elif nilai_input == "" and event.keysym == "BackSpace":
        jumlah_backspace += 1
    
    else:
        jumlah_backspace = 0

#UI DISPLAY
display_frame = ctk.CTkFrame(master=app, width=300, height=400, corner_radius=10, fg_color="white")
display_frame.pack(padx=10, pady=10)

segment_A = ctk.CTkLabel(master=display_frame, width=60, height=15, fg_color="dark grey", text=(), corner_radius=7)
segment_A.grid(row=0, column=1)

segment_B = ctk.CTkLabel(master=display_frame, width=15, height=60, fg_color="dark grey", text=(), corner_radius=7)
segment_B.grid(row=1, column=2)

segment_C = ctk.CTkLabel(master=display_frame, width=15, height=60, fg_color="dark grey", text=(), corner_radius=7)
segment_C.grid(row=3, column=2)

segment_D = ctk.CTkLabel(master=display_frame, width=60, height=15, fg_color="dark grey", text=(), corner_radius=7)
segment_D.grid(row=4, column=1)

segment_E = ctk.CTkLabel(master=display_frame, width=15, height=60, fg_color="dark grey", text=(), corner_radius=7)
segment_E.grid(row=3, column=0)

segment_F = ctk.CTkLabel(master=display_frame, width=15, height=60, fg_color="dark grey", text=(), corner_radius=7)
segment_F.grid(row=1, column=0)

segment_G = ctk.CTkLabel(master=display_frame, width=60, height=15, fg_color="dark grey", text=(), corner_radius=7)
segment_G.grid(row=2, column=1)

#UI TABLE
table_frame = ctk.CTkFrame(master=app, width=300, height=400, corner_radius=10, fg_color="white")
table_frame.pack(padx=10, pady=10)

label_A = ctk.CTkLabel(master=table_frame, text="A", width=20, height=10, text_color="black")
label_A.grid(row=0, column=0, padx=(10,0), pady=10)

label_B = ctk.CTkLabel(master=table_frame, text="B", width=20, height=10, text_color="black")
label_B.grid(row=0, column=1, padx=(10,0), pady=10)

label_C = ctk.CTkLabel(master=table_frame, text="C", width=20, height=10, text_color="black")
label_C.grid(row=0, column=2, padx=(10,0), pady=10)

label_D = ctk.CTkLabel(master=table_frame, text="D", width=20, height=10, text_color="black")
label_D.grid(row=0, column=3, padx=(10,0), pady=10)

label_E = ctk.CTkLabel(master=table_frame, text="E", width=20, height=10, text_color="black")
label_E.grid(row=0, column=4, padx=(10,0), pady=10)

label_F = ctk.CTkLabel(master=table_frame, text="F", width=20, height=10, text_color="black")
label_F.grid(row=0, column=5, padx=(10,0), pady=10)

label_G = ctk.CTkLabel(master=table_frame, text="G", width=20, height=10, text_color="black")
label_G.grid(row=0, column=6, padx=(10,10), pady=10)

table_label = []
for i in range(7):
    label = ctk.CTkLabel(master=table_frame, text=0, width=20, height=10, text_color="black")
    label.grid(row=1, column=i, padx=(10,0), pady=(0,10))
    if i == 6:
        label.grid(row=1, column=i, padx=(10,10), pady=(0,10))
    table_label.append(label)

#BUTTON INPUT BIND
app.bind("<Return>", lambda event: tampilkan_angka())

def tangani_input():
    input_W = entry_W.get().strip()
    input_X = entry_X.get().strip()
    input_Y = entry_Y.get().strip()
    input_Z = entry_Z.get().strip()

    inputs = [input_W, input_X, input_Y, input_Z]

    names = ["W", "X", "Y", "Z"]

    input_kosong = [name for name, value in zip(names, inputs) if not value]
    input_salah = any(bit not in ("0", "1", "") for bit in inputs)

    error_messages = []

    if len(input_kosong) == 1:
        error_messages.append(f"Input pada {(input_kosong[0])} kosong")
    elif len(input_kosong) == 2:
       error_messages.append(f"Input pada {input_kosong[0]} dan {input_kosong[1]} kosong")
    elif len(input_kosong) > 2 and len(input_kosong) < 5:
        error_messages.append(f"Input pada {', '.join(input_kosong[:-1])}, dan {input_kosong[-1]} kosong")
 
    if input_salah:
        error_messages.append("Input hanya bisa 0 atau 1")

    input_W = int(input_W) if input_W in ("0", "1") else 0
    input_X = int(input_X) if input_X in ("0", "1") else 0
    input_Y = int(input_Y) if input_Y in ("0", "1") else 0
    input_Z = int(input_Z) if input_Z in ("0", "1") else 0

    angka = input_W * 8 + input_X * 4 + input_Y * 2 + input_Z

    if angka < 0 or angka > 9:
        error_messages.append("Input harus angka 0-9")

    if error_messages and len(input_kosong) == 1:
        messagebox.showerror("Error", " dan ".join(error_messages))
        angka = 10
    elif error_messages and (len(input_kosong) == 2 or len(input_kosong) == 3):
        messagebox.showerror("Error", " serta ".join(error_messages))
        angka = 10
    elif error_messages:
        messagebox.showerror("Error", " dan ".join(error_messages))
        angka = 10

    segmen = {
            0: [1, 1, 1, 1, 1, 1, 0],
            1: [0, 1, 1, 0, 0, 0, 0],
            2: [1, 1, 0, 1, 1, 0, 1],
            3: [1, 1, 1, 1, 0, 0, 1],
            4: [0, 1, 1, 0, 0, 1, 1],
            5: [1, 0, 1, 1, 0, 1, 1],
            6: [1, 0, 1, 1, 1, 1, 1],
            7: [1, 1, 1, 0, 0, 0, 0],
            8: [1, 1, 1, 1, 1, 1, 1],
            9: [1, 1, 1, 1, 0, 1, 1],
            10:[0, 0, 0, 0, 0, 0, 0]
        }
    
    segmen_angka = segmen[angka]
    
    #UBAH UI SEGMENT
    segment_A.configure(fg_color="red" if segmen_angka[0] else "dark gray")
    segment_B.configure(fg_color="red" if segmen_angka[1] else "dark gray")
    segment_C.configure(fg_color="red" if segmen_angka[2] else "dark gray")
    segment_D.configure(fg_color="red" if segmen_angka[3] else "dark gray")
    segment_E.configure(fg_color="red" if segmen_angka[4] else "dark gray")
    segment_F.configure(fg_color="red" if segmen_angka[5] else "dark gray")
    segment_G.configure(fg_color="red" if segmen_angka[6] else "dark gray")

    #UBAH UI TABLE
    for i, value in enumerate(segmen_angka):
        table_label[i].configure(text=value)

#JALANKAN APP
app.mainloop()
