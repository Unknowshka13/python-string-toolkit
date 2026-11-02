
def count_words(text):
  #splits the text into words and return their count
    words = text.split()
    return len(words)


def normalize_whitespace(text):
    # Replace multiple whitespace characters with a single space
    return " ".join(text.split())
