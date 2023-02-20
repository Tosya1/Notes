import sys


class View:

    def get_value(msg):
        try:
            value = input(msg)
            return value
        except:
            sys.exit()

    def print_msg(msg):
        print(msg)
