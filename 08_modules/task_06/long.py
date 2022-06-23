

txt = 'bannannannannnaaaaa'
new = list(txt)
longest_word = ''
word = ''

for i in range(0,len(new)):
    if i == len(new)-1:
        word+=new[-1]
        break
    if new[i] == new[i+1]:
        word+=new[i]

print(word)