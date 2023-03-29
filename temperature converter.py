# simple converter, using a tkinter interface


import tkinter as tk
from tkinter import NORMAL, DISABLED
from tkinter import messagebox


def has_whitespace():
    if any(char.isspace() for char in temp_celsius.get()) or any(char.isspace() for char in temp_fahrenheit.get()) or any(char.isspace() for char in temp_kelvin.get()):
        messagebox.showerror("Error", "input is not valid")
    else:
        input_check()

def input_check():
    if temp_celsius.get().isalpha() or temp_fahrenheit.get().isalpha() or temp_kelvin.get().isalpha():
        messagebox.showerror("Error", "input is not valid")
    else:
        if temp_celsius.get() == "":
            if temp_fahrenheit.get() == "":
                if temp_kelvin.get() == "":
                    messagebox.showerror("Error", "input is not valid")
                else:
                    convert_temperature_kelvin()
            else:
                convert_temperature_fahrenheit()
        else:
            convert_temperature_celsius()


def convert_temperature_celsius():
    celsius = temp_celsius.get()
    temp_fahrenheit.delete(0, "end")
    temp_kelvin.delete(0, "end")
    while True:
        if celsius.isdigit():
            celsius = int(celsius)
            fahrenheit = celsius * 1.80 + 32.00
            kelvin = celsius + 273.15
            temp_fahrenheit.insert(0, fahrenheit)
            temp_kelvin.insert(0, kelvin)
            break
        else:
            celsius = float(celsius.replace(",","."))
            fahrenheit = celsius * 1.80 + 32.00
            kelvin = celsius + 273.15
            temp_fahrenheit.insert(0, fahrenheit)
            temp_kelvin.insert(0, kelvin)
            break

def convert_temperature_fahrenheit():
    fahrenheit = temp_fahrenheit.get()
    temp_celsius.delete(0, "end")
    temp_kelvin.delete(0, "end")
    while True:
        if fahrenheit.isdigit():
            fahrenheit = int(fahrenheit)
            celsius = (fahrenheit - 32.00) * 5/9
            kelvin = (fahrenheit - 32.00) * 5/9 + 273.15
            temp_celsius.insert(0, celsius)
            temp_kelvin.insert(0, kelvin)
            break
        else:
            fahrenheit = float(fahrenheit.replace(",","."))
            celsius = (fahrenheit - 32.00) * 5/9
            kelvin = (fahrenheit - 32.00) * 5/9 + 273.15
            temp_celsius.insert(0, celsius)
            temp_kelvin.insert(0, kelvin)
            break

def convert_temperature_kelvin():
    kelvin = temp_kelvin.get()
    temp_celsius.delete(0, "end")
    temp_fahrenheit.delete(0, "end")
    while True:
        if kelvin.isdigit():
            kelvin = int(kelvin)
            celsius = kelvin - 273.15
            fahrenheit = 1.8 * (kelvin - 273.15) + 32
            temp_celsius.insert(0, celsius)
            temp_fahrenheit.insert(0, fahrenheit)
            break
        else:
            kelvin = float(kelvin.replace(",","."))
            celsius = fahrenheit * 5/9 - 32.00
            fahrenheit = 1.8 * (kelvin - 273.15) + 32
            temp_celsius.insert(0, celsius)
            temp_fahrenheit.insert(0, fahrenheit)
            break

def clear_text():
    temp_celsius.delete(0, "end")
    temp_fahrenheit.delete(0, "end")
    temp_kelvin.delete(0, "end")

def switch_button_state():
    if (btn1['state'] == tk.NORMAL):
        btn1['state'] = tk.DISABLED
    else:
        btn1['state'] = tk.NORMAL


master = tk.Tk()

master.title("temperature converter")
master.maxsize(400, 100)
master.eval("tk::PlaceWindow . center")

tk.Label(master, text="Type the desired temperature in one of the fields").grid(row=0, column=0, columnspan="3")
tk.Label(master, text="Celsius").grid(row=1, column=0)
tk.Label(master, text="Fahrenheit").grid(row=1, column=1)
tk.Label(master, text="Kelvin").grid(row=1, column=2)

frame = tk.Frame(master)
btn1 = tk.Button(frame, text="Convert", command=lambda:[has_whitespace(), switch_button_state()])
btn2 = tk.Button(frame, text="Clear", command=lambda:[clear_text(), switch_button_state()])

temp_celsius = tk.Entry(master) 
temp_fahrenheit = tk.Entry(master)
temp_kelvin = tk.Entry(master)

frame.grid(row=3, column=1)
btn1.grid(row=0, column=0, padx=5, pady=5)
btn2.grid(row=0, column=1)

temp_celsius.grid(row=2, column=0, padx=5)
temp_fahrenheit.grid(row=2, column=1, padx=5)
temp_kelvin.grid(row=2, column=2, padx=5)

master.mainloop()
