import tkinter as tk

def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)

# Window
window = tk.Tk()
window.title("GUI 101")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tk.Label(text="I'm a Label.", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text" or my_label.config(text="New Text") useful if need a lot of changes.
my_label.grid(column=0, row=0)

# Button
button1 = tk.Button(text="Click Me!", command=button_clicked)
button1.grid(column=1, row=1)

# Button
button2 = tk.Button(text="Click Me!", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = tk.Entry() # width
input.grid(column=3, row=2)









window.mainloop() 