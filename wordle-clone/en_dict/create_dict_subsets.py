# create_dict_subsets.py
# Source: https://github.com/dwyl/english-words?tab=readme-ov-file


import pathlib

from string import ascii_letters

EN_DICT_PATH = pathlib.Path(__file__).parent / "words_alpha.txt"

def main():
    for word_length in range(1, 46):
        file_name = f"{word_length}_letter_words.txt"
        print(f"Generating '{file_name}'...")
        out_path = pathlib.Path(file_name)
        words = sorted(
            {
                word.lower()
                for word in EN_DICT_PATH.read_text(encoding="utf-8").split()
                if len(word) == word_length and all(letter in ascii_letters for letter in word)
            },
            key=lambda word: (len(word), word),
        )

        out_path.write_text("\n".join(words))
    
    print("\nDone.\n")


if __name__ == "__main__":
    main()
