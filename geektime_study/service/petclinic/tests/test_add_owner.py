import pytest

from service.petclinic.api.owner import Owner
from service.petclinic.api.owners import Owners


class TestAddOwner:
    def setup_class(self):
        "clear init"
        self.owners = Owners()

    def setup(self):
        "setup"

    def teardown(self):
        "teardown"

    def setup_teardown(self):
        "teardown class"

    @pytest.mark.parametrize("owner", [
        {"city": "深圳", "telephone": "18800000001", "firstName": "li"},
        {"city": "上海", "telephone": "188000000", "firstName": "a"}
    ])
    def test_add_fail(self,owner):
        owner1 = Owner(**owner);
        owner1.address = "xxx市xxx区xxx街道"
        owner1.lastName = "xiao"
        r = self.owners.add(owner1)
        assert r.status_code == 400

    @pytest.mark.parametrize("owner",[
        {"city": "深圳", "telephone": "1880000000", "firstName":"li"},
        {"city": "上海", "telephone": "1880000009", "firstName":"qian"}
    ])
    def test_add_success(self,owner):
        owner1 = Owner(**owner); #**owner相当于是初始化
        owner1.address = "xxx市xxx区xxx街道"
        owner1.lastName = "xiao"
        r = self.owners.add(owner1)
        assert r.status_code == 201
