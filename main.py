import msgs
from classes import Box


def main():
    print('Welcome to box calculator 0.1')
    box = Box.create(msgs.BOX)
    box.get_packing()
    while True:
        box.resize(msgs.SAME_BOX)
        box.product.resize(msgs.SAME_PROD)
        box.get_packing()


if __name__ == '__main__':
    main()
