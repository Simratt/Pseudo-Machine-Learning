# "Jainky" Random  Story Generator

The algorithm uses a python dictionary in which the keys are a set of all the unique words that exist in the story and the values are a list of every possible word that comes after each key. Then, looping through the dictionary, it creates a story of ```n``` specified words

## Installation

```bash
git clone https://github.com/Simratt/Pseudo-Machine-Learning.git
cd Pseudo-Machine-Learning

```

## Usage
Open a python env, you can follow [the docs](https://docs.python.org/3/tutorial/venv.html) to setup an environment if not setup from before. In the ```jAInk_reader.py```, change the ```YOUR_PATH``` input to the path to the sample .txt file in the folder or any other file. 

```python
if __name__ == '__main__':
    set = prep_dataset('FILE_PATH') -> '.../shakespeare.txt'
    story = randomize(set)
    print(story) 

```
You can also change the ```count``` variable to change the length of the paragraph 

```python
def randomize(dataset: dict) -> str:
    dkeys = list(dataset.keys())
    key = dkeys[random.randint(0, len(dkeys)-1)]
    value = dataset[key][random.randint(0, len(dataset[key])-1)]
    paragraph = ''
    count = 0 #The count for the paragraph length
    while count <= 50:
        paragraph += " " + value
        key = value
        value = dataset[key][random.randint(0, len(dataset[key])-1)]
        count += 1
    paragraph += "..."
    return(paragraph)
```
After running, you should get something like this!


```
count: 50
this place thou filch'd my gracious duke This man hath no eyes are but your father's house remote seven leagues And by Cupid's strongest bow By the next new moon- The jaws of any dream away our nuptial and on you your fancies to say 'Behold! The course of THESEUS Enter...
```
Of course, the result is according to the inputted story, here I have inputted A Midsummer Night's Dream. Here is some Sherlock Holmes

```
count: 50
cloud from under any other of Cassel-Felstein, and do not take it is indeed committed a note itself. What do yo alone. I should marry anothe woman, there are of a small "t" woven into his whole appearance. He took down in my trifling experiences, you a Hebrew rabbi and he...

count: 100
 which must pay. It i means? "I am lost without putting myself is herself the 'Eg.' Le us your practice, if a half a long, nervous hands together "It came home in Scarlet, I should much prefer to Mar Jane, she will find me in this." H threw across the royal brougham and limbs of the photograph. "Oh, dear! That is true that photograph. "Oh, dear! That is no doubt depicted to it t introduce a distracting factor which would, in this mask," continued our doubts. As I rose to consult you that you are. I rang the stud of the...
 ```
 
Have fun!

## License
[MIT](https://choosealicense.com/licenses/mit/)
