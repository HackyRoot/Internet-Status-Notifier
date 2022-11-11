# import asyncio
# import telegram

# bot = telegram.Bot("5517808661:AAFi_DwbMlwwbZELzqbibdFF8lNDLfShr4U")
# print(bot.get_me())


# import requests

# TOKEN = "5517808661:AAFi_DwbMlwwbZELzqbibdFF8lNDLfShr4U"
# chat_id = "5517808661"
# message = "hello from your telegram bot"
# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# print(requests.get(url).json()) # this sends the message


import requests

def send_to_telegram(message):

    apiToken = '5517808661:AAFi_DwbMlwwbZELzqbibdFF8lNDLfShr4U'
    chatID = '274659714'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)