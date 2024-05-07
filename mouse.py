from pynput import mouse

def on_move(x, y):
    with open('mouse_log.txt', 'a') as f:
        f.write('Pointer moved to {0}\n'.format((x, y)))

def on_click(x, y, button, pressed):
    with open('mouse_log.txt', 'a') as f:
        f.write('{0} at {1}\n'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
    if not pressed:
        return False

def on_scroll(x, y, dx, dy):
    with open('mouse_log.txt', 'a') as f:
        f.write('Scrolled {0} at {1}\n'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)

listener.start()