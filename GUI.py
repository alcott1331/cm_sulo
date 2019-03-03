import tkinter as tk
from StringLanguage import UserInterFaceLabels as Language
import ctypes
import Cryptography
class MainGUI:
    __root = None
    __inp_License1 = None
    __inp_License2 = None
    __inp_ApiToken = None
    __btn_Check_License = None
    __btn_Active_Bot = None
    __lbl_text_License1 = None
    __lbl_text_License2 = None
    __lbl_text_ApiToken = None


    __value__License1 = None
    __value__License2 = None
    __value__ApiToken = None


    __token_auth = None
    __License1_auth = None
    __License2_auth = None

    __bool_Actived_bot = False
    __bool_Allow_to_active = False

    def __msgBox(self, text, title):
        ctypes.windll.user32.MessageBoxW(0, text, title, 0)
    """----------------------------------------------------"""

    def  __active_the_bot(self):
        import RobotInterface
        x = RobotInterface.RobotWire(self.__token_auth)

    def __btn_press_ActiveBot(self):
        if self.__bool_Actived_bot and self.__bool_Allow_to_active:
            import threading
            t1 = threading.Thread(target = self.__active_the_bot)
            t1.start()

            self.__root.withdraw()
        else:

            token = str(self.__value__ApiToken.get())
            if  token != None and len(token) > 40:
                self.__token_auth = token
                import DataBank
                db_wire = DataBank.DataBank()
                try:
                    db_wire.insertToken_and_ActiveCode(self.__token_auth, self.__License1_auth, self.__License2_auth)
                    self.__bool_Actived_bot = True
                except Exception as ex:
                    db_wire.edit(self.__token_auth, self.__License1_auth, self.__License2_auth)
                    self.__bool_Actived_bot = True
                self.__btn_Active_Bot.config(text="Hide Bot")
            else:
                self.__msgBox(Language.err_Token_Invalid_text, Language.err_Token_Invalid_title)




    def __btn_press_Licensing_Validation(self):
        if len(self.__value__License1.get()) < 108 or len(self.__value__License1.get()) > 108:
            self.__msgBox(Language.err_LicenseKey_Invalid_text, Language.err_LicenseKey_Invalid_title)
            self.__bool_Allow_to_active = False

        elif len(self.__value__License2.get()) < 108 or len(self.__value__License2.get()) > 108:
            self.__msgBox(Language.err_LicenseKey_Invalid_text, Language.err_LicenseKey_Invalid_title)
            self.__bool_Allow_to_active = False

        elif Cryptography.LicenseKey(self.__value__License1.get(), self.__value__License2.get()).Check_License():
            self.__msgBox(Language.ok_LicenseKey_is_ok_text, Language.ok_LicenseKey_is_ok_title)
            self.__License1_auth = str(self.__value__License1.get())
            self.__License2_auth = str(self.__value__License2.get())
            self.__btn_Active_Bot.config(state=tk.NORMAL)
            self.__bool_Allow_to_active = True
        else:
            self.__msgBox(Language.err_LicenseKey_Invalid_text, Language.err_LicenseKey_Invalid_title)
            self.__bool_Allow_to_active = False




    """----------------------------------------------------"""

    def __init__(self):

        self.__root = tk.Tk(screenName=Language.lbl_AppName)
        self.__root.title(Language.lbl_AppName)
        self.__root.resizable(False, False)
        self.__root.iconbitmap("icon.ico")
        self.__root.config(bg='#3c3f41')


        self.__value__License1 = tk.StringVar()
        self.__value__License2 = tk.StringVar()
        self.__value__ApiToken = tk.StringVar()


        """----------------------------------------------"""
        self.__lbl_text_License1 = tk.Label(self.__root, text=Language.inp_License1)
        self.__lbl_text_License1.grid(row=0, column=0, sticky=tk.W)
        self.__lbl_text_License1.config(bg='#3c3f41', fg='#afb1b3')

        self.__inp_License1 = tk.Entry(self.__root, textvariable=self.__value__License1, width=40)
        self.__inp_License1.grid(row=0, column=1, sticky=tk.E)
        self.__inp_License1.config(bg='#626262')




        self.__lbl_text_License2 = tk.Label(self.__root, text=Language.inp_License2)
        self.__lbl_text_License2.grid(row=1, column=0, sticky=tk.W)
        self.__lbl_text_License2.config(bg='#3c3f41', fg='#afb1b3')

        self.__inp_License2 = tk.Entry(self.__root, textvariable=self.__value__License2, width=40)
        self.__inp_License2.grid(row=1, column=1, sticky=tk.E)
        self.__inp_License2.config(bg='#7d7d7d')




        self.__lbl_text_ApiToken = tk.Label(self.__root, text=Language.inp_ButtonApiToken)
        self.__lbl_text_ApiToken.grid(row=2, sticky=tk.W)
        self.__lbl_text_ApiToken.config(bg='#3c3f41', fg='#afb1b3')

        self.__inp_ApiToken = tk.Entry(self.__root, textvariable=self.__value__ApiToken, width=40)
        self.__inp_ApiToken.grid(row=2, column=1, sticky=tk.E)
        self.__inp_ApiToken.config(bg='#959595')




        self.__btn_Active_Bot = tk.Button(self.__root, text=Language.btn_ButtonActiveBot, command=self.__btn_press_ActiveBot)
        self.__btn_Active_Bot.grid(row=3, column=0, sticky=tk.W, columnspan=2)
        self.__btn_Active_Bot.config(bg='#3c3f41', fg='#afb1b3', relief=tk.GROOVE, state=tk.DISABLED)


        self.__btn_Check_License = tk.Button(self.__root, text=Language.btn_ButtonCheckLicense, command=self.__btn_press_Licensing_Validation)
        self.__btn_Check_License.grid(row=3, column=1, sticky=tk.E)
        self.__btn_Check_License.config(bg='#3c3f41', fg='#afb1b3', relief=tk.GROOVE)
        """----------------------------------------------"""




        self.__root.mainloop()




x = MainGUI()
