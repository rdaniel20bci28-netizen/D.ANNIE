def longest_word(s):
    return max(s.split(), key=len,default="")
print(longest_word("civil engineering"))
