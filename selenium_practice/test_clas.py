import pytest

# @pytest.mark.usefixtures("setup")
# class Test_cls_level:
#
#     def test_c1(self):
#         print("temp1")
#
#     def test_c2(self):
#         print("temp2")
#
#
# @pytest.mark.usefixtures('data')
# class Test_dt:
#     def test_name(self, data):
#         print(data[0])



@pytest.mark.usefixtures('data2')
class Test_dt2:
    def test_name2(self, data2):
        print(data2)