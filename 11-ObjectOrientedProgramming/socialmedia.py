class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"{self.username}'s Timeline")
        if not self.posts:
            print("no posts to display yet.")
            return
        for i,post in enumarate(self.posts, 1):
            


def main():
    user = SocialMediaProfile('johndoe')
    user.

