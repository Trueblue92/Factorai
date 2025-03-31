from pynput.mouse import Listener as MouseListener

def on_move(x, y):
    print(x," ",y)


with MouseListener(
    on_move = lambda x, y: on_move(x=x, y=y)
) as listener:
    listener.join()