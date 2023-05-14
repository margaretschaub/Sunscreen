def output_file_path():
    while True:
        try:
            output_file = input("Output file name: ")
            return output_file
        except FileNotFoundError:
            print("No such file or directory. Please try again.")


def input_file_path():
    while True:
        try:
            input_file = input("Input file name: ")
            return input_file
        except FileNotFoundError:
            print("No such file or directory. Please try again.")


def main():
    output_file_path()
    input_file_path()


if __name__ == "__main__":
    main()
