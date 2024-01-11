"""
pip install googletrans==3.1.0a0
pip install SpeechRecognition
pip install PyAudio
pip install gTTS
pip install playsound==1.2.2
pip install wheel
sudo apt-get install python3-pyaudio
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio

"""
import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
with sr.Microphone() as source:
	print("Speak Now")
	voice = recognizer.listen(source)
	listen = recognizer.recognize_google(voice,language="en")
	print(listen)

#print(googletrans.LANGUAGES)

#data = "What is your name"
translator = googletrans.Translator()
#translate = translator.translate(data,dest="fr")
translate = translator.translate(listen,dest="fr")
#print(translate) #to display both the text and language source
print("The Result:")
print(translate.text) #to display only the text

converted_audio =gtts.gTTS(translate.text,lang="fr")
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")
