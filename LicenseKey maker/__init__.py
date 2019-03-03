import tkinter as tk
import sys
import ctypes
import base64
sys.path.insert(0,"StringLanguage.py")
from StringLanguage import GUI_Label



class Cryptography:
    def checkDateFormat(self, date):
        digit_count = 0
        slash_count = 0
        for item in date:
            if str(item).isdigit():
                digit_count += 1
            if item == '/':
                slash_count += 1

        number_section = [False, False, False]
        try:
            temp = str(date).split('/')[0]
            if len(temp) == 4 and int(temp):
                number_section[0] = True

            temp = str(date).split('/')[1]
            if len(temp) == 2 and int(temp):
                number_section[1] = True

            temp = str(date).split('/')[2]
            if len(temp) == 2 and int(temp):
                number_section[2] = True
            return True
        except Exception as ex:
            return False

    def encode(self, text):

        memory = ""
        for item in text:
            memory += str((ord(item)) << 3) + "e"

        memory = str(base64.b16encode(bytes(memory, 'utf-8'))).split('b')[1].split('\'')[1].split('\'')[-1]
        return str(base64.b64encode(bytes(memory, 'utf-8'))).split('b')[1].split('\'')[1].split('\'')[-1]


class GUI:
    __root = None
    __val_start = None
    __val_end = None

    __val_hash1 = None
    __val_hash2 = None

    def __msgBox(self, text, title):
        ctypes.windll.user32.MessageBoxW(0, text, title, 0)

    def __btn_press(self):
        start = self.__val_start.get()
        end = self.__val_end.get()
        if len(start) == 10 and len(end) == 10:
            if Cryptography().checkDateFormat(start) and Cryptography().checkDateFormat(end):
                self.__val_hash1.set(Cryptography().encode(start))
                self.__val_hash2.set(Cryptography().encode(end))
        else:
            self.__msgBox(GUI_Label.error_text, GUI_Label.error_title)


    def __init__(self):
        self.__root = tk.Tk("LicenseKey Maker")
        self.__root.title("LicenseKey Maker")
        self.__root.resizable(False, False)
        self.__val_hash1 = tk.StringVar()
        self.__val_hash2 = tk.StringVar()
        self.__val_start = tk.StringVar()
        self.__val_end = tk.StringVar()

        self.__root.config(bg='#3c3f41')
        lbl_top_head_info = tk.Label(self.__root, text=GUI_Label.lbl_top_head)
        lbl_top_head_info.grid(row=0, column=0, columnspan=3)
        lbl_top_head_info.config(bg='#3c3f41', fg='#ffa9a9')

#----------------------------------------------
        lbl_text_start_date = tk.Label(self.__root, text=GUI_Label.lbl_text_start_date)
        lbl_text_start_date.grid(row=1, column=0)
        lbl_text_start_date.config(bg='#3c3f41', fg='#FEEEEA')

        inp_start_date = tk.Entry(self.__root, textvariable=self.__val_start)
        inp_start_date.grid(row=1, column=1)
        inp_start_date.config(bg='#626262', fg='#f8e4b0')


        lbl_text_start_date_example = tk.Label(self.__root, text=GUI_Label.lbl_text_start_date_example)
        lbl_text_start_date_example.grid(row=1, column=2)
        lbl_text_start_date_example.config(bg='#3c3f41', fg='#FEEEEA')
#-----------------------------------------------

        lbl_text_end_date = tk.Label(self.__root, text=GUI_Label.lbl_text_end_date)
        lbl_text_end_date.grid(row=2, column=0)
        lbl_text_end_date.config(bg='#3c3f41', fg='#FEEEEA')

        inp_end_date = tk.Entry(self.__root, textvariable=self.__val_end)
        inp_end_date.grid(row=2, column=1)
        inp_end_date.config(bg='#626262', fg='#f8e4b0')

        lbl_text_end_date_example = tk.Label(self.__root, text=GUI_Label.lbl_text_end_date_example)
        lbl_text_end_date_example.grid(row=2, column=2)
        lbl_text_end_date_example.config(bg='#3c3f41', fg='#FEEEEA')
#----------------------------------------------


        lbl_text_start_date_hash = tk.Label(self.__root, text=GUI_Label.lbl_text_start_date_hash)
        lbl_text_start_date_hash.grid(row=3, column=0)
        lbl_text_start_date_hash.config(bg='#3c3f41', fg='#FEEEEA')

        inp_start_date_hash = tk.Entry(self.__root, width=33, textvariable=self.__val_hash1)
        inp_start_date_hash.grid(row=3, column=1, columnspan=2)
        inp_start_date_hash.config(bg='#626262', fg='#f8e4b0')
#-----------------------------------------------a

        lbl_text_end_date_hash = tk.Label(self.__root, text=GUI_Label.lbl_text_end_date_hash)
        lbl_text_end_date_hash.grid(row=4, column=0)
        lbl_text_end_date_hash.config(bg='#3c3f41', fg='#FEEEEA')

        inp_end_date_hash = tk.Entry(self.__root, width=33, textvariable=self.__val_hash2)
        inp_end_date_hash.grid(row=4, column=1, columnspan=2)
        inp_end_date_hash.config(bg='#626262', fg='#f8e4b0')
#----------------------------------------------


        btn_make_hash = tk.Button(self.__root, text=GUI_Label.btn_make_hash, command=self.__btn_press)
        btn_make_hash.grid(row=5, column=1, columnspan=1)
        btn_make_hash.config(bg='#7d7d7d', fg='#FFFFFF')

        self.__root.mainloop()



GUI()
