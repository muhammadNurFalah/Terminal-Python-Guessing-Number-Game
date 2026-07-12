import time

def loading_efect() -> None:
    text: str = "Deciding the number"

    for i in range(6):
        print(text + "." * (i % 3 + 1))
        time.sleep(0.6)

def main() -> None:
    #Test the functions here!
    loading_efect()

if __name__ == "__main__":
    main()
