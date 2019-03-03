import sys
import os
sys.path.insert(0, "Functions.py")
sys.path.insert(0, "Cryptography.py")
sys.path.insert(0, "UserInterface.py")
sys.path.insert(0, "DataBank.py")
sys.path.insert(0, "StringLanguage.py")
sys.path.insert(0, "RobotInterface.py")
sys.path.insert(0, "Machin_and_Bot_interface.py")
sys.path.insert(0, "GUI.py")

import Cryptography

from DataBank import DataBank
if os.path.exists("configs.db"):
    data = DataBank()
    data = data.getTokenAndActiveCode()
    import Cryptography
    auth = [False, False]
    if len(data[0]) < 40:
        import ctypes  # An included library with Python install.
        ctypes.windll.user32.MessageBoxW(0, "Api Token Invalid", "Error in Api Token", 0)
        import GUI
    else:
        auth[0] = True

    if not Cryptography.LicenseKey(Cryptography.BigAss().encode(text=data[1]),
                                   Cryptography.BigAss().encode(text=data[2])).Check_License():
        import ctypes  # An included library with Python install.
        ctypes.windll.user32.MessageBoxW(0, "LicenseKey Invalid", "Error in LicenseKey value", 0)
        print("d1\t{0}\nd2\t{1}".format(data[1], data[2]))
        import GUI
    else:
        auth[1] = True

    if auth[0] == True and auth[1] == True:
        from DataBank import DataBank
        x = DataBank()
        args = x.getTokenAndActiveCode()
        from RobotInterface import RobotWire
        xc = RobotWire(args[0])
else:
    import GUI