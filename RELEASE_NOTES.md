# RELEASE NOTES

## Version 0.2.1

- Major overhaul on the CodeGenerator class with new methods .ie 
	- **DeleteKey**
	- **GetKey**
	- **ReplaceKey**
	- **GetCode**
	- **DeleteCode**

- Logo update


 ## Version 0.1.7    (21-02-2025)
 
 
- Docstrings  for the *CodeGenerator* class improved
- More stringent tests for code generation
- In the class method **CodeGenerator.NewCode** and in the function **generate_code** the following arguments have been removed  : 
		- **capitalize**
		- **random case** 
	and replaced with with the key word **casing = ""**
	> Say we want to generate a code in uppercase form , instead of using the old way like so :
	```python
	code = generate_code ( capitalize =True , length = 10 , numbers= False )	
    ```
  
   > We do it this way now:
	
	```python
	code = generate_code(casing = "upper", length = 10 , numbers= False )
	```

- Code generation algorithm improved
- README discrepancies fixed and spelling corrected
- Examples updated
