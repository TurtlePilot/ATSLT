# A T S L T - Audio To Sign Language Translator
# Programmed by Benjamin Taylor 19044585
# SpeechRecognition, pyaudio, OpenCV and pyttsx3 are required for this program to function.
# Programmed in PyCharm CE 2023.1 IDE.

import speech_recognition as sr
import cv2
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initializes TTS engine
engine = pyttsx3.init()

while True:
    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Please speak into the Microphone!")

        # TTS asks user to speak into the microphone
        engine.say("Please speak into the microphone!")
        engine.runAndWait()

        # Sets minimum energy threshold for recognizing speech which allows more accurate recognition
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    # Use Google Speech Recognition to recognize the audio
    text = r.recognize_google(audio)

    # Uses engine to say the recognized text from source
    engine.say(f"You said: {text}")
    engine.runAndWait()

    # Display the recognized text to the user
    print(f"You said: {text}")

    # Will ask the user whether they are left-handed or right-handed
    engine.say("Are you left-handed or right-handed? Enter 'Left' or 'Right'")
    engine.runAndWait()
    hand = input("Are you left-handed or right-handed? Enter 'Left' or 'Right'")

    # This will use OpenCV to display the sign language images
    if hand.lower() == 'left':
        sign_language_images = {

            # left-handed sign language alphabet section
            "a": cv2.imread("left_a.png"),
            "b": cv2.imread("left_b.png"),
            "c": cv2.imread("left_c.png"),
            "d": cv2.imread("left_d.png"),
            "e": cv2.imread("left_e.png"),
            "f": cv2.imread("left_f.png"),
            "g": cv2.imread("left_g.png"),
            "h": cv2.imread("left_i.png"),
            "i": cv2.imread("left_i.png"),
            "j": cv2.imread("left_j.png"),
            "k": cv2.imread("left_k.png"),
            "l": cv2.imread("left_l.png"),
            "m": cv2.imread("left_m.png"),
            "n": cv2.imread("left_n.png"),
            "o": cv2.imread("left_o.png"),
            "p": cv2.imread("left_p.png"),
            "q": cv2.imread("left_q.png"),
            "r": cv2.imread("left_r.png"),
            "s": cv2.imread("left_s.png"),
            "t": cv2.imread("left_t.png"),
            "u": cv2.imread("left_u.png"),
            "v": cv2.imread("left_v.png"),
            "w": cv2.imread("left_w.png"),
            "x": cv2.imread("left_x.png"),
            "y": cv2.imread("left_y.png"),
            "z": cv2.imread("left_z.png"),

            # left-handed sign language phrases section
            "hello": cv2.imread("left_hello.png"),
            "goodbye": cv2.imread("left_goodbye.png"),
            "how are you": cv2.imread("left_how_are_you.png"),
            "thank you": cv2.imread("left_thank_you.png"),
            "you're welcome": cv2.imread("left_you're_welcome.png"),
            "you": cv2.imread("left_you.png"),
            "america": cv2.imread("left_america.png"),
            "brother": cv2.imread("left_brother.png"),
            "dad": cv2.imread("left_dad.png"),
            "computer": cv2.imread("left_computer.png"),
        }

    elif hand.lower() == 'right':
        sign_language_images = {

            # right-handed sign language alphabet section
            "a": cv2.imread("right_a.png"),
            "b": cv2.imread("right_b.png"),
            "c": cv2.imread("right_c.png"),
            "d": cv2.imread("right_d.png"),
            "e": cv2.imread("right_e.png"),
            "f": cv2.imread("right_f.png"),
            "g": cv2.imread("right_g.png"),
            "h": cv2.imread("right_i.png"),
            "i": cv2.imread("right_i.png"),
            "j": cv2.imread("right_j.png"),
            "k": cv2.imread("right_k.png"),
            "l": cv2.imread("right_l.png"),
            "m": cv2.imread("right_m.png"),
            "n": cv2.imread("right_n.png"),
            "o": cv2.imread("right_o.png"),
            "p": cv2.imread("right_p.png"),
            "q": cv2.imread("right_q.png"),
            "r": cv2.imread("right_r.png"),
            "s": cv2.imread("right_s.png"),
            "t": cv2.imread("right_t.png"),
            "u": cv2.imread("right_u.png"),
            "v": cv2.imread("right_v.png"),
            "w": cv2.imread("right_w.png"),
            "x": cv2.imread("right_x.png"),
            "y": cv2.imread("right_y.png"),
            "z": cv2.imread("right_z.png"),

            # right-handed sign language phrases section
            "hello": cv2.imread("right_hello.png"),
            "goodbye": cv2.imread("right_goodbye.png"),
            "how are you": cv2.imread("right_how_are_you.png"),
            "thank you": cv2.imread("right_thank_you.png"),
            "you're welcome": cv2.imread("right_you're_welcome.png"),
            "you": cv2.imread("right_you.png"),
            "america": cv2.imread("right_america.png"),
            "brother": cv2.imread("right_brother.png"),
            "dad": cv2.imread("right_dad.png"),
            "computer": cv2.imread("right_computer.png"),
        }
    else:
        print("Invalid input: Please enter 'left' or 'right'.")
        continue

    # Maps the recognized text to the sign language image
    if text in sign_language_images:
        image = sign_language_images[text]
        cv2.imshow("Sign Language Translation", image)
        cv2.waitKey(0)
    else:
        print("No sign language translation was found for what was said. Please try again.")
        engine.say("No sign language translation was found for what was said. Please try again.")
        engine.runAndWait()

    # Asks the user if they want to continue using the program
    engine.say("Do you want to continue? Enter 'Yes' or 'No'.")
    engine.runAndWait()
    answer = input("Do you want to continue? Enter 'Yes' or 'No'.")

    # If the user inputs no, then the while loop will break and end the program
    if answer.lower() == 'no':
        print("Thank you for using A T S L T!")
        engine.say("Thank you for using A T S L T!")
        engine.runAndWait()
        break
