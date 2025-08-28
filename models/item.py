from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    
    store = db.relationship("StoreModel", back_populates="items") # Automatically creates store model object with id store_id
    tags = db.relationship("TagModel", back_populates="item", secondary="item_tags")