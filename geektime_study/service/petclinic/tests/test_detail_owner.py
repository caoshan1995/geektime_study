from copy import copy

from service.petclinic.api.owners import Owners
from service.petclinic.api.test_data import owner_common


class TestDetailOwner:

    def setup_class(self):
        "clear init"
        self.owners = Owners()

        "清理数据"
        self.owners.clear("xiao")

        "初始化数据"
        owner1 = copy(owner_common);
        r = self.owners.add(owner1).json()
        self.owner_id = r["id"]

    def setup(self):
        "setup"

    def teardown(self):
        "teardown"

    def setup_teardown(self):
        "teardown class"
        self.owners.clear("xiao")

    def test_update_success(self,):
        print(self.owner_id)
        r = self.owners.detail(self.owner_id)
        assert r.firstName == 'li'

    def test_update_fail(self):
        r = self.owners.detail(111111)
        assert r == 404
