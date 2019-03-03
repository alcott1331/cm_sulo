from telegram import ParseMode

from StringLanguage import Command_Labels as cmd
import Functions
import os

class Procurement_Manager:
    def GetAllTask_in_manager(self, bot, query):
        file = open("task.txt", "w")
        import Functions
        for i in Functions.GetAllTask():
            text = "{ " + i[0] + " } [ PID  " + i[1] + " ]\n"
            file.write(text)
        file.close()
        bot.send_document(query.message.chat_id, open("task.txt", 'rb'))
        os.remove("task.txt")

    def TakeScreenShoot(self, bot, query):
        sc_path = Functions.TakeScreenShoot()
        bot.send_photo(query.message.chat_id, open(sc_path, "rb"))
        os.remove(sc_path)

    def GetSystemInfo(self, bot, query):
        bot.edit_message_text(text=str(Functions.GetPlatformInfo()),
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id, parse_mode=ParseMode.MARKDOWN)


    def GetIP(self, bot, query):
        ip = Functions.GetIP()
        bot.edit_message_text(text="Public IP : {0}Private IP : {1}".format(ip[0], ip[1]),
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)

    def GetOtherFunctions(self, bot, query):
        bot.edit_message_text(text=Functions.Help(),
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              parse_mode=ParseMode.MARKDOWN)

    def getAdminUsers(self, bot, query, token):
        Functions.GetList_of_admins(token, query.message.chat_id)


    def getUsers(self, bot, query, token):
        Functions.GetList_of_users(token, query.message.chat_id)


    def sendFile(self,bot, update, path):
        if not os.path.exists(path):
            bot.send_message(text="File or Directory is not Exists!", chat_id=update.message.chat_id)
        else:
            bot.send_document(update.message.chat_id, open(path, 'rb'))


    def openFile(self, bot, update):
        ans = Functions.open_file(update.message.text[5:])
        bot.send_message(text=str(ans), chat_id=update.message.chat_id)

    def delete_file(self, bot, update):
        ans = Functions.delete_file(update.message.text[7:])
        bot.send_message(text=str(ans), chat_id=update.message.chat_id)

    def copy_file(self, bot, update):
        ans = Functions.copy_file(str(update.message.text[5:]).split("->")[0], str(update.message.text[5:]).split("->")[1])
        bot.send_message(text=str(ans), chat_id=update.message.chat_id)


    def move_file(self, bot, update):
        ans = Functions.move_file(str(update.message.text[5:]).split("->")[0], str(update.message.text[5:]).split("->")[1])
        bot.send_message(text=str(ans), chat_id=update.message.chat_id)

    def reboot_system(self, bot, update):
        Functions.reboot()

    def add_user(self, bot, update, token, name, pwd):
        Functions.AddUser(token=token, id=update.message.chat_id,name=name, pwd=pwd)

    def show_expiration_date(self, bot, update):
        import DataBank
        info = DataBank.DataBank().getTokenAndActiveCode()
        import StringLanguage as Language
        bot.send_message(text=Language.UserInterFaceLabels.info_License_expert.format("*"+info[2]+"*",\
                    "@ٍExample_bot"),
                         chat_id=update.message.chat_id,
                         parse_mode=ParseMode.MARKDOWN)




class machinAndRobotInterface:
    def __init__(self):
        pass

    def Pressed_Button(self, bot, update, token):
        query = update.callback_query

        if query.data == cmd.btn_get_all_tasks:
            Procurement_Manager().GetAllTask_in_manager(bot, query)

        if query.data == cmd.btn_get_screen_shoot:
            Procurement_Manager().TakeScreenShoot(bot, query)

        if query.data == cmd.btn_get_ip:
            Procurement_Manager().GetIP(bot, query)

        if query.data == cmd.btn_get_other_functions:
            Procurement_Manager().GetOtherFunctions(bot, query)

        if query.data == cmd.btn_get_users:
            Procurement_Manager().getUsers(bot, query, token)

        if query.data == cmd.btn_get_user_admins:
            Procurement_Manager().getAdminUsers(bot, query, token)

        if query.data == cmd.btn_reboot_system:
            Procurement_Manager().reboot_system(bot, query)

        if query.data == cmd.btn_get_platform_info:
            Procurement_Manager().GetSystemInfo(bot, query)

        if query.data == cmd.btn_get_expiration_date:
            Procurement_Manager().show_expiration_date(bot=bot, update=query)




    def Script_Parseer(self, bot, update, token):
        text = update.message.text
        if text[:4] == "cmd:":
            bot.send_message(text=Functions.ShellScript(text[4:], token, update.message.chat_id), chat_id=update.message.chat_id)
        if text[:4] == "get:":
            Procurement_Manager().sendFile(bot, update, text[4:])

        if text[:5] == "open:":
            Procurement_Manager().openFile(bot, update)

        if text[:5] == "copy:":
            Procurement_Manager().copy_file(bot, update)

        if text[:5] == "move:":
            Procurement_Manager().move_file(bot, update)

        if text[:7] == "delete:":
            Procurement_Manager().delete_file(bot, update)

