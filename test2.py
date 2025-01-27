import time
import os 

def get_tick():
    with open(path, 'r') as file:
        data = file.readlines()
    if data is None or data == []:
        return get_tick()
    else:
        return data   



path = "C:\\Users\\mitch\\AppData\\Roaming\\Factorio\\script-output\\tick.txt"
# if os.path.exists(path):
#     with open(path, 'r') as file:
#         data = file.readlines()
#     if data is not None or data != []:
#         last_played_tick = data
while True:
   print(get_tick())
   time.sleep(1/60)
