from basic_handler import BasicHandler


class MainHandler(BasicHandler):
    def get(self):
        self.render('../templates/main.html')


class UserPageHandler(BasicHandler):
    def get(self):
        self.render('../templates/user_page.html', alert=None)
