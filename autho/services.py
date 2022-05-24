from autho.models import User


def create_user(kwargs):
    user = User.objects.create_user(**kwargs)
    return user
