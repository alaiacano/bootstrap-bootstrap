import sha
import datetime
from models import *
from basic_handler import BasicHandler


class RegisterHandler(BasicHandler):
    def get(self):
        self.render("../templates/register.html", just_registered=False, page='register')

    def post(self):
        email = self.get_argument('email', None)
        pw = self.get_argument('password', None)

        if email is None or pw is None:
            self.render('../templates/main.html')
            return

        if len(User.objects(email=email)) > 0:
            self.render('../templates/main.html', hey='%s is already registered' % email, page='register')
            return

        user = User(
            email=email,
            password=sha.sha(pw).hexdigest(),
            registered_on=datetime.datetime.now()
        )
        user.save()

        # log them in by setting the cookie
        self.set_secure_cookie('user', user.email)
        self.render('../templates/register.html', just_registered=True, current_user=user, page='register')


class LoginHandler(BasicHandler):
    def post(self):
        email = self.get_argument('email', None)
        pw = self.get_argument('password', None)

        if pw is not None:
            pw = sha.sha(pw).hexdigest()

        user = User.objects(email=email, password=pw)
        if len(user) != 1:
            self.render('../templates/main.html', hey='Bad login. Try again', page=None, tests=[])
            return
        user = user[0]
        self.set_secure_cookie('user', user.email)
        self.redirect("/")


class LogoutHandler(BasicHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")


class ResetPasswordHandler(BasicHandler):
    def post(self):
        new_password = self.get_argument('password', None)
        current_password = self.get_argument('password_current', None)

        if new_password is not None and current_password is not None:
            if sha.sha(current_password).hexdigest() != self.current_user.password:
                alert_text = "<strong>FAILED:</strong> Your original password was invalid."
            else:
                self.current_user.password = sha.sha(new_password).hexdigest()
                self.current_user.save()
                alert_text = "Your password, public key, and private key have been changed!"
        else:
            alert_text = "Password change failed!"
        self.render("../templates/user_page.html", page='account', alert=alert_text)
