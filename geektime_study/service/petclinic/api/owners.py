from _ast import List
from dataclasses import asdict
import requests

from service.petclinic.api.owner import Owner
from service.petclinic.utils import log


class Owners:
    def list(self, last_name) -> List(Owner):
        r = requests.get("https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners",
                         params={"lastName": last_name}
                         )
        # 方便用来断言
        if r.status_code == 200:
            owner_list = []
            for item in r.json():
                if isinstance(item, dict):
                    item.pop('pets')  # 暂时不需要使用这个字段
                    owner = Owner(**item)
                    owner_list.append(owner)
            return owner_list
        else:
            return []

    def add(self, owner):
        r = requests.post(
            "https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners",
            json=asdict(owner)
        )
        return r

    def delete(self,     owner_id):
        r = requests.request(
            "delete",
            f"https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners/{owner_id}"
        )
        return r

    def clear(self, last_name):
        for item in self.list(last_name):
            self.delete(item.id)

    def update(self, owner_id, owner):
        r = requests.request(
            "put",
            f"https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners/{owner_id}",
            json=asdict(owner)
        )
        return r

    def detail(self, owner_id) -> Owner:
        r = requests.get(
            f"https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners/{owner_id}",
        )

        if r.status_code == 200:
            result = r.json()
            if isinstance(result, dict):
                result.pop('pets')  # 暂时不需要使用这个字段
                owner = Owner(**result)
                return owner
        else:
            return r.status_code

