"""Task 2
Create a variable called text to store the data: Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital. . Then search for the word Frankfurt in the string .

Your result should look like this:
None"""

# Solution 1
import re

# Define the input text
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

# Search for the word "Frankfurt" in the text
match = re.search(r"Frankfurt", text)

# Check if a match is found
if match:
    print(match.group())
else:
    print(None)

print("_________________________________________________")

# Solution 2
# Define the input text
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

# Check if "Frankfurt" is present in the text
if "Frankfurt" in text:
    print("Frankfurt")
else:
    print(None)

print("_________________________________________________")

# Solution 3
import re

# Define the input text
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

# Find all occurrences of "Frankfurt" in the text
matches = re.findall(r"Frankfurt", text)

# Check if any matches are found
if matches:
    print(matches)
else:
    print(None)

