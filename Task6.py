"""Task 6
Create a variable called text to store the data: The rain in Spain.. Count how many times the subphrase ai appears in the string. Print the results on the screen.

Your result should look like this:
2"""

# Solution 1
import re

# Define the input text
text = "The rain in Spain."

# Count the occurrences of the subphrase "ai"
matches = re.findall(r"ai", text)
count = len(matches)

# Print the count
print(count)

print("_________________________________________________")

# Solution 2
import re

# Define the input text
text = "The rain in Spain."

# Count the occurrences of the subphrase "ai"
matches = re.finditer(r"ai", text)
count = 0

# Iterate over the matches and increment the count
for match in matches:
    count += 1

# Print the count
print(count)

print("_________________________________________________")

# Solution 3
import re

# Define the input text
text = "The rain in Spain."

# Count the occurrences of the subphrase "ai"
count = len(re.findall(r"ai", text))

# Print the count
print(count)

print("_________________________________________________")

# Solution 4
import re

# Define the input text
text = "The rain in Spain."

# Count the occurrences of the subphrase "ai"
count = len(re.findall(r"ai", re.sub(r"(ai)", r"\1", text)))

# Print the count
print(count)

