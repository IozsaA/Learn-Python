friends = ['Rolf', 'Charlie', 'Anna']
friends_lower = map(lambda x: x.lower(), friends)

print(friends_lower)

print(list(friends_lower))


friends_lower = [friend.lower() for friend in friends]

friends_lower = (friend.lower() for friend in friends)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


# imagine these users are coming from a database...

users = [
    { 'username': 'rolf', 'password': '123' },
    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
]

user_objects = map(User.from_dict, users)

"""
The option of using a list comprehension is slightly uglier, I feel:
"""

user_objects = [User.from_dict(u) for u in users]

"""
Although of course, using dictionary unpacking everything would be made much simpler… More on that in a coming section!
"""