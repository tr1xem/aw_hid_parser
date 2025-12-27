import sys
from extract import extract_hid_bytes


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    extract_hid_bytes(filename)


if __name__ == "__main__":
    main()
