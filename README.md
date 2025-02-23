 
 
 
 
<p align="center">
  <img   src="https://i.ibb.co/B5ktzB6F/codemongerlogo.png" alt="Logo">
</p>

<div align="center">
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
		<a href="https://pepy.tech/projects/code_monger"><img src="https://static.pepy.tech/badge/code-monger" alt="PyPI">
<a href="https://github.com/victhepythonista/code_monger"><img src="https://img.shields.io/github/stars/victhepythonista/code_monger.svg?style=social&label=Stars"></a>
</div>




# Introduction

- **Code monger** is a simple Python package for generation and validation of authentication codes which are generated and stored in files . 
-  For example , you can use this package when generating authentication codes for authenticating user email addresses in a web application .
- Check out the <a href="https://github.com/victhepythonista/code_monger/blob/main/RELEASE_NOTES.md" target="_blank"> Release notes</a> to stay updated . 
- Ideas are welcome, contribute !!
- More is on the way .

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

To upgrade your version in Windows ,just use the --upgrade  option when installing . Like so :

```
python -m pip install --upgrade code_monger
```

# Usage

### Simple code generation

- Let us generate a simple code based on the provided parameters

```python

from code_monger import generate_code
# generates the code and returns it as a string object
my_code = generate_code(length = 20  )

print("Code generated : ", my_code)
```

### Custom code generation

- Let us generate a custom code 

```python
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
```

> Please __NOTE__  :  generate_code function and __CodeGenerator.NewCode__  method require the same keyword arguments  with the exception that  __CodeGeneratorNewCode__ requires the __key_string__ argument 


### Code generation and validation in files

- The class __CodeGenerator__ is what we will use for this functionality

```python
from code_monger import CodeGenerator
# specify the path you want to store the codes 
# If the path doesnt exist , the program will attempt to make it 
# Let's replicate a scenario where you want to authenticate a user's email in a web app

user_email = "somerandom@email.com"
codes_file = "codes/my_codes.txt"
cg = CodeGenerator(storage_file = codes_file)

# let us generate a new code and store it in this variable ,
# the code is automatically saved in the file provided during initialization of CodeGenerator
code = cg.NewCode(key_string = user_email )

# validation can be done through the CodeGenerator.ValidateCode method like so:
cg.ValidateCode(user_email , code) 
# will return a Boolean , True if the code is valid else False
```

 

