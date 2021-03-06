from models.base_model import BaseModel
import peewee as pw
from models.user import User


class Review(BaseModel):
    manager_notes = pw.CharField(unique=False, null=True)
    executive_notes = pw.CharField(unique=False, null=True)
    review_date = pw.DateField(null=True)
    executive = pw.ForeignKeyField(User, backref="reviews")