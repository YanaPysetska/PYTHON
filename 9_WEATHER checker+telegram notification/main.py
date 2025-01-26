import requests
import os
from dotenv import load_dotenv

load_dotenv()

lat=12.610230
lon=37.468971
api_key = os.getenv("API_KEY")


def telegram_bot_sendtext(bot_message):
    bot_token = os.getenv("BOT_TOKEN")
    bot_chatID = os.getenv("BOT_CHAT_ID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

parameters={
    "lat":lat,
    "lon":lon,
    "appid":api_key,
    "cnt":4,
}
response=requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data=response.json()
will_rain=False
for i in weather_data:
    weather_id = weather_data['list'][0]['weather'][0]['id']
    if int(weather_id)<700:
        will_rain=True
if will_rain:
    test = telegram_bot_sendtext("Bring an umbrella ☔️")
    print(test)
else:
    test = telegram_bot_sendtext("There probably won't be any rain ☀️")
    print(test)



