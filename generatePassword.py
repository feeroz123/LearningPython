# Write a password generator in Python. Strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

import random
import string

rand_lowerchar = random.choice(string.ascii_lowercase)     # generating one random value out of ascii lower case letters
rand_upperchar = random.choice(string.ascii_uppercase)     # generating one random value out of ascii lower case letters
rand_int = str(random.randint(0, 9))                        # generating one random value out of integers between 0 and 9, both inclusive
rand_digits = random.choice(string.digits)                  # generating one random value out of string of digits
rand_splchars = random.choice(string.punctuation)           # generating one random value out of special characters

# Generating password of length 8
print("".join(rand_lowerchar * 2 + rand_digits * 2 +rand_upperchar * 2 + rand_int * 2 + rand_splchars * 2))

# OR
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    print(''.join(random.choice(chars) for x in range(size)))

random_generator()
random_generator(3, "6793YUIO")