from pynput.keyboard import Listener as  KeyboardListener
import sys

def on_press(keys):
    key = str(keys).replace("'", "")
    if key == 'Key.delete':
        sys.exit('delete key pressed')
    print(key)
        

def on_release(keys):
    key = str(keys).replace("'", "")
    print(key)




with KeyboardListener(
    on_press=lambda event: on_press(event), 
    on_release=lambda event: on_release(event)
) as listener:
    listener.join()