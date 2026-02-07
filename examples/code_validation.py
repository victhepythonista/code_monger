from code_monger import CodeGenerator
# specify the path you want to store the codes 
# If the path doesnt exist , the program will attempt to make it 
# Let's replicate a scenario where you want to authenticate a user's email in a web app

user_email = "somerandom@email.com"
codes_file = "test_codes/my_codes.txt"
cg = CodeGenerator(storage_file = codes_file)

# let us generate a new code and store it in this variable ,
# the code is automatically saved in the file provided during initialization of CodeGenerator
code = cg.NewCode(key_string = user_email )

# validation can be done through the CodeGenerator.ValidateCode method like so:
cg.ValidateCode(user_email , code) 
# will return a Boolean , True if the code is valid else False