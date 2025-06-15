from code_monger import generate_code
# A code comprising of numbers only 
numbers_only = generate_code(numbers = True , letters = False)

# Letters only code
letters_only =  generate_code(numbers = False , letters = True )

# Uppercase Letters only code
uppercase_letters_only =  generate_code(casing = "upper" , letters = True   )

# Lowercase Letters only code
lowercase_letters_only =  generate_code(casing = "lower" , letters = True   )

# code made up of letters, numbers and punctuation charachters
all_types_of_charachters =  generate_code(numbers = True , letters = True  , punctuation_chars  = True)