# replace old email address domains with new email address domains.

def replace_domain(old_email,old_domain,new_domain):
    if '@'+ old_domain in old_email:
        index = old_email.index('@' + old_domain)
        new_email = old_email[:index] + '@' + new_domain
        return new_email

print(replace_domain('alexy@yahoo.com','yahoo.com','gmail.com')) # alexy@gmail.com
print(replace_domain('maxy@spacex.com','spacex.com','nasa.gov')) # maxy@nasa.gov
