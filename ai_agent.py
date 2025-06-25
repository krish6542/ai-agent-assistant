
import requests
import datetime

weather_api_key = '8494ec878f131cf22b92ab212c31cefc'

def get_weather(city="Thrissur"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        return f"The weather in {city} is {temp}°C with {desc}."
    else:
        return "Couldn't fetch weather."

def get_quote():
    url = "https://zenquotes.io/api/today"
    response = requests.get(url).json()
    return f""{response[0]['q']}" - {response[0]['a']}"

def check_day_status():
    today = datetime.datetime.today().weekday()
    if today >= 5:
        return "🎉 It's a holiday!"
    else:
        return "💼 It's a working day."

print("🤖 Hello! Ask me about weather, a quote, or if today is a holiday. Type 'exit' to stop.
")

while True:
    user_input = input("You: ")
    if "weather" in user_input.lower():
        print("🤖", get_weather())
    elif "quote" in user_input.lower():
        print("🤖", get_quote())
    elif "today" in user_input.lower() or "holiday" in user_input.lower():
        print("🤖", check_day_status())
    elif user_input.lower() in ["exit", "bye", "quit"]:
        print("🤖 Goodbye! 👋")
        break
    else:
        print("🤖 Sorry, I can tell you weather, quotes, or if today is a working day.")
