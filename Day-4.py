# PYTHON'S BUILT-IN DATA TYPES

# 1. Numbers: int and float

age = 40 # int
temparature = 20.1 # float type

# Static vs. Dynamic Typing
# Java (example - for comparison)
# int age;
# age = 40

# 2. Booleans: Logical values => True or False

print(age == 40)
print(age < 30)

# 3. Strings: Ordered sequences of characters, stored in UTF-8 encoding.

model_name = "Gemini" # ""

# 4. List: Ordered, mutable sequences of objects.
person = ['RNS', 13, True, 34.8, 'Address', 13]

# 5. Tuple: Ordered, immutable sequences of objects.
coordinates = (40.3, 54.7) # Latitude and Longitude

# 6. Sets: Mutable collections of unordered, unique objects.
ip_addresses = {'100.0.0.1', '80.1.1.2', '5.6.1.4'}

# 7. Dictionary: Collections of unordered key-value pairs
employees = {'name': 'Rns', 'age': 40, 'is_permanent': True}
print(employees['name'])


# -----------------------------------------------------------------------------------

# Numbers and Math Operators in Python

# -----------------------------
# 1. Basic Arithmetic Operators
# -----------------------------

# Addition (+) and Subtraction (-)
print(10 + 12)
print(12 - 10)

# Multiplication (*)
print(10 * 3)

# Division (/): Always returns float
print(9 / 2)

# Division (//): Rounds down to the nearest whole number
print(9 // 2)

# Multiplication with float values
print(5 * 2.0)

# Exponentiation (**): Raises a number to a power
print((2 ** 3) ** 3)

# Modulus (%): Returns the remainder of a division
print(5 % 5)

# -----------------------------
# 3. Operator Precedence
# -----------------------------
print((2 + 4) * 2 ** 3)

