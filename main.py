from IntToString import numberToWords
import sys


def convert_input():
    # for i in sys.argv[1:]:
    #     try:    # check for input
    #         num = int(i)
    #     except ValueError:
    #         print("please type an integer")
    #         return
    #     s = numberToWords(num)
    #     print("Integer: {} --> English: ".format(num) + s)

    val = input("please type an integer:(Ctrl+C to stop) ")
    try:    # check for input
        num = int(val)
    except ValueError:
        print("error input\n")
        return
    s = numberToWords(num)
    print("Input: {} --> English: ".format(num) + s + "\n")


if __name__ == '__main__':
    # convert_input()
    while True:
        convert_input()