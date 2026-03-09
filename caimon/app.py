from guide import get_response

def main():
    print("\nPrititit! Kamusta? I'm CAIMON and welcome to the Basilica Minore del Santo Niño de Cebu!\n"
          "What would you like to learn more about the Basilica?\n"
          "Feel free to ask me anything about its history, traditions, and significance.\n"
          "If you want to exit, just type 'exit' or 'quit'.\n"
          "PIT SENYOR!")

    while True:
        user_input = input("\nYOU: ")

        if user_input.lower() == "exit":
            print("\nCAIMON: Pit Señor! Safe travels and God bless.\n")
            break

        reply = get_response(user_input)
        print(f"\nCAIMON: {reply}\n")

if __name__ == "__main__":
    main()