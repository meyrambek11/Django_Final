import time
from django.contrib.auth.hashers import check_password
from django.conf import settings
from rest_framework import authentication, exceptions
import jwt
from rest_framework.exceptions import ValidationError

from autho.models import TokenLog, User


def empty_to_none(s):
    """
    :param s: String to be converted.
    :return: If string is empty returns None; otherwise returns string itself.
    """
    if s is not None:
        if len(s) == 0:
            return None
    return s


def create_token(user, request=None):
    """
    Creates token string.
    :param user: User for which token should be created.
    :return: authentication token.
    """
    info = {
        'id': user.id,
        'email': user.email,
        'timestamp': int(time.time()),
    }
    token = jwt.encode(info, settings.JWT_KEY, settings.JWT_ALGORITHM)

    if request:
        TokenLog.objects.filter(user=user, deleted=False).update(deleted=True)
    TokenLog.objects.create(user=user, token=token)
    return token


def verify_token(token_string, request):
    """
    Verifies token string.
    :param token_string: Token string to verify.
    :return: Profile/user object if token is valid; None is token is invalid.
    """
    try:
        result = jwt.decode(
            token_string, settings.JWT_KEY, settings.JWT_ALGORITHM)
        user_id = result['id']
        user = User.objects.get(id=user_id)
        # Check if token exists in TokenLog and not deleted
        token_obj = user.tokens.get(token=token_string, deleted=False)
        return user, token_obj
    except:
        return None, None


def extract_token_from_request(request):
    header_names_list = settings.AUTH_TOKEN_HEADER_NAME
    token_string = None
    for name in header_names_list:
        if name in request.META:
            token_string = empty_to_none(request.META[name])
    return empty_to_none(token_string)


class CustomAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        token_string = extract_token_from_request(request)
        if token_string is None:
            return None

        user, token_obj = verify_token(token_string, request)
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid token.')

        return user, token_string


def authorize(request, email, password):
    user = User.objects.get(email=email)
    if not check_password(password, user.password):
        raise ValidationError('Пароль неверный!')
    token = create_token(user, request)
    return user, token


def logout(request):
    token_string = extract_token_from_request(request)
    token_obj = request.user.tokens.get(token=token_string, deleted=False)
    token_obj.deleted = True
    token_obj.save(update_fields=('deleted',))
