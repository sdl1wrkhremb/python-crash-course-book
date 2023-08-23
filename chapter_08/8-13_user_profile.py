def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


print(build_profile('james', 'smith', location='usa',
      language='python', major='computer science', pet='dog'))
