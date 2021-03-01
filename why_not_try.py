import sys
from time import sleep
indent_increase = True
indent = 0
try:
    while True:
        print(" " * indent, end = "")
        print("*" * 10)
        sleep(0.1)
        if indent_increase:
            indent += 1
            if indent == 25:
                indent_increase = False
        else:
            indent -= 1
            if indent == 0:
                indent_increase = True
except KeyboardInterrupt:
    sys.exit()
