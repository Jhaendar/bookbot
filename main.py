import string


def main() -> None:
    FILE_PATH = "books/frankenstein.txt"

    contents = get_book_contents(FILE_PATH)

    word_count = count_words(contents)
    letter_count = count_letters(contents)

    report(FILE_PATH, word_count, letter_count)


def get_book_contents(file_path: str) -> str:
    with open(file_path) as file:
        file_contents = file.read()

    return file_contents


def count_words(text: str) -> int:
    return len(text.split())


def count_letters(text: str) -> dict[str, int]:
    freq: dict[str, int] = dict()
    for letter in text:
        if letter.isalpha() is False:
            continue

        letter = letter.lower()
        freq[letter] = 1 + freq.get(letter, 0)

    return freq


def report(filename, word_count, letter_freq):
    print(f"--- Begin report of {filename} ---")

    print(f"Word Count: {word_count}")
    print()

    print("Letter Frequency:")
    for letter, count in sorted(
        letter_freq.items(), key=lambda lf: lf[1], reverse=True
    ):
        print(f"  {letter}: {count:5}")


if __name__ == "__main__":
    main()
