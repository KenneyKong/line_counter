import sys

def count_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            count = 0

            for line in lines:
                line = line.strip()  # Remove leading and trailing whitespace
                if line and not line.startswith("#"):
                    count += 1

            return count
    except FileNotFoundError:
        print("File not found.")
        sys.exit()

def main():
    if len(sys.argv) != 2:
        print("Usage: python lines.py filename.py")
        sys.exit()

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        print("Please provide a valid Python file.")
        sys.exit()

    num_lines = count_lines(filename)
    print(f"Number of lines of code (excluding comments and blanks): {num_lines}")

if __name__ == "__main__":
    main()


# run the code in the terminal: python lines.py filename.py
