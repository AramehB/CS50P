_ = input("Input: ")
for c in _:
    if c in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:  #also could do "AEIOUaeiou"
        _ = _.replace(c, "")
print("Output: " + _)
