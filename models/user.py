from models.base_model import BaseModel
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from playhouse.hybrid import hybrid_property
import peewee as pw


class User(BaseModel, UserMixin):
    name = pw.CharField(unique=False, null=False)
    password = pw.CharField(null=False)
    email = pw.CharField(unique=True, null=False)
    role = pw.CharField(null=False)
    department = pw.CharField(null=False)
    profile_picture = pw.CharField(null=True)
    is_manager = pw.BooleanField(null=True)
    is_executive = pw.BooleanField(null=True)
    manager_id = pw.IntegerField(null=True)

    @hybrid_property
    def profile_image(self):
        from app import app
        if self.profile_picture:
            return f"{app.config['S3_LOCATION']}" + self.profile_picture
        else:
            return "https://api.adorable.io/avatars/285/abott@adorable.png"

    @hybrid_property
    def completed_objective(self):
        from models.objective import Objective
        return [obs for obs in Objective.select().where((Objective.user_id == self.id) & (Objective.done == True)).order_by(Objective.id.desc())]

    @hybrid_property
    def incomplete_objective(self):
        from models.objective import Objective
        return [obs for obs in Objective.select().where((Objective.user_id == self.id) & (Objective.done == False)).order_by(Objective.id.asc())]
