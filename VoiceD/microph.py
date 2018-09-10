import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index = 1, sample_rate = 48000) as source:
    print("Say something!")
    audio = r.record(source,duration = 5)
	
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())