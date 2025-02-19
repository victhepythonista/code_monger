from code_monger import CodeGenerator
# specify the path you want to store the codes 
# If the path doesnt exist , the program will attempt to make it 
# Let's replicate a scenario where you want to authenticate a user's email in a web app

user_email = "somerandom@email.com"
codes_file = "codes/my_codes.txt"
cm = CodeGenerator(storage_file = codes_file)

# let us generate a new code and store it in the specified file 
code = cm.NewCode(key_string = user_email )

# validation can be done through the CodeGenerator.ValidateCode method like so:
cm.ValidateCode(user_email , code) # will return a Boolean 