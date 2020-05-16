from pyfirmata import Arduino, util, INPUT

PIN = 0

board = Arduino('/dev/ttyACM0')
board.analog[PIN].mode = INPUT


def main():
    """ Main function"""
    it = util.Iterator(board)
    it.start()
    board.analog[PIN].enable_reporting()
    while True:
        value = board.analog[PIN].read()
        print(value)


if __name__ == "__main__":
    main()
