# PYTHON STRING BASICS

# Defining string variables (use '' or "" but stay consistent)
model_summary = 'This AI model predicts stock trends.'
prediction_message = "AI will revolutionize industries!"

# Printing a basic string
print(model_summary)

# Example of using special characters in strings
feedback = 'Press the # button to continue.'

# Demonstrating escape characters for single quotes
print('AI says, I\'m here to assist you.')
print("AI says, I'm here to assist you.")

# Using a multi-line string
ai_response = '''Hello there!
I’m an AI here to help.
Feel free to ask me anything.
'''
print(ai_response)

# Using `\n` for multi-line text representation
ai_prompt = 'Welcome to AI Bot\nYour virtual assistant\nHere to assist with all things tech!'
print(ai_prompt)

# Demonstrating the use of escape character `\`
print('\\ is essential for handling escape characters in Python.')

# Using a backslash `\` to split a long string across multiple lines
gen_ai_message = 'Generative AI has revolutionized the way we create, ' \
                 'from text generation to image synthesis. It is like having a creative partner!'
print(gen_ai_message)

# Printing non-English text
print('こんにちはPython！')  # This says 'Hello Python!' in Japanese

# Printing an emoji for fun. Python strings are UTF-8 encoded.
print('🤖')

# ----------------------------------------------------------------------------------------------

# GETTING USER INPUT

# BASIC USER INPUT

# Prompt the user to ask a question
# command = input('Ask your AI assistant a question: ')
# print('Your question was:', command)

# USER INPUT RETURNS A STRING

training_hours = input('Enter hours spent training the model: ')

# Demonstrate that `input()` always returns a string
print('Data type of training_hours:', type(training_hours))  # Output: <class 'str'>

# CONVERTING USER INPUT TO NUMERIC TYPES

iterations = int(input('Enter the number of model iterations: '))
datasets = int(input('Enter the number of datasets: '))

total = iterations * datasets
print('Total processing units:', total)

# -------------------------------------------------------------------------------------------

# CORE STRING OPERATIONS: INDEXING, SLICING, CONCATENATING

message = 'GenAI is amazing!'

# INDEXING: Accessing individual characters in a string
print(message[0])    # First character: 'G'
print(message[5])    # Sixth character: 'i'
print(message[-1])   # Last character: '!'
print(message[-7])   # Seventh character from the end: 'a'

# Get the length of the string
n = len(message)
print(n)             # Output: 16 (total characters in 'GenAIis amazing!')

# Access the last character using length
print(message[n-1])  # Equivalent to message[-1]

# STRINGS ARE IMMUTABLE
# message[0] = 'X'  # Uncommenting this line will cause an error

# STRING CONCATENATION

greeting = 'Hello, '
role = 'AI enthusiast'

# Combining strings using `+`
print(greeting + role + '!')  # Output: 'Hello, AI enthusiast!'

# Concatenating strings with different data types (requires type conversion)
print('Version ' + str(4.0))  # Output: 'Version 4.0'

# STRING REPETITION

separator = '??'

# Repeating a string multiple times
print(separator * 5)  # Output: '??????????'

# STRING SLICING

tech = 'Machine Learning'

# Extracting a substring using slicing: string[start:stop]
print(tech[0:7])   # 'Machine' (characters from index 0 to 6)

# Demonstrating different slicing variations

# string[start:stop:step]

print(tech[:7])    # 'Machine' (from the start up to index 6)
print(tech[8:])    # 'Learning' (from index 8 to the end)
print(tech[-4:])   # 'ning' (last four characters)
print(tech[8:100]) # 'Learning' (Python doesn't throw an error if stop exceeds length)
print(tech[0:14:2])# 'McieLann' (every second character)
print(tech[::-1])  # 'gninraeL enihcaM' (reversed string)

# -------------------------------------------------------------------------------------------

# COMMON STRING METHODS

# Demonstrating type checking for an integer and a string
x = 10
s = 'abc'
print(type(x), type(s))  # Output: <class 'int'> <class 'str'>

# STRING CASE CONVERSIONS

model_output = 'ai IS the future of everything!'

# Convert the string to uppercase
print(model_output.upper())  # 'AI IS THE FUTURE OF EVERYTHING!'

# Convert the string to lowercase
print(model_output.lower())  # 'ai is the future of everything!'

# The original string remains unchanged (strings are immutable)
print(model_output)  # 'ai IS the future of everything!'

# STRING STRIPPING

response = ' ?? Hello, human! ?? '

# Remove leading and trailing whitespace characters
print(response.strip())  # '?? Hello, human! ??'

# Remove specific leading and trailing characters (' ??')
print(response.strip(' ??'))  # 'Hello, human!'

# STRING REPLACEMENT

text = 'ML is a critical component of modern AI. ML techniques are advancing rapidly.'

# Replace occurrences of 'ML' with 'machine learning'
updated_text = text.replace('ML', 'machine learning')
print(updated_text)
# 'machine learning is a critical component of modern AI. machine learning techniques are advancing rapidly.'

# STRING COUNTING

text = 'AI is the FUture. Embrace the future of AI!'

# Count occurrences of 'future' (case-insensitive)
print(text.lower().count('future'))  # Output: 2

# STRING SPLITTING

statement = 'AI breakthrough at every step'

# Split the string into a list of words
words = statement.split()
print(words)  # ['AI', 'breakthrough', 'at', 'every', 'step']

# STRING JOINING

terms = ['AI', 'ML', 'GenAI', 'LLM', 'NLP']

# Join the list elements into a single string, separated by ', '
buzzwords_string = ', '.join(terms)
print(buzzwords_string)  # 'AI, ML, GenAI, LLM, NLP'

# STRING PREFIX AND SUFFIX REMOVAL (Python 3.9+)

url = 'https://example.com'

# Remove 'https://' from the beginning of the URL
cleaned_url = url.removeprefix('https://')
print(cleaned_url)  # 'example.com'

filename = 'state_of_ai_2025.pdf'

# Remove '.pdf' from the end of the filename
cleaned_filename = filename.removesuffix('.pdf')
print(cleaned_filename)  # 'state_of_ai_2025'

# USING HELP TO VIEW DOCUMENTATION

# Display available string methods and documentation
# help(str)

# Display help information for the `strip()` method
help(str.strip)

# ------------------------------------------------------------------------

# FORMATTED STRINGS: USING F-STRINGS FOR CLEAN OUTPUT

# STRING CONCATENATION (LESS EFFICIENT)
model_name = 'GPT'
version = 4

# Traditional concatenation (requires explicit type conversion)
print('Hello from ' + model_name + '-' + str(version) + '!')

# USING F-STRINGS (MORE READABLE & EFFICIENT)

# The f-string automatically converts variables to strings
print(f'Hello from {model_name}-{version}!')
# Output: Hello from GPT-4!

# FORMATTING NUMBERS WITH F-STRINGS

token_used = 123
cost_per_token = 0.001

# Formatting a floating-point number to 4 decimal places
total_cost = f'{token_used * cost_per_token}'
print(f'Total cost for this message: {total_cost}')
# Output: Total cost for this message: 0.1230

# INLINE VARIABLE DISPLAY USING F-STRINGS (Python 3.8+)

learning_rate, epochs = 0.01, 10

# The `=` syntax displays both the variable name and its value
print(f'Learning rate: {learning_rate=}, Epochs: {epochs=}')
# Output: Learning rate: learning_rate=0.01, Epochs=10

# CALCULATING AND FORMATTING PRECISION

true_positive = 42
false_positive = 8

# Compute precision and format it to 3 decimal places
precision = true_positive / (true_positive + false_positive)
print(f'Precision: {precision=:.3f}')
# Output: Precision: precision=0.840

# ---------------------------------------------------------------------------
