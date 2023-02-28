
def check_user_credentials(user_cred):
  # get user credentials
  login = input("Please enter your login name:")
  
  # get a list of all the users with defined credentials
  users = list(user_cred.keys())
  
  try:
    index = users.index(login)
  except: 
    index = -1
  
  print("Returned user index is " + str(index))
  if (index == -1):
      print("The specified user does not exist")
  
  
  
  
  password = input("Please enter your password:")
  
  # check to see if it is a valid user
  stored_password = user_cred.get(login)
  if (stored_password == None):
    print("The user does not have a password set")
    return False
  
  allow_access = False
  # check password against stored password
  if (password == stored_password ):
    print("User password matches the stored value. Access allowed.")
    allow_access = True
  else:
    print("User password does not match the stored value. Access denied.")

  return allow_access

