import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()
translator = google_translator()

while True:
    with sr.Microphone() as source:
        print("Speak Now!")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if (speech_text == "exit"):
                break
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError:
            print("Could not request result from google")

        translated_text = translator.translate(speech_text, lang_tgt='fr')
        print(translated_text)

        voice = gTTS(translated_text, lang='fr')
        voice.save("voice.mp3")
        playsound("voice.mp3")

        os.remove("voice")
