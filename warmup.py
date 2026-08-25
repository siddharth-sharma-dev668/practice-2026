import re
from collections import Counter
def most_common_word(text):
    words = re.findall(r"\b\w+\b",text.lower())
    if not words:
        return none
    counts = Counter(words)
    max_counts= max(counts.values())
    return min(word for word, count in counts.items() if counts == max_counts)