class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.follower = 0
        self.following = 0

    def instagram(self, u):
        self.following += 1
        u.follower += 1
        u.following += 1

    def change_name(self, new_name):
        self.username = new_name


user_1 = User("001", "fatema")
user_2 = User("002", "ovi")

user_1.instagram(user_2)

user_1.change_name("sorna")
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)
print(user_1.username)
