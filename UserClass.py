import xlwt
import xlrd
from xlutils.copy import copy
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
        self.working_row = None
        self.ID = FPSID
        self.rb = xlrd.open_workbook('UserData.xlsx')
        self.r_sheet = self.rb.sheet_by_index(0)
        self.wb = copy(self.rb)
        self.w_sheet = self.wb.get_sheet(0)

    def user_recall(self):
        print(str(self.r_sheet.nrows))
        for counter in range(1, self.r_sheet.nrows-1):
            if self.r_sheet.cell(counter, 6) == self.ID:
                self.working_row = counter
                print(str(self.working_row))
                print(str(counter))