import os
import timeit

def get_filenames(path):
    filenames = os.listdir(path)
    filenames = [int(name.split('.')[0]) for name in filenames]
    filename = sorted(filenames)[-1]
    return filename


path = 'C:\\Users\\mitch\\AppData\\Roaming\\Factorio\\script-output\\run1'
r = get_filenames(path)
print(r)

timerun = timeit.timeit(lambda: get_filenames(path=path), number = 60)
print(timerun)