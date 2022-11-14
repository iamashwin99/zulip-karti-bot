# See readme.md for instructions on running this code.

from email import message
from typing import Any, Dict
import os
from zulip_bots.lib import BotHandler
import requests
import wget
import zulip
from pdf2image import convert_from_path
from PIL import Image
client = zulip.Client(config_file="/home/karnada/zulip/python-zulip-api/zuliprc")

class KartiHandler:
    def getDESYMenu(self):
        # take a screen shot of the site  https://desy.myalsterfood.de/
        pass



    def uploadImage(self, filename,method='zulip'):
        if(method=='zulip'):
            with open(filename, "rb") as fp:
                result = client.upload_file(fp)
            os.remove(filename)
            return result["uri"]

    def getMenu(self,day='today'):
        # day can be today, next_day
        image_f_name = "menu.jpg"
        pdf_f_name = "menu.pdf"
        response = wget.download("https://www.stwhh.de/en/?type=1628686455&l=177&t="+day, "menu.pdf")
        images = convert_from_path(pdf_f_name)
        image = images[0]
        image=image.resize((660,932),Image.ANTIALIAS)
        image.save(image_f_name, 'JPEG', optimize = True, compress_level = 9)
       
        url=self.uploadImage(image_f_name)
        os.remove(pdf_f_name)
        return  "[Check here]("+url+")"


    def usage(self) -> str:
        return """
        Hallo I am Karti a potato
        I live in Germany but I dont know much german
        I make my own food but I can help you with the menu and other things
        I speak English and I can read german

        I am a potato


        """

    def handle_message(self, message: Dict[str, Any], bot_handler: BotHandler) -> None:
        def sendUsage():
            content = """
            Hallo I am Karti a potato
            Please DM/tag me with `today` or `tomorrow` to get the CFEL menu
            Im assuming you wanted to know todays menu"""
            bot_handler.send_reply(message, content)
            return 

        user_msg=message['content'].lower()
        if("today" in user_msg):
            day='today'
        elif("tomorrow" in user_msg):
            day='next_day'
        else:
            sendUsage()
            day='today'
        content = self.getMenu(day=day)
        bot_handler.send_reply(message, content)

        emoji_name = "wave"  # type: str
        bot_handler.react(message, emoji_name)
        return
   
handler_class = KartiHandler
