"""Task 4
Create a variable called text to store the data: Berlin is a city of culture. . Search if the phrase in appears inside the string. Print the output of the regex function.

Your result should look like this:
<re.Match object; span=(4, 6), match='in'>"""

# Solution 1
import re

# Define the input text
text = "Berlin is a city of culture."

# Search for the phrase "in" in the text
match = re.search(r"in", text)

# Print the output of the regex function
print(match)

print("_____________________________________________")

# Solutin 2
import re

# Define the input text
text = "Berlin is a city of culture."

# Find all occurrences of the phrase "in" in the text
matches = re.finditer(r"in", text)

# Print the output of the regex function
for match in matches:
    print(match)

print("______________________________________________")


# Solution 3
import re

text = "Berlin is a city of culture."
pattern = r"in"

match = re.search(pattern, text)

if match:
    print(f"<re.Match object; span={match.span()}, match='{match.group()}'>")
