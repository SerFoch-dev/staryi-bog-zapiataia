from pynput import keyboard
import winsound
import os

SOUNDS = {
    ',': 'sounds/comma.wav',
}

def on_press(key):
    try:
        char = key.char

        if char in SOUNDS:
            sound = SOUNDS[char]

            if os.path.exists(sound):
                winsound.PlaySound(
                    sound,
                    winsound.SND_FILENAME | winsound.SND_ASYNC
                )

    except AttributeError:
        pass

print("Program is running.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()