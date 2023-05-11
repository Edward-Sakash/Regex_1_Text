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

text = "Berlin is a city of culture."  # The text to search for the pattern
pattern = r"in"  # The pattern to search for

match = re.search(pattern, text)  # Search for the pattern in the text

if match:
    span = match.span()  # Get the span of the match
    matched_text = match.group()  # Get the matched substring
    output = f"<re.Match object; span={span}, match='{matched_text}'>"  # Format the output string
    print(output)  # Print the formatted output
