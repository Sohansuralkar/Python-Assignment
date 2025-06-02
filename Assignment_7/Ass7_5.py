#palindrome
word = input("pleae enter a string :")
flag = True
for i in range(len(word)):
    if word[i] != word [-(i+1)]:
        flag = False
if flag : 
    print("palindrome")
else:
    print("its not palindrome ")