
from service.petclinic.api.owners import Owners
from copy import copy
from service.petclinic.api.test_data import owner_common


class TestSearchList:
    def setup_class(self):
        "clear init"
        "在所有测试用例之前只之行一次"

        "引入业务模型"
        self.owners = Owners()

        "清理数据"
        self.owners.clear("xiao")
        self.owners.clear("zhang")

        "初始化数据"
        owner1 = copy(owner_common);
        self.owners.add(owner1)

        owner2 = copy(owner1)
        owner2.firstName = "zhao"
        r = self.owners.add(owner2)

        owner3 = copy(owner1)
        owner3.lastName = "zhang"
        r = self.owners.add(owner3)

    def setup(self):
        "setup"
        "在每个测试用例之行之前执行一次"

    def teardown(self):
        "teardown"

    def setup_teardown(self):
        "teardown class"
        "有可能因为进程被强制终止导致teardown_class得不到执行"
        self.owners.clear("xiao")
        self.owners.clear("zhang")


    def test_search_list_query_null(self):
        r = self.owners.list("")


    def test_search_list_result_null(self):
        r = self.owners.list("liu")
        assert len(r) == 0

    def test_search_list_result_single(self):
        r = self.owners.list("zhang")
        assert len(r) == 1
        assert r[0].lastName == "zhang"
        assert r[0].city == "深圳"


    def test_search_list_result_multile(self):
        r = self.owners.list("xiao")
        assert len(r) > 1


