 
<div align="center">
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
		<a href="https://pepy.tech/projects/art"><img src="https://static.pepy.tech/badge/code-monger" alt="PyPI">
<a href="https://github.com/victhepythonista/art"><img src="https://img.shields.io/github/stars/victhepythonista/code_monger.svg?style=social&label=Stars"></a>
</div>

# Introduction
- **Code monger** is a simple Python package for generation and validation of authentication codes which are generated and stored in files . 
-  For example , you can use this package when generating authentication codes for authenticating user email addresses in a web application .
# Installation using pip
- You can install the package easily on the command using **pip**

## Dependencies
- Oh , none need installing ,every dependency comes with python ( __Python Standard Library__ )
- The main libraries used are :
  - string 
  - random
  - os 

## Windows OS installation
```
python3 -m pip install code_monger

```
alternatively 
```
pip install code_monger
```
or
```
py -m pip install code_monger
```
# Usage
### Simple code generation
- Let us generate a simple code based on the provided parameters

```

from code_monger import generate_code
# generates the code and returns it as a string object
my_code = generate_code(length = 20  )

print(my_code)
```
### Custom code generation
- Let us generate a custom code 

```


# A code comprising of numbers only 
code = generate_code(numbers = True , letters = False)

# Letters only code
code generate_code(numbers = False , letters = True )

# Uppercase Letters only code
code generate_code(numbers = False , letters = True , capitalize = True )

# Lowercase Letters only code
code generate_code(numbers = False , letters = True ,capitalize = False )

# code made up of letters, numbers and punctuation marks
# Letters only code
code generate_code(numbers = True , letters = True  , punctuation  = True)
```
> Please __NOTE__  :  generate_code function and __CodeGenerator.NewCode__  method require the same keyword arguments  with the exception that  __CodeGeneratorNewCode__ requires the __key_string__ argument 


### Code generation and validation in files
- The class __CodeGenerator__ is what we will use for this functionality
```
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
```
 

