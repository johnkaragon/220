from die import *

def main():
    playing = True
    while playing:

        d1 = Die(20)
        d1.roll()
        print(d1.get_value())

        stopping = input("hit enter to continue")
        playing = not stopping


if __name__ == "__main__":
    main()

