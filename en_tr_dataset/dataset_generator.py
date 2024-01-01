from tatoebatools import ParallelCorpus
import pandas as pd
dataset = []
for sentence, translation in ParallelCorpus("eng", "tur"):
    dataset.append({
        "text": sentence.text,
        "translation": translation.text
    })
data = pd.DataFrame(dataset)
data.to_csv("eng_tur_translation_dataset.csv")



