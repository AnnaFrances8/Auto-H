#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from tkinter import filedialog, messagebox, Tk, Button, Label, Menu, Text
import tkinter as tk
from PIL import Image, ImageTk
import re
import pyautogui
import shutil
import time
import keyboard


#-----------------------------------#FUNCTIONS#--------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------


#--------------INFO FUNCTIONS-------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#Instructions function
def instructions():
    os.chdir(program_directory)
    
    try:
        with open("instructions.txt", "r") as file:
            content = file.read()
            popup = tk.Toplevel(root)  # Create a popup window
            popup.title("How to use")
            popup.iconphoto(False, icono_p, icono_p)
            text_widget = tk.Text(popup, wrap=tk.WORD)
            text_widget.pack()
            text_widget.insert(tk.END, content)
            update_console("How to use manual displayed on screen.")
    except FileNotFoundError:
        popup = tk.Toplevel(root)
        popup.title("How to use")
        text_widget = tk.Text(popup, wrap=tk.WORD)
        text_widget.pack()
        text_widget.insert(tk.END, "File not found")
        

# Attribution function
def attribution():
    os.chdir(program_directory)
    os.system("ICON_ATR.pdf")
    
# License function
def license():
    os.chdir(program_directory)
    os.system("license.pdf")


# Function to clean the console
def clear_console():
    console_text.delete("1.0", tk.END)

#-------------------------------MAIN FUNCTIONS--------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

# Function to update the console with progress or information
def update_console(message):
    console_text.insert("end", message + "\n")
    console_text.see("end")  
    root.update_idletasks() 

# to write the directory in the program   
def path_to_letters(directory_path):
    path_letters = list(directory_path)
    return path_letters
    
# automatization    
def helicon_focus():
    ask_folder = filedialog.askdirectory()
    if ask_folder == "":
        update_console("No files selected")
    else:
        update_console(ask_folder)
        time.sleep(1.0) 
        pyautogui.hotkey('winright')
        time.sleep(2.0) 
        pyautogui.typewrite(['h','e','l','i','c','o','n',' ','f','o','c','u','s',' ','8','\n'], interval=0.2)
        time.sleep(5.0)

        for x in range (0,6):
            pyautogui.hotkey('tab') #to get to methods

        pyautogui.keyDown('alt')#choose C
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.keyUp('alt')
        time.sleep(5.0)
        pyautogui.hotkey('F7')#batch
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')

        ruta_fotos = path_to_letters(ask_folder)#enter the directory
        pyautogui.typewrite(ruta_fotos, interval=0.05)
        pyautogui.hotkey('enter')

        for x in range (0,3):
            pyautogui.hotkey('down')

        pyautogui.hotkey('enter')#start

        update_console("Helicon Focus 8.2.2 is currently\nrunning. Check the program to see\nwhen it has finished.")
    
    
#to change the name of the folder    
def change_folder_name():
    directory_cfn= filedialog.askdirectory()
      
    if directory_cfn == "":
        update_console("No files selected")
    else:
        for x in sorted(os.listdir(directory_cfn), key=len):
            os.chdir(directory_cfn)
            update_console(x)
            split_x = x.split('_')
            if split_x[0] == 'Exp':
                update_console(x)
                clean_name = re.sub("Exp_STACK_", "", x)
                clean_name2 = clean_name.split('+')
                semifinal_name = clean_name.rstrip(clean_name2[-1])
                final_name = semifinal_name.rstrip(semifinal_name[-1])
                os.rename(x, final_name)
                update_console(final_name)
        update_console("The name of your folders has been changed.\nYou may need to refresh the folder.")

#change the name of the helicon output as your folder
def nombre_final():
    directory_nf= filedialog.askdirectory()
    if directory_nf == "":
        update_console("No files selected")
    else:
        update_console(directory_nf)
        os.chdir(directory_nf)
        for x in sorted(os.listdir(directory_nf), key=len): 
                update_console(x)
                for image in sorted(os.listdir(x), key=len):
                    update_console(image)
                    if image.endswith(".jpg"):
                        update_console(image)
                        os.rename(directory_nf + "/" + x +"/" + image, directory_nf + "/" + x +"/" + x +".jpg")
                        update_console("Process finished.")
                        

#put them in a single folder
def to_new_folder():  
    directory_newf= filedialog.askdirectory()
    if directory_newf == "":
        update_console("No files selected")
    else:
        update_console(directory_newf)
        os.chdir(directory_newf)
    
    if 'OUTPUT' not in sorted(os.listdir(), key=len):  
        os.mkdir(directory_newf + '/OUTPUT')  
  
    list_TODOS = sorted(os.listdir(directory_newf + '/OUTPUT'), key=len)
    
    for carpeta in sorted(os.listdir(directory_newf), key=len):
                if not carpeta.endswith("OUTPUT"):
                    fitxers = sorted(os.listdir(directory_newf + '/' + carpeta), key=len)
                    for fitxer in fitxers:
                        if fitxer.endswith(".jpg"):
                            foto_fitxer = fitxer
        
                            if foto_fitxer not in list_TODOS:
                                origen = directory_newf + '/' + carpeta + '/' + foto_fitxer
                                desti = directory_newf + '/OUTPUT'
                                shutil.copy(origen, desti)
    update_console("Your OUTPUT folder with all the\nstacked images is ready.")
    messagebox.showinfo(title=None, message="Process complete. OUTPUT ready.")
    
    

#------------------------------------#INTERFACE#--------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
# Create the root window
root = Tk()
root.title('AUTO-H')
root.geometry("700x540")
root.configure(bg="lightgray")

#Logo
icono_p = tk.PhotoImage(file="automatico.png")
root.iconphoto(False, icono_p, icono_p)

# Create a console-like frame for stitching progress
console_frame = Label(root, width=45, height=25, relief="solid", borderwidth=1,
                      highlightthickness=10.5, bg="white")
console_frame.pack()
console_frame.place(x=300, y=70)


# Create a text box for displaying progress or information
console_text = Text(root, width=38, height=20)
console_text.pack()
console_text.place(x=320, y=90)

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create the 'Options' dropdown menu
options_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Options', menu=options_menu)

# Create a File menu with a dropdown option
options_menu.add_command(label='Helicon-focus 8.2.2', font=("Open Sans", 10), command=helicon_focus)
options_menu.add_command(label='Change folder name', font=("Open Sans", 10), command= change_folder_name)
options_menu.add_command(label='Final name', font=("Open Sans", 10), command = nombre_final)
options_menu.add_command(label='New folder', font=("Open Sans", 10), command= to_new_folder)

doc_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Documentation', menu=doc_menu, font=("Open Sans",10))
doc_menu.add_command(label='How to use', font=("Open Sans", 10), command=instructions)
doc_menu.add_command(label='Author and attributions', font=("Open Sans", 10),command=attribution)
doc_menu.add_command(label='License', font=("Open Sans", 10), command=license)


#Create buttons for 
#helicon focus
button_hf = Button(root, text='Helicon-focus 8.2.2', bg="lightblue", height= 2, width=25, font=("Open Sans", 10), command=helicon_focus)
button_hf.pack()
button_hf.place(x=60, y=68)

#change name
button_cn = Button(root, text='Change folder name', bg="lightblue", height= 2, width=25, font=("Open Sans", 10), command= change_folder_name)
button_cn.pack()
button_cn.place(x=60, y=128)

#final name
button_fn = Button(root, text='Final name', bg="lightblue", height= 2, width=25, font=("Open Sans", 10), command = nombre_final)
button_fn.pack()
button_fn.place(x=60, y=188)

#new folder
button_nf = Button(root, text='New folder', bg="lightblue", height= 2, width=25, font=("Open Sans", 10), command= to_new_folder)
button_nf.pack()
button_nf.place(x=60, y=248)

#instructions
inst_image = Image.open("planificacion.png")
inst_image = inst_image.resize((40, 40))
inst_photo = ImageTk.PhotoImage(inst_image)
button_inst = Button(root, image=inst_photo, bg="lightgray", command=instructions)
button_inst.pack()
button_inst.place(x=535, y=10)

#clear
cl_image = Image.open("clean.png")
cl_image = cl_image.resize((40, 40))
cl_photo = ImageTk.PhotoImage(cl_image)
button_cl = Button(root, image=cl_photo, bg="lightgray", command=clear_console)
button_cl.pack()
button_cl.place(x=595, y=10)

#deco
auto_image = Image.open("automatico.png")
auto_image = auto_image.resize((145, 145))
auto_photo = ImageTk.PhotoImage(auto_image)
label_auto = Label(root, image=auto_photo, bg="lightgray", bd=4)
label_auto.pack()
label_auto.place(x=76, y=320)

#Create text for copyright
text_copyright = Label(root, text=" Creative Commons Copyright License Attribution 4.0 International",bg="lightgray", fg="black", font=("Open Sans", 6))
text_copyright.pack()
text_copyright.place(x=390, y=480)

#set program directory
program_directory = os.getcwd()
print(program_directory)

# Start the GUI event loop
root.mainloop()

