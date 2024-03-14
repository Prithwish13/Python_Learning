from random import Random

class User:
    # pass
    def __init__(self, username: str) -> None:
        random_generator = Random()
        self.id = random_generator.randint(1, 1000)
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user: 'User') -> None:
        user.followers += 1
        self.following += 1    
    
user_1 = User(username="Prithwish")
user_2 = User(username="Ankana")

user_1.follow(user=user_2)
print(user_1.following)
print(user_2.followers)

