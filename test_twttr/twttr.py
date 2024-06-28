def main():
    user_input = input("Input: ")
    print(shorten(user_input))          #whatever is returned, print it


def shorten(word):
    for c in word:
        if c in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:  #also could do "AEIOUaeiou"
            word = word.replace(c, "")
    #print("Output: " + word)                  #there isnt a return value here, it wont work for the test since nothing is returned
    return f"Output: {word}"                    #return this string


if __name__ == "__main__":
    main()
