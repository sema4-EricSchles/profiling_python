import requests
import random
from datetime import datetime
import pandas as pd
import numpy as np
import code

def get_alice_in_wonderland():
    response = requests.get("http://www.gutenberg.org/cache/epub/19033/pg19033.txt")
    return response.text

def inject_date(sentence):
    words = sentence.split(" ")
    index = random.randint(len(words))
    new_words = words[:index] + [str(datetime(1999, 9, 5))] + words[index:]
    return " ".join(new_words)
    
def generate_data(sentences, num_texts, with_dates=False):
    df = pd.DataFrame()
    texts = []
    for _ in range(num_texts):
        text = []
        size = int(np.random.normal(64, 68))
        for _ in range(size):
            sentence_choice  = random.choice(sentences)
            if with_dates:
                sentence_with_date = inject_date(sentence_choice)
                text.append(sentence_with_date)
            else:
                text.append(sentence_choice)
        texts.append(
            ".".join(text)
        )
    df["text"] = np.array(texts)
    return df

if __name__ == '__main__':
    text = get_alice_in_wonderland()
    sentences = text.split(".")
    df = generate_data(sentences, 5)
    code.interact(local=locals())
