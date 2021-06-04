f = open("file.txt", 'r')
lines = f.readlines()

for line in lines:
    words = line.split()
    print(*words[::-1])