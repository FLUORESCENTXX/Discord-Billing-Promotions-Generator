import requests

def get_promotion_codes(self):
    url = f"https://discord.com/api/v8/promotions/pics-art"
    headers = {"authorization: self.token,
               "accept": "/"
               "authority": "discordapp.com"
               }
    r = requests.get(url, headers=headers)          