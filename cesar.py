#python, 3 

# Шифрование
# ord("A") = 65; chr(65) = "A"
word = "To decrypt a ciphertext, go from the inner circle to the outer circle. Let’s say you receive this ciphertext from a friend, “Iwt ctl ephhldgs xh Hldgsuxhw.” You and everyone else won’t be able to decrypt it unless you know the key (or unless you are a clever hacker). But your friend has decided to use the key 15 for each message she sends you. \n" + \
"Line up the letter A on the outer circle (the one with the dot below it) over the letter on the inner circle that has the number 15 (which is the letter P). The first letter in the secret message is I, so we find I on the inner circle and look at the letter next to it on the outer circle, which is T. The W in the ciphertext will decrypt to the letter H. One by one, we can decrypt each letter in the ciphertext back to the plaintext, “The new password is Swordfish.”"
shift = 3

chipher_text = []
for i in word:
    if i.isupper():
        ind = ord(i) - ord("A")
        if ind + shift >= 26: 
            ind = ind + shift - 26
        else: 
            ind = ind + shift
        chipher_text.append(chr(ind + ord("A")))
    elif i.islower(): 
        ind = ord(i) - ord("a")
        if ind + shift >= 26: 
            ind += shift - 26
        else: 
            ind += shift
        chipher_text.append(chr(ind + ord("a")))
    else:
        chipher_text += i

print(chipher_text)

with open("chipher.txt", "w") as f:
    f.write("".join(chipher_text))

# word = []
# for i in chipher_text:
#     if i.isupper():
#         ind = ord(i) - ord("A")
#         if ind - shift < 0:
#             ind = 26 + ind - shift
#         else:
#             ind = ind - shift
#         word.append(chr(ind + ord("A")))
#     elif i.islower():
#         ind = ord(i) - ord("a") 
#         if ind - shift < 0:
#             ind = 26 + ind - shift
#         else:
#             ind = ind - shift
#         word.append(chr(ind + ord("a")))

# print("".join(word))
        