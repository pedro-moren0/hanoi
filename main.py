import sys

from hanoi import hanoi


def main():
    for pair in hanoi(int(sys.argv[1])):
        print(f'({pair[0]}, {pair[1]})')


if __name__ == '__main__':
    main()
