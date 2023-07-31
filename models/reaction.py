class Reaction():
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, label, image_url):
        self.id = id
        self.label = label
        self.image_url = image_url