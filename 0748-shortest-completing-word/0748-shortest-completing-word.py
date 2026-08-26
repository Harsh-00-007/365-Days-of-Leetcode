from collections import Counter


class Solution:

  def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
    # Extract only the letters and convert to lowercase
    plate_counts = Counter(c.lower() for c in licensePlate if c.isalpha())

    shortest = None

    for word in words:
      word_counts = Counter(word)

      # Check if the word contains at least the required counts for each letter
      if all(word_counts[char] >= count for char, count in plate_counts.items()):
        if shortest is None or len(word) < len(shortest):
          shortest = word

    return shortest