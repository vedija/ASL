import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for speech...")
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)  # Use recognizer instance
        print(f"Recognized Text: {recognized_text}")  # Debugging log
        return recognized_text
    except sr.UnknownValueError:
        print("Could not understand the audio")  # Debugging log
        return "Could not understand the audio"
    except sr.RequestError:
        print("Speech Recognition service is unavailable")  # Debugging log
        return "Speech Recognition service is unavailable"
