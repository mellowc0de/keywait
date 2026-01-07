class KEYWAIT:
    @staticmethod
    def wait_for_key():
        while True:
            user_process_input = input("(c)ontinue or (q)uit...").strip().lower()

            if user_process_input == "c":
                return
            elif user_process_input == "q":
                exit()
            else:
                print("Invalid input. Please enter a valid option.")

