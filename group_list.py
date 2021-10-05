'''
The group_list function accepts a group name and a list of members,
and returns a string with the format: group_name: member1, member2, …
'''
def group_list(group, users):
  team = str(users).replace('[','').replace(']','').replace("'","").replace(',','')
  members = '{}: {}'.format(group,team)
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
# Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) 
# Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:
