def turnCalc(word):
    turn_word = []
    if not word.isnumeric():
        print("Please enter a number")
        return
    for i in range(len(word)):
        if word[i] == "1":
            turn_word.append("I")
        elif word[i] == "2":
            turn_word.append("Z")
        elif word[i] == "3":
            turn_word.append("E")
        elif word[i] == "4":
            turn_word.append("H")
        elif word[i] == "5":
            turn_word.append("S")
        elif word[i] == "6":
            turn_word.append("G")
        elif word[i] == "7":
            turn_word.append("L")
        elif word[i] == "8":
            turn_word.append("B")
        elif word[i] == "9":
            turn_word.append("-")
        elif word[i] == "0":
            turn_word.append("O")
    secret_word = "".join(turn_word)
    secret_word_reverse = secret_word[::-1]
    print(f"Secret word: {secret_word_reverse}")

secret_word = input("Enter a number: ")
turnCalc(secret_word)
 
#  The above script will take a number as input and convert it into a word. 
#  The script is simple and easy to understand. 
#  Let’s run the script and see the output. 
#  python script.py