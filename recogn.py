import speech_recognition as sr

# Создаем объект recognizer для распознавания речи
recognizer = sr.Recognizer()

# Функция для распознавания речи с помощью SpeechRecognition
def recognize_speech():
    with sr.Microphone() as source:
        print("Скажите что-нибудь:")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            print("Вы сказали:", text)
            process_command(text)
        except sr.UnknownValueError:
            print("Извините, не удалось распознать речь")
        except sr.RequestError as e:
            print("Ошибка при запросе к сервису распознавания речи; {0}".format(e))

# Функция для обработки команд
def process_command(command):
    if "привет" in command:
        print("Привет!")
    elif "как дела" in command:
        print("У меня все отлично, спасибо!")
    elif "пока" in command:
        print("До свидания!")
    else:
        print("Команда не распознана")

# Основной цикл программы
while True:
    recognize_speech()
