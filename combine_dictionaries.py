'''
Taylor and Rory are hosting a party. They sent out invitations, and each one collectedresponses
into dictionaries,with names of their friends and how many guests each friend is bringing.Each
dictionary is a partial list, but Rory's list has more current information about the number of guests.
'''
def combine_dictionaries(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  guests2.update(guests1)
  return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

