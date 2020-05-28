# validation.py
# Omar Adnan
# 18-05-2020

# ########
# Packages
# ########
import re # regular expression

# ################
# Validation Class
# ################

class Validation():

    def is_numeric(self, val):
        val = str(val) # only str have the isnumeric() method
        if val.isnumeric():
            print("Numeric")
            return True
        else:
            print("Not numeric")
            return False  

    def is_alphabetic(self, val):
        val = str(val)
        if val.isalpha():
            print("Alphabetic")
            return True
        else:
            print("Not alphabetic")
            return False  

    def is_alphanumeric(self, val):
        val = str(val)
        if val.isalnum():
            print("Alphanumeric")
            return True
        else:
            print("Not alphanumeric")
            return False  

    def is_phone_number(self, val):
        val = str(val)
        if re.search(r'(^\d{2} \d{4} \d{4})', val): # 02 9999 9999
            print("Valid phone number")
            return True
        else:
            print("Invalid phone number")
            return False  

    def is_year_manu(self, val):
        val = str(val) # only str have the isnumeric() method
        if val.isnumeric():
            print("Numeric")
            return True
        else:
            print("Not numeric")
            return False  
    
        
    pass

# ###########
# Main method
# ###########

# The main method is only executed when the file is 'run' (not imported in another file)

if __name__ == '__main__':
    # Instead of writing separate test scripts, could write them here
    # The test scripts would not be executed when the file is imported into another one
    pass        