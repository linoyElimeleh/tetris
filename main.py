from datetime import datetime

from tetris_engine import tetris_engine


def main():
    output_file_name = 'output_files/' + str(datetime.now()) + '_output.txt'
    tetris_engine('input.txt', output_file_name)


if __name__ == "__main__":
    main()
