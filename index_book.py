def print_index(input):
    word_frequency = {}
    index = {}
    for key, val in input.items():
        for word in val.split():
            words = index.keys()
            if word not in words:
                index[word] = [key]
                word_frequency[word] = 1
            else:
                index[word].append(key)
                word_frequency[word] += 1
    print(index)
    print(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))

print_index({1: "harry potter is a wizard from Hogwartz",
2: "Dinosaurs fly in fairytales"})
