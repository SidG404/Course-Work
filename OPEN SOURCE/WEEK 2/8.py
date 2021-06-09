f = open("file.txt", 'r')
lines = f.readlines()

for line in range(-1, -len(lines)-1, -1):
    print(lines[line].rstrip('\n'))