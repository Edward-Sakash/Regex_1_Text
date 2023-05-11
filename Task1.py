"""String Regex 1
Python Regex
In this exercise, we will focus on the use and manipulation of text in Python, including:

Using the Python regex
Creating custom regex patterns"""

# Task 1
# Solution 1
import re

# Define the input text
text = "Berlin is a world city of culture, politics, media and science."

# Search for the first occurrence of a white space character in the text
match = re.search(r"\s", text)

# Check if a match is found
if match:
    # Print the position of the match
    print("The first white-space character is located at position:", match.start())

print("__________________________________________________")

# Solution 2
import re

# Define the input text
text = "Berlin is a world city of culture, politics, media and science."

# Use re.sub() to replace the first white space character with a unique marker
modified_text = re.sub(r"\s", "*", text, count=1)

# Find the position of the unique marker in the modified text
position = modified_text.find("*")

# Print the position of the first white space character
print("The first white-space character is located at position:", position)
