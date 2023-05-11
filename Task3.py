"""Task 3
Create a variable called text to store the data: Berlin is a city of culture. . Replace the spaces with a hyphen.

Your result should look like this:
Berlin-is-a-city-of-culture."""

# Solution 1
# Define the input text
text = "Berlin is a city of culture."

# Replace spaces with hyphens
modified_text = text.replace(" ", "-")

# Print the modified text
print(modified_text)

print("___________________________________________")

# Solution 2
import re

# Define the input text
text = "Berlin is a city of culture."

# Replace spaces with hyphens using re.sub()
modified_text = re.sub(r"\s", "-", text)

# Print the modified text
print(modified_text)
