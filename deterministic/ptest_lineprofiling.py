import time


@profile
def fast():
    print("Я быстрая функция")


@profile
def slow():
    time.sleep(3)
    print("Я очень медленная функция")


@profile
def medium():
    time.sleep(0.5)
    print("Я средняя функция...")


def main():
    fast()
    slow()
    medium()


if __name__ == "__main__":
    main()
