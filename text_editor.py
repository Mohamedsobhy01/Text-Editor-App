import tkinter as tk 
from tkinter import filedialog

def open_file() :
    file_path = filedialog.askopenfilename(
        title="Choose a File",
        filetypes=(("Text File", "*.txt"), ("All Files", "*.*"))
    )
    if not file_path :
        return
    
    txt_edit.delete(1.0, "end")
    with open(file_path, "r") as input_file :
        text = input_file.read()
        txt_edit.insert("end", text)

    window.title(f"Dark Theme Text Editor => {file_path}")

def save_file() :
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=(("Text File", "*.txt"), ("All Files", "*.*"))
    )
    if not file_path :
        return
    
    with open(file_path, "w") as output_file :
        text = txt_edit.get("1.0", "end")
        text = output_file.write(text)

    window.title(f"Dark Theme Text Editor => {file_path}")

window = tk.Tk()
window.title("Dark Theme Text Editor")
window.config(bg="#1e1e1e")
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=700)

txt_edit = tk.Text(window, bg="#1e1e1e", fg="white", insertbackground="white")
frame_buttons = tk.Frame(window, relief=tk.RAISED)
btn_open = tk.Button(frame_buttons, text="Open File", command=open_file)
btn_save = tk.Button(frame_buttons, text="Save As", command=save_file)

btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=7)
btn_save.grid(column=0, row=1, sticky="ew", padx=5)

frame_buttons.grid(column=0, row=0, sticky="nw")
txt_edit.grid(column=1, row=0, sticky="nsew")

window.mainloop()

