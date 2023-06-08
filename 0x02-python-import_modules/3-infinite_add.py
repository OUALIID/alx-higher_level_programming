#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    resalt = 0
    for i in range(1, len(argv)):
        resalt += int(argv[i])
    print("{}".format(resalt))


if __name__ == "__main__":
    main()
