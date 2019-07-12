import sys
import argparse

parser = argparse.ArgumentParser(description="Test out command line scripts")

args = parser.parse_args()


parser.add_argument_group('-h', '--help', type=str, help='Ask for Help')

parser.add_argument_group('-h', '--help', type=str, help='Ask for Help')


print('the name of this file is: ' + sys.argv[0])


def command_line(**args):
    # if len(sys.argv) > 0:
    pass


if __name__ == '__main__':
    print(command_line(**args))
