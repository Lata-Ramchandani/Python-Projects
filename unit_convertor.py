import tkinter as tk
from tkinter import ttk,messagebox

unit_categories = {
    "Length": {
        "meters": 1.0,
        "kilometers": 0.001,
        "centimeters": 100.0,
        "millimeters": 1000.0,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    },
    "Mass": {
        "grams": 1.0,
        "kilograms": 0.001,
        "milligrams": 1000.0,
        "pounds": 0.00220462,
        "ounces": 0.035274
    },
    "Area": {
        "square meters": 1.0,
        "square kilometers": 0.000001,
        "square miles": 0.0000003861,
        "acres": 0.000247105,
        "hectares": 0.0001
    },
    "Speed": {
        "meters per second": 1.0,
        "kilometers per hour": 3.6,
        "miles per hour": 2.23694,
        "feet per second": 3.28084,
        "knots": 1.94384
    },
    "Pressure": {
        "pascals": 1.0,
        "kilopascals": 0.001,
        "bars": 0.00001,
        "psi": 0.000145038,
        "atmospheres": 0.00000986923
    },
    "Temperature": {
        "celsius": lambda c: (c + 273.15, c * 9/5 + 32),
        "fahrenheit": lambda f: ((f - 32) * 5/9 + 273.15, (f - 32) * 5/9),
        "kelvin": lambda k: (k, (k - 273.15) * 9/5 + 32)
    },
    "Time": {
        "seconds": 1.0,
        "minutes": 1/60.0,
        "hours": 1/3600.0,
        "days": 1/86400.0,
        "weeks": 1/604800.0,
        "years": 1/31536000.0
    }
}

def select_units(*args):
    
    selected_unit = unit_dropdown.get()

    if selected_unit in unit_categories:
        if selected_unit == 'Temperature':
            units = ['celcius','fahrenheit','kelvin']
        else:
            units = list(unit_categories[selected_unit].keys())
        from_dropdown['values'] = units
        to_dropdown['values'] = units
        from_dropdown.set(units[0])
        to_dropdown.set(units[1])

def convert_unit():
    
    try:
        selected_unit  = unit_dropdown.get()
        from_unit = from_dropdown.get()
        to_unit = to_dropdown.get()
        value = float(input_entry.get())

        if selected_unit not in unit_categories:
            raise ValueError("Invalid Selection")
        
        if to_unit == from_unit:
            result = value
        
        if selected_unit == "Temperature":
            
            temp_convert = unit_categories[selected_unit][from_unit]
            if to_unit == "celcius":
                result = temp_convert(value)[1]
            elif to_unit == "farenheit":
                result = temp_convert(value)[1]
            elif to_unit == "kelvin":
                result = temp_convert(value)[0]
        else:
            
            if from_unit not in unit_categories[selected_unit] or to_unit not in unit_categories[selected_unit]:
                raise ValueError("Invalid Selection")
            
            from_factor = unit_categories[selected_unit][from_unit]
            to_factor = unit_categories[selected_unit][to_unit]
            result = value * (to_factor/from_factor)
        
        label_result.config(text=f" {value} {from_unit} = {result:.4f} {to_unit}")

    except ValueError as e:
        messagebox.showerror("Input Error",e)
    
    except Exception as e:
        messagebox.showerror("Error",f"An Unexpected error occured {e}")


root = tk.Tk()
root.title('Unit Convertor')
root.resizable(False,False)
root.geometry('350x400')

label_font = ("Arial",15,"bold")
title1 = ttk.Label(root,text="UNIT CONVERTOR",justify='center',font=label_font)
title1.pack(padx=10,pady=5)

unit_dropdown = ttk.Combobox(root,values=list(unit_categories.keys()),width=30)
unit_dropdown.pack(padx=10,pady=10)
unit_dropdown.set('-------------Select Unit------------')
unit_dropdown.bind('<<ComboboxSelected>>',select_units)

sublabel_font = ("Arial",10,"bold")

input_frame = ttk.Frame(root)
input_frame.pack(pady=20)

input_label= ttk.Label(input_frame,text="Value: ",font=sublabel_font)
input_label.pack()

input_entry = ttk.Entry(input_frame,width=32)
input_entry.pack()

from_frame = ttk.Frame(root)
from_frame.pack()

from_label = tk.Label(from_frame,text="From: ",font=sublabel_font,justify="center")
from_label.pack()

from_dropdown=ttk.Combobox(from_frame,values="",width=30)
from_dropdown.pack()

to_frame = ttk.Frame(root)
to_frame.pack(pady=20)

to_label = ttk.Label(to_frame,text="To: ",font=sublabel_font,justify="center")
to_label.pack()

to_dropdown = ttk.Combobox(to_frame,value="",width=30)
to_dropdown.pack()

convert_btn = ttk.Button(root,text="Convert",width=32,command=convert_unit)
convert_btn.pack(pady=20)

label_result = ttk.Label(root,text="",foreground="blue",font=("Arial",12))
label_result.pack()


root.mainloop()