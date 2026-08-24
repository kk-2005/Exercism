def add_prefix_un(word):
    str1="un"+word
    return str1
    pass


def make_word_groups(vocab_words):
    if not vocab_words:
        return ""
    if len(vocab_words) == 1:
        return vocab_words[0]
    remaining = [vocab_words[0] + word for word in vocab_words[1:]]
    return " :: ".join([vocab_words[0]] + remaining)
    pass


def remove_suffix_ness(word):
    if word.endswith("ness"):
        str1 = word.removesuffix("ness")
    else:
        str1 = word
    if str1.endswith("i"):
        return str1[:-1] + "y"
        
    return str1



def adjective_to_verb(sentence, index):
    words = sentence.split()
    target_word = words[index]
    cleaned_word = target_word.rstrip(".,?!;:")
    return cleaned_word + "en"

    pass
