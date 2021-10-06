'''
The format_address function separates out parts of the address
string into new strings: house_number and street_name, and returns:
"house number X on street named Y". The format of the input string is:
numeric house number, followed by the street name which may contain numbers,
but never by themselves, and could be several words long
'''
def format_address(address_string):
  # Declare variables
  house_number = ''
  street_name = ''
  # Separate the address string into parts
  address = address_string.split(' ',1)
  # Traverse through the address parts
  for name in address:
    # Determine if the address part is the
    # house number or part of the street name
    #print(name)
    if name.isdigit():
      house_number += ''.join(name)
      #print(house_number)
    elif name != ' ':
      street_name += ''.join(name)
      #print(street_name)
    else:
      street_name += ''.join(' ')

  #print(house_number,street_name) 
  # Does anything else need to be done 
  # before returning the result?
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number,street_name)

print(format_address("123 Main Street"))
# print: "house number 123 on street named Main Street"
print(format_address("1001 1st Ave"))
# print: "house number 1001 on street named 1st Ave"
print(format_address("55 North Center Drive"))
# print "house number 55 on street named North Center Drive"

