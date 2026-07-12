#!/usr/bin/python3
if __name__ == "__main__":
    hidden_4 = __import__("hidden_4")

    for name in sorted(dir(hidden_4)):
        if name[:2] != "__":
            print(name)
