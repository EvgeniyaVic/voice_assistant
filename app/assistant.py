import speech_recognition as sr
import random
import playsound
import os
from gtts import gTTS
import datetime
import webbrowser


def listen():
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Скажите что-то >>>')
        audio = voice_recognizer.listen(source)
    try:
        voice_text = voice_recognizer.recognize_google(audio, language='ru')
        print(f'Вы сказали: {voice_text}')
        return voice_text
    except sr.UnknownValueError:
        return 'Ошибка распознания'
    except sr.RequestError:
        return 'Ошибка соединения'


def say(text):
    voice = gTTS(text, lang='ru')
    unique_file = 'audio ' + str(random.randint(0, 10000)) + '.mp3'
    voice.save(unique_file)
    playsound.playsound(unique_file)
    os.remove(unique_file)

    print(f'Ассистент: {text}')



def handle_command(command):
    command = command.lower()
    if command == 'привет':
        say('Привет-привет')
    elif command == 'открой браузер':
        webbrowser.open('google.com')
        say('Google открыт')
    elif command == 'время':
        str_time = datetime.datetime.now().strftime('%H: %M')
        say(f'Сейчас {str_time}')
    elif command == 'включи музыку':
        webbrowser.open('https://www.youtube.com/results?search_query=stromae')
        say('Включаю')
    elif command == 'пока':
        stop()
    else:
        say('Повторите, не понятно')



def stop():
    say('До скорого')
    exit()




def start():
    print("Запуск ассистента..." )

    while True:
        command = listen()
        handle_command(command)


try:
    start()
except KeyboardInterrupt:
    stop()
