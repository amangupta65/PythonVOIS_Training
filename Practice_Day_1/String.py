#1
s = "Hello123@#"

vowels = consonants = digits = special = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)

#2
s = "Hello World Python"
words = s.split()
result = []

for word in words:
    result.append(word[::-1])

print(" ".join(result))

#3
s = "malyalam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#4
s = "python"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

#5
s = "Python"
s[0] = "J"

# try except
s = "Python"

try:
    s[0] = "J"
except TypeError as e:
    print("Error:", e)

 
