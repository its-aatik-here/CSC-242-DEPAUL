class SocialAccount:
    def __init__(self,init_followers = 0):
        self.followers = init_followers
        return
    def add_follower(self):
        self.followers-=1
        return
    def remove_follower(self):
        self.followers-=1
        return
    def get_followers(self):
        return self.followers
    def __str__(self):
        return "You have {} followers.".format(self.followers)

    def __repr__(poop):
        return "SocialAccount({})".format(poop.followers)


class InstagramAccount:
    def __init__(self, initial_posts=0, initial_followers = 0):
        self.posts = initial_posts
        self.follower_tracker = SocialAccount(initial_followers)
        self.followers_list = []
    def add_post(self):
        self.posts+=1
    def remove_post(self):
        self.posts-=1
    def add_follow(self):
        self.follower_tracker.add_follower()
    def remove_follow(self):
        self.follower_tracker.remove_followers()
    def __str__(self):
        return "You have {} posts and {}".format(self.posts, str(self.follower_tracker))

#if __name__ == 'main':
#   s = SocialAccount()

 #   assert s.get_followers() == 0, "Invalid Initial Follower Count"

  #  s.add_follower()

   # assert s.get_followers() == 1, "Add follower invalid"

    #t = SocialAccount(100)

    #assert s.get_followers() == 100, "Non-default initial followers is invalid"








    
