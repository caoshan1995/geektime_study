from copy import copy

import pytest

from service.petclinic.api.owner import Owner
from service.petclinic.api.owners import Owners
from service.petclinic.api.test_data import owner_common


class TestUpdateOwner:
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

    @pytest.mark.parametrize("owner", [
        {"telephone": "1880000000", "city": "上海", "address": "xxx市xxx区xxx街道", "firstName": "li",
         "lastName": "xiao"},
        {"telephone": "1870000000", "city": "深圳", "address": "xxx市xxx区xxx街道", "firstName": "li",
         "lastName": "xiao"},
        {"telephone": "1880000000", "city": "深圳", "address": "深圳市xxx区xxx街道", "firstName": "li",
         "lastName": "xiao"},
        {"telephone": "1880000000", "city": "深圳", "address": "xxx市xxx区xxx街道", "firstName": "qian",
         "lastName": "xiao"}
    ])
    def test_update_success(self, owner):
        owner1 = Owner(**owner)
        r = self.owners.update(self.owner_id, owner1)
        assert r.status_code == 204
