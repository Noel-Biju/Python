string=input("Enter a string:")
vowels="aeiouAEIOU"
vowel_count=0
count=0
for char in string:
    if char in vowels:
        vowel_count+=1
    else:
        count+=1
print("The no of vowels in string is",vowel_count)
print("The no of consonants in string is",count)
