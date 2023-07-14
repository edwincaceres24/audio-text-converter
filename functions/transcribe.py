#!/usr/bin/env python3

import speech_recognition as sr
import os 

current_dir = os.getcwd()

audio_folder_path = os.path.join(current_dir,'..', "audios")
transcription_folder_path = os.path.join(current_dir,'..',"transcriptions")
print(audio_folder_path)
wav_file_path = None

for file in os.listdir(audio_folder_path):
    if file.endswith(".wav"):
        wav_file_path = os.path.join(audio_folder_path, file)
        break

if wav_file_path:
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as audio_file:
        audio = recognizer.record(audio_file)
        try:
            text = recognizer.recognize_sphinx(audio)
            text_file_path = os.path.join(transcription_folder_path, "transcription.txt")
            with open(text_file_path, "w") as output_file:
                output_file.write(text)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
        except sr.RequestError as e:
            print("Error occurred during speech recognition:", str(e))
    
else:
    print("No wav file found in the 'audios' folder.")