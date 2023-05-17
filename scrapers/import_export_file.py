import sys


def arg_1():
    file_name = sys.argv[1]
    return file_name


def arg_2():
    file_name = sys.argv[2]
    return file_name


def arg_3():
    file_name = sys.argv[3]
    return file_name


def main():
    arg_1()
    arg_2()
    arg_3


if __name__ == "__main__":
    main()
