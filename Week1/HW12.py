num = int(input())

print("The next number for the number", num, "is", (num + 1),
      sep=" ", end="")    # E501 line too long (82 > 79 characters)
print(".")
print("The previous number for the number", num, "is", (num - 1),
      sep=" ", end="")
print(".")
