"""Task 5
Use the text variable from the previous task. Create a regular expression to look for any word that starts with an upper case "B". Print the position (start- and end-position) of the first match occurrence.

Your result should look like this:
(0, 6)"""

# Solution 1
import re

# Use the text variable from the previous task
text = "Berlin is a city of culture."

# Search for the pattern using re.search()
match = re.search(r"\bB\w+", text)

# Check if a match is found
if match:
    start = match.start()
    end = match.end()
    print((start, end))
else:
    print(None)

print("_____________________________________________")

# Solution 2
import re

# Use the text variable from the previous task
text = "Berlin is a city of culture."

# Find all occurrences of words starting with an uppercase "B"
matches = re.finditer(r"\bB\w+", text)

# Get the position of the first match
first_match = next(matches)
start = first_match.start()
end = first_match.end()

# Print the position of the first match
print((start, end))

print("_____________________________________________")

# Solution 3
import re

# Use the text variable from the previous task
text = "Berlin is a city of culture."

# Search for the first occurrence of a word starting with an uppercase "B"
match = re.search(r"\bB\w+", text)

# Check if a match is found
if match:
    start = match.start()
    end = match.end()
    print((start, end))
else:
    print(None)
