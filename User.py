class User:
    '''
    id = 100
    full_name = "Full Name"
    personal_email = "personal_email@gmail.com"
    '''

#Constructor
    def __init__(self, id, full_name, personal_email) -> None:
        self.id = id
        self.full_name = full_name
        self.personal_email = personal_email


object_user = User("0122110810", "Ivan de Santiago", "ivanodesantiago@gmail.com")
print(object_user)
print(object_user.id)
print(object_user.full_name)
print(object_user.personal_email)