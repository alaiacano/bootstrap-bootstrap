import tornado.web
from models import *


class BasicHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        email = self.get_secure_cookie("user")
        if email is None:
            return None

        user = User.objects(email=email)

        try:
            return user[0]
        except IndexError:
            return None
