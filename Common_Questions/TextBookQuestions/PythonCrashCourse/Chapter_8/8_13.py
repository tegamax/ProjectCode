'''
8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(),
using your first and last names and three other key-value pairs that describe you.
'''

def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

complete_profile=build_profile('tega','maxi',location='San Francisco',race='black')
print(complete_profile)

''' 
#full_name = {'first': first_name, 'last':last_name}
#full_name['names'] = names
#print(full_name)
'''