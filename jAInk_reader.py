import random

def prep_dataset(addr: str) -> dict:
    ### VARIABLES ###

    text = []
    wordlist = []
    chars = "\"\',?!.-"
    dataset = {'':[]}
    count = 0
    safety = 1
    # Loading the text file
    with open(addr) as t:
        text = t.readlines()
        t.close()

    # Extracting every word from the text and formatting it 
    for i in range(len(text)):
        wordlist.extend(text[i][4:-2].split())
    
    # this is if I want to take out any punctuation
    # for p in range(len(wordlist)):
    #     for character in chars:
    #         if character in wordlist[p]:
    #             wordlist[p] = wordlist[p].replace(character, '')


    # Make the dataset
    for w in range(len(wordlist)):
        if wordlist[w] in dataset and safety < (len(wordlist)-2):
            dataset[wordlist[w]].append(wordlist[safety])
        else:
            if safety < (len(wordlist)-2):
                dataset[wordlist[w]] = [wordlist[safety]]
        safety +=1
    
    return dataset

def randomize(dataset: dict) -> list[int,str]:
    dkeys = list(dataset.keys())
    key = dkeys[random.randint(0, len(dkeys)-1)]
    value = dataset[key][random.randint(0, len(dataset[key])-1)]
    paragraph = ''
    count = 0 #The count for the paragraph length
    while count <= 100:
        paragraph += " " + value
        key = value
        value = dataset[key][random.randint(0, len(dataset[key])-1)]
        count += 1
    paragraph += "..."
    return([count, paragraph])

def switch(key, value):
    key = value
    return key

if __name__ == '__main__':
    set = prep_dataset('YOUR_PATH')
    story = randomize(set)
    print("count: {} \n{}".format(story[0]-1, story[1]))
