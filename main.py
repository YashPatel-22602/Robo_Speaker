import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to Text-to-Speech Program Created by Yash Patel")
    while True:
        text = input("Enter the text you want to convert to speech (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        engine.say(text)
        engine.runAndWait()
