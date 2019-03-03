from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, MessageHandler
from Machin_and_Bot_interface import machinAndRobotInterface
from StringLanguage import Command_Labels
import urllib.request


class RobotWire:

    __token = None
    def __start(self, bot, update):
        keyboard = [
            [InlineKeyboardButton(Command_Labels.btn_get_ip, callback_data=Command_Labels.btn_get_ip),
                     InlineKeyboardButton(Command_Labels.btn_get_all_tasks, callback_data=Command_Labels.btn_get_all_tasks)]

                    ,[InlineKeyboardButton(Command_Labels.btn_get_screen_shoot, callback_data=Command_Labels.btn_get_screen_shoot)
                    ,InlineKeyboardButton(Command_Labels.btn_get_user_admins, callback_data=Command_Labels.btn_get_user_admins)]

                    ,[InlineKeyboardButton(Command_Labels.btn_get_users, callback_data=Command_Labels.btn_get_users)
                    ,InlineKeyboardButton(Command_Labels.btn_get_platform_info, callback_data=Command_Labels.btn_get_platform_info)]

                    ,[InlineKeyboardButton(Command_Labels.btn_reboot_system, callback_data=Command_Labels.btn_reboot_system)
                    ,InlineKeyboardButton(Command_Labels.btn_get_other_functions, callback_data=Command_Labels.btn_get_other_functions)]

                    ,[InlineKeyboardButton(Command_Labels.btn_get_expiration_date, callback_data=Command_Labels.btn_get_expiration_date)],]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose an item:', reply_markup=reply_markup)







    def __button_press(self, bot, update):
        machinAndRobotInterface().Pressed_Button(bot, update, self.__token)


    def __text_msg(self, bot, update):
        machinAndRobotInterface().Script_Parseer(bot, update, self.__token)

    def _download_file(self, bot, update):
        url = update.message.document.get_file().file_path
        urllib.request.urlretrieve(url, url.split("/")[-1])
        bot.send_message(text=("file saved in : {0}".format(url.split("/")[-1])), chat_id=update.message.chat_id)

    def __init__(self, token):
        import logging
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        self.__token = token
        try:
            update = Updater(token=token)
            dispatcher = update.dispatcher

            dispatcher.add_handler(CommandHandler('start', self.__start))
            dispatcher.add_handler(CallbackQueryHandler(self.__button_press))
            dispatcher.add_handler(MessageHandler(Filters.text, self.__text_msg))
            dispatcher.add_handler(MessageHandler(Filters.document, self._download_file))

            update.start_polling()
        except Exception as ex:
            print(ex)