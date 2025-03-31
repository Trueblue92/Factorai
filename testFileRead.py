from writeread_actionsfromfile import readActionsfromFileDeltaKeypress

result = readActionsfromFileDeltaKeypress("./run1/inputs/keys.txt")
for keypress in result:
    print(keypress)
print(len(result))