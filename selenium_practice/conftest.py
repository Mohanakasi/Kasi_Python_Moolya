from pytest import fixture

# @fixture(scope="class", params=[])
# def setup(request):
#     print('test setup\n')
#     yield
#     print('test teardown\n')
#
# @fixture(scope="class")
# def data():
#     return ['moahana', 'kasi']

@fixture(scope='class', params=['chrome', 'edge'])
def data2(request):
    return request.param

