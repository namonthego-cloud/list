#function to whether
#first and last charecter of words match
def match_words(words):
    ctr =0
    lst = []
    for word in words:
        if len(word)> 1 and word[0] == word[-1]:
            ctr += 1
            lst. append(word)


    print("list of words with first and last charater same\n",lst)
    return ctr

count = match_words (['abc','ckc','xue','aba','1321'])
print("number of words having first and last character same:",count)

            
