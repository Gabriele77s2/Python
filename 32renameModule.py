# Creating a random user password
from string import punctuation, ascii_letters, digits
import random

symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()

password = "".join(secure_random.choice(symbols) for i in range(10))
print(password) # '^@g;J?]M6e'

# Create cryptographically secure random numbers
from random import SystemRandom
secure_rand_gen = SystemRandom()

print([secure_rand_gen.randrange(10) for i in range(10)])
# [9, 6, 9, 2, 2, 3, 8, 0, 9, 9]
print(secure_rand_gen.randint(0, 20))
# 5

# Random and sequences: shuffle, choice and sample
# shuffle
import random
laughs = ["Hi", "Ho", "He"]
random.shuffle(laughs) # Shuffles in-place! Don't do: laughs = random.shuffle(laughs)
print(laughs)
# Out: ["He", "Hi", "Ho"] # Output may vary!

# choice
print(random.choice(laughs))
# Out: He       # Output may vary!

# sample
#   |--sequence--|--number--|
print(random.sample( laughs , 1 )) # Take one element
# Out: ['Ho']       # Output may vary!
print(random.sample(laughs, 3)) # Take 3 random element from the sequence.
# Out: ['Ho', 'He', 'Hi']       # Output may vary!
print(random.sample(laughs, 4)) # Take 4 random element from the 3-item sequence.
# ValueError: Sample larger than population

# Creating random integers and floats: randint, randrange, random, and uniform
import random
random.randint(x, y)
random.randint(1, 8) # Out: 8
random.randrange(100) # Random integer between 0 and 99
random.randrange(20, 50) # Random integer between 20 and 49
random.rangrange(10, 20, 3) # Random integer between 10 and 19 with step 3 (10, 13, 16 and 19)
random.random() # Out: 0.66486093215306317
random.uniform(1, 8) # Out: 3.726062641730108

# Reproducible random numbers: Seed and State
random.seed(5) # Create a fixed state
print(random.randrange(0, 10)) # Get a random integer between 0 and 9
# Out: 9
print(random.randrange(0, 10))
# Out: 4
random.seed(5) # Reset the random module to the same fixed state.
print(random.randrange(0, 10))
# Out: 9
print(random.randrange(0, 10))
# Out: 4

save_state = random.getstate() # Get the current state
print(random.randrange(0, 10))
# Out: 5
print(random.randrange(0, 10))
# Out: 8
random.setstate(save_state) # Reset to saved state
print(random.randrange(0, 10))
# Out: 5
print(random.randrange(0, 10))
# Out: 8
