import random

data = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
data_list = data.split()
for word in data_list:
    if len(word) > 4:
        target = word[1:-1]
        target = ''.join(random.sample(target, len(target)))
        word = word[0] + target + word[-1]
        print word,
    else:
        print word,


        
