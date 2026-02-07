

from code_monger import CodeGenerator



email= "myemail@domain.com" 
cg = CodeGenerator("test_codes/example.txt")


# Create a new code for the email
code = cg.NewCode(email)

# delete the code and the email using the code
cg.DeleteCode(code)

# delete the code and the email using the email/key
cg.DeleteKey(email)

# get the code 
cg.GetCode(email)

# get the key/email
cg.GetKey(code)

# replace the email/key string
cg.ReplaceKey(email , "mewemail.dom.com")


