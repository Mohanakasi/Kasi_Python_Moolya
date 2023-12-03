
class bank_xyz:
    ac_num = 1234
    ac_bal = 0
    _cc_num = 2345
    __cc_bal = 20
    def display_acc_bal(self):
        print(self.ac_num)

    def display_cc_details(self):
        print(self._cc_num, self.__cc_bal)

    def modify_cc_bal(self, bal):
        self.__cc_bal += bal

# obj1 = bank_xyz()
# print(obj1.ac_num, obj1.ac_bal)
# print(obj1._cc_num)
# print(obj1.display_acc_bal())
# print(obj1.display_cc_details())
# obj1.modify_cc_bal(123000)
class bank_xyz_ops(bank_xyz):

    def modify_cc_num(self):
        # print(self.__cc_bal)
        # self.__cc_bal += 100
        # print(self.__cc_bal)
        self._cc_num = 8968
        print(self._cc_num)

    def modify_cc_bal_child(self, bal):
        super().modify_cc_bal(bal)
        super().display_cc_details()

obj2 = bank_xyz_ops()
# print(bank_xyz._cc_num)
# obj2.modify_cc_num()
# obj1.display_cc_details()
obj2.modify_cc_bal_child(50000)
obj1 = bank_xyz()
obj1.display_cc_details()