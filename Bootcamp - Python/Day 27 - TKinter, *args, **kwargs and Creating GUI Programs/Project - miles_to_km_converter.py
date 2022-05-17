import tkinter as tk

def convert():
    inmiles = int(miles.get())
    text_value.config(text=f'{round(inmiles*1.609)}')

# 2x2 ('3x3') | Window
window = tk.Tk()
window.title("Miles/Km Converter")
window.config(padx=25, pady=20)

# 0x0 | NONE

# 1x0 | Entry value in miles.
miles = tk.Entry(width=10) # width
miles.grid(column=1, row=0)

# 2x0 | 'Miles'
text_miles = tk.Label(text='Miles')
text_miles.grid(column=2, row=0)

# 0x1 | 'is equal to'
text_equal = tk.Label(text='is equal to')
text_equal.grid(column=0, row=1)

# 1x1 | Show value in Km.
text_value = tk.Label(text='0')
text_value.grid(column=1, row=1)

# 2x1 | 'Km'
text_km = tk.Label(text='Km')
text_km.grid(column=2, row=1)

# 0x2 | NONE

# 1x2 | Button: Calculate
calculate = tk.Button(text='Calculate', command=convert)
calculate.grid(column=1, row=2)

# 2x2 | NONE

window.mainloop() 