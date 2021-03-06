from models.base_model import BaseModel
from models.feedback import Feedback
import peewee as pw
from playhouse.hybrid import hybrid_property

class Replies(BaseModel):
    reply_message = pw.CharField(null=False)
    feedback_replied = pw.ForeignKeyField(Feedback, backref='feedback_msg')

    