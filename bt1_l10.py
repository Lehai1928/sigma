from collections import Counter
import string

text = input("nhap chu:")
text =text.lower()
filter_text = [char for char in text if char in string.ascii_lowercase]

counter = Counter(filter_text)

for char, count in sorted(counter.items()):
    print(f"{char}: {count}")