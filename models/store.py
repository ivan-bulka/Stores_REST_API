from db import db

class StoreModel(db.Model): 
    __tablename__ = 'stores' 

    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic') # CHANGES. It's a list of ItemModels. When we use 'dynamic', items is a query builder. So, we should use  'all()' when get the list of items 

    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]} # CHANGES
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self): 
        db.session.add(self) 
        db.session.commit() 

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
