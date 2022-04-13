def word_sort(tup):
    return tup[1]

def count(filename):
    file = open(filename, "r")
    text = file.read()
    file.close()
    text = text.lower()
    punc = "`~,./;''[]{}:\"<>?\"!@$%&-"
    for ch in punc:
        text.replace(ch, " ")
    words = text.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    counts_list = list(counts.items())
    counts_list.sort(key=word_sort)


if __name__ == "__main__":
    count("Alice.txt")
