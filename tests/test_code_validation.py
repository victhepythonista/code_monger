

import string , unittest

from unittest import TestCase

from code_monger import CodeGenerator , generate_code


test_file = "test_data/test_code_validation.txt"




generator = CodeGenerator(test_file)

class Test_CodeValidation(TestCase):
	'''Test whether codes are validated as expected '''
	def test_validate_code(self):
		pass 

