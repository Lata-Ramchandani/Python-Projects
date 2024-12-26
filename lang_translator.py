import tkinter as tk
from tkinter import ttk 
from languages import languages
from deep_translator import GoogleTranslator

def translate_text():
    
    src_text = input_text_box.get("1.0",tk.END).strip()

    src_lang_name = src_lang_dropdown.get()
    dest_lang_name = dest_lang_dropdown.get()

    src_lang_code = languages.get(src_lang_name,'en')
    dest_lang_code = languages.get(dest_lang_name,'hi')

    if src_text and src_lang_code and dest_lang_code :

        try:
            translated_text = GoogleTranslator(source=src_lang_code,target=dest_lang_code).translate(src_text)
            output_text_box.delete("1.0",tk.END)
            output_text_box.insert(tk.END,translated_text)
        
        except Exception as error :
            output_text_box.delete("1.0",tk.END)
            output_text_box.insert(tk.END,f"Error: {str(error)}")

    

root = tk.Tk()
root.resizable(0,0)
root.title('Translator')
root.geometry('710x300')

input_text_label = ttk.Label(root, text="Input Text: ")
input_text_label.grid(row=0,column=0,padx=10,pady=5,sticky="W")

input_text_box = tk.Text(root,height=10,width=40)
input_text_box.grid(row=1,column=0,columnspan=2,padx=10,pady=5)

output_text_label = ttk.Label(root,text="Translated Text: ")
output_text_label.grid(row=0,column=2,padx=10,pady=5,sticky="W")

output_text_box = tk.Text(root,height=10,width=40)
output_text_box.grid(row=1,column=2,columnspan=2,padx=10,pady=5)

languages_option  = list(languages.keys())

src_lang_label = ttk.Label(root,text="Source Language: ")
src_lang_label.grid(row=2,column=0,padx=10,pady=5,sticky="W")

src_lang_dropdown=ttk.Combobox(root,value=languages_option,width=30)
src_lang_dropdown.grid(row=2,column=1,padx=10,pady=5)
src_lang_dropdown.set('English')

dest_lang_label=ttk.Label(root,text="Destinatation Language: ")
dest_lang_label.grid(row=2,column = 2, padx=10,pady=5,sticky="W")

dest_lang_dropdown=ttk.Combobox(root,value=languages_option,width=30)
dest_lang_dropdown.grid(row=2,column=3,padx=10,pady=5)
dest_lang_dropdown.set('Hindi')

btn_translator = ttk.Button(root,text="Translate",command=translate_text)
btn_translator.grid(row=3,column=0,columnspan=4,pady=10)


root.mainloop()