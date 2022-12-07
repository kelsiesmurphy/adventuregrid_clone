class Experience:
    def __init__(self, title, description, location, image, price, is_featured, id=None):
        self.title = title
        self.description = description
        self.location = location
        self.image = image
        self.price = price
        self.is_featured = is_featured
        self.id = id