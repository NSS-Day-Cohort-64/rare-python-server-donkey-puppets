class Post_Reaction():
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, user_id, reaction_id, post_id):
        self.id = id
        self.user_id = user_id
        self.reaction_id = reaction_id
        self.post_id = post_id