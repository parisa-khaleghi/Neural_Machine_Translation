import random

# Function to read the files and pair sentences
def read_and_pair_sentences(en_file, fr_file):
    with open(en_file, 'r', encoding='utf-8') as file_en, open(fr_file, 'r', encoding='utf-8') as file_fr:
        lines_en = file_en.readlines()
        lines_fr = file_fr.readlines()

    paired_sentences = list(zip(lines_en, lines_fr))
    return paired_sentences

# Function to split the dataset and save to files
def split_and_save_dataset(paired_sentences, save_path, train_size=0.6, val_size=0.2):
    # Shuffle the dataset
    random.shuffle(paired_sentences)

    # Calculate split sizes
    total_size = len(paired_sentences)
    train_split = int(total_size * train_size)
    val_split = int(total_size * (train_size + val_size))

    # Splitting the dataset
    train_data = paired_sentences[:train_split]
    val_data = paired_sentences[train_split:val_split]
    test_data = paired_sentences[val_split:]

    # Save function
    def save_data(data, file_name):
        with open(f'{save_path}/{file_name}', 'w', encoding='utf-8') as file:
            for en, fr in data:
                file.write(f'{en.strip()}\t{fr.strip()}\n')

    # Save the splits to separate files
    save_data(train_data, 'train.txt')
    save_data(val_data, 'val.txt')
    save_data(test_data, 'test.txt')

    print("Datasets saved to:", save_path)

# File paths
en_file = 'fr-en/europarl-v7.fr-en.en'
fr_file = 'fr-en/europarl-v7.fr-en.fr'
save_path = 'fr-en'

# Read, pair, and split the dataset
paired_sentences = read_and_pair_sentences(en_file, fr_file)
split_and_save_dataset(paired_sentences, save_path)
