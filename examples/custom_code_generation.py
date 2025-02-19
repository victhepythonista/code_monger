from code_monger import generate_code
# A code comprising of numbers only 
code_numbers_only = generate_code(numbers = True , letters = False)

# Letters only code
code_letters_only =  generate_code(numbers = False , letters = True )

# Uppercase Letters only code
code_capitalized_no_numbers =  generate_code(numbers = False , letters = True , capitalize = True )

# Lowercase Letters only code
code_lowercase_only =  generate_code(numbers = False , letters = True ,capitalize = False )

# code made up of letters, numbers and punctuation charachters
code_all_types_of_charachters =  generate_code(numbers = True , letters = True  , punctuation_chars  = True)