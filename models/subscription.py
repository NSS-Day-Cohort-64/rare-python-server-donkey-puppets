class Subscription():
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, follower_id, author_id, created_on):
        self.id = id
        self.follower_id = follower_id
        self.author_id = author_id
        self.created_on = created_on
