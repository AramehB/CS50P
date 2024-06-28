_ = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
ans = "Yes" if _ == "42" or _ == "forty-two" or _ == "forty two" else "No"
print (ans)
