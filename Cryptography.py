import base64
class BigAss:
    def __init__(self):
        pass

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

        except Exception as ex:
            return False

        try:
            from datetime import datetime
            OnlineUTCTime = datetime.strptime(date, '%Y/%m/%d')
            OnlineUTCTime = datetime.fromtimestamp(OnlineUTCTime.timestamp()).strftime("%Y/%m/%d")
        except Exception as ss:
            return False

        if digit_count == 8 and slash_count == 2 and number_section[0] == True\
            and number_section[1] == True and number_section[2] == True:
            return True
        else:
            return False


    def text_decode(self, text):
        try:
            text = str(base64.b64decode(bytes(text, 'utf-8'))).split('b')[1].split('\'')[1].split('\'')[-1]
            text = str(base64.b16decode(bytes(text, 'utf-8'))).split('b')[1].split('\'')[1].split('\'')[-1]




            mini_buffer = ""
            big_buffer = ""

            for item in text:
                if not str(item).isdigit() and item != 'e':
                    return None

                if len(mini_buffer) == 10:
                    return mini_buffer
                if str(item).isdigit():
                    mini_buffer += item
                if item == 'e':
                    big_buffer += chr(int(mini_buffer) >> 3)
                    mini_buffer = ""

            return big_buffer
        except Exception as ex:
            return None
    def encode(self, text):

        memory = ""
        for item in text:
            memory += str((ord(item)) << 3) + "e"

        memory = str(base64.b16encode(bytes(memory, 'utf-8'))).split('b')[1].split('\'')[1].split('\'')[-1]
        return str(base64.b64encode(bytes(memory, 'utf-8'))).split('b')[1].split('\'')[1].split('\'')[-1]
        #return memory

    def decode(self, text):
        try:
            text = str(base64.b64decode(bytes(text, 'utf-8'))).split('b')[1].split('\'')[1].split('\'')[-1]
            text = str(base64.b16decode(bytes(text, 'utf-8'))).split('b')[1].split('\'')[1].split('\'')[-1]




            mini_buffer = ""
            big_buffer = ""
            if len(text)> 40 or len(text) < 40:
                return None
            for item in text:
                if not str(item).isdigit() and item != 'e':
                    return None

                if len(mini_buffer) == 10:
                    return mini_buffer
                if str(item).isdigit():
                    mini_buffer += item
                if item == 'e':
                    big_buffer += chr(int(mini_buffer) >> 3)
                    mini_buffer = ""

            return big_buffer
        except Exception as ex:
            return None



class LicenseKey:

    __I = None
    __II = None

    def __getToday(self):
        import ntplib
        from datetime import datetime

        c = ntplib.NTPClient()
        try:
            response = c.request('europe.pool.ntp.org', version=3)

            x = datetime.fromtimestamp(int(response.tx_time)).strftime("%Y/%m/%d")
            return x
        except Exception as ex:
            print(ex)
            try:
                from urllib import request
                from datetime import datetime

                webpage = request.urlopen("http://just-the-time.appspot.com/")
                internettime = webpage.read()
                internettime = str(internettime.strip()).split('b')[1].split('\'')[1]
                OnlineUTCTime = datetime.strptime(internettime, '%Y-%m-%d %H:%M:%S')
                OnlineUTCTime = datetime.fromtimestamp(OnlineUTCTime.timestamp()).strftime("%Y/%m/%d")
                return OnlineUTCTime

            except Exception as EX1:
                print(EX1)
                return None


    def __init__(self, I_license, II_license):
        self.__I = I_license
        self.__II = II_license

    def Check_License(self):
        start_date = BigAss().decode(self.__I)
        end_date   = BigAss().decode(self.__II)
        if start_date == None or end_date == None:
            return False
        if BigAss().checkDateFormat(start_date) == False or BigAss().checkDateFormat(end_date) == False:
            return False


        #print(start_date, "\t", end_date, "\t decoded ")
        today = self.__getToday()

        if today == None:
            import time
            today = str(time.strftime("%Y/%m/%d"))
            print(today, " is local date")


        if start_date <= today and end_date >= today:
            if today <= end_date:
                return True
            else:
                return False
        else:
            return False




