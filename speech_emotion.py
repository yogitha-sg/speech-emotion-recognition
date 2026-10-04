import speech_recognition as sr

print("=" * 60)
print("          SPEECH EMOTION RECOGNITION")
print("=" * 60)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("\nAdjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Speak with your emotion...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)

    print("\nRecognized Speech:")
    print(text)

    # Simple emotion classification based on words
    text_lower = text.lower()

    angry_words = ["angry", "hate", "furious", "mad", "terrible"]
    happy_words = ["happy", "excited", "wonderful", "great", "love"]
    sad_words = ["sad", "cry", "lonely", "upset", "hurt"]

    if any(word in text_lower for word in angry_words):
        emotion = "Angry"
    elif any(word in text_lower for word in happy_words):
        emotion = "Happy"
    elif any(word in text_lower for word in sad_words):
        emotion = "Sad"
    else:
        emotion = "Neutral"

    print("\nDetected Emotion:", emotion)

except sr.UnknownValueError:
    print("\nCould not understand the speech.")

except sr.RequestError:
    print("\nSpeech recognition service is unavailable.")