import dataclasses




@dataclasses.dataclass
class Owner:
    address: str = None
    city: str = None
    firstName: str = None
    lastName: str = None
    telephone: str = None
    id: int = 0
