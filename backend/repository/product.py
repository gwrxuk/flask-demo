class Product(db):
    __tablename__ = 'TEST'
    id = db.Column(db.Integer)
    name = db.Column(db.String(30))

    def __init__(self, id, name):
        self.id=id
        self.name = name