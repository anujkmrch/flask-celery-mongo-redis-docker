from flask_admin.contrib.mongoengine import ModelView
from app.models import User, Consent, DataInsight
# Helper function to register models
def register_mongoengine_models(admin):
    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Consent))
    admin.add_view(ModelView(DataInsight))