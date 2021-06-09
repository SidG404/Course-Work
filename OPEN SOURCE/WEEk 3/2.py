
import textwrap, sys

if len(sys.argv) != 3:
    print("invalid arguments")
else:
    file, length = sys.argv[1:3]
    f = open(file, 'r')
    s = f.read()
    s = textwrap.wrap(s, int(length))
    f.close()
    s = "\n".join(s)+'\n'
    f = open(file, 'w')
    f.write(s)
    f.close()
    print("text wrap completed")