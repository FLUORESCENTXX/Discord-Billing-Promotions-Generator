import requests

# Theres no current working apis for checking these codes, this used to work if not try xbox game pass
def get_promotion_codes(self):
    url = f"https://discord.com/api/v8/promotions/pics-art"
    headers = {"authorization: self.token,
               "accept": "/"
               "authority": "discordapp.com"
               }
    r = requests.get(url, headers=headers)          
