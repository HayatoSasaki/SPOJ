import tkinter as tk

# Window
window = tk.Tk()
window.title("GUI 101")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I'm a Label.", font=("Arial", 24, "bold"))
my_label.pack() # side="left" "right" "bottom"
# my_label["text"] = "New Text" or my_label.config(text="New Text") useful if need a lot of changes.

# Button
def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)

button = tk.Button(text="Click Me!", command=button_clicked)
button.pack()

# Entry
input = tk.Entry() # width
input.pack()

window.mainloop() 