import xlwt
import xlrd
import xlutils
class User():
    """
    User class, responsible for storing and recalling user information.
    """
    def __init__(self, FPSID):
        self.user_first_name = None
        self.user_last_name = None
        self.user_email = None
        self.user_status = None
        self.user_strength = None
        self.user_volume = None
        self.ID = FPSID
        rb = xlrd.open_workbook('CoffeeUsers.xlsx')
        wb = copy(rb).get

    def user_recall(self):
        self.user_first_name =