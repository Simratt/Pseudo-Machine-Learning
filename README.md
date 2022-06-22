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

After running, you should get something like this!

## License
[MIT](https://choosealicense.com/licenses/mit/)
