import re
def func_longest_word(text):
     cleaned_text = re.sub(r'[^\w\s]', '', text)
     x = cleaned_text.split(" ")
     longest = ''
     for i in x:
        if len(i) > len(longest):
            longest = i
     return longest
print(func_longest_word("The heaven cannot brook two suns nor the earth two rajnikanths"))