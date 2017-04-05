import xlwt
class User():
    """
    User class, responsible for storing and recalling user information.
    """
    def __init__(self, FPSID):
        self.user_name = None
        self.user_email = None
        self.user_status = None
        self.ID = FPSID
    def user_recall(self):
        self.user_name =