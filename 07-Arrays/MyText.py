# MyText module
def word_count(text):
    """Returns the number of words in the text."""
    return len(text.split())

def words_by_length(text):
    """Returns an ordered array of words, from longest to shortest."""
    words = text.split()
    return sorted(words, key=len, reverse=True)

def words_alphabetically(text):
    """Returns an alphabetically ordered array of words."""
    words = text.split()
    return sorted(words, key=str.lower) 