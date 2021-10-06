'''
The groups_per_user function receives a dictionary, which contains
group names with the list of users. Users can belong to multiple groups.
'''
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group,users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
			# Reverse users to be dictionary keys and group to be values.
			user_groups[user] = user_groups.get(user,[])+[group]
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
