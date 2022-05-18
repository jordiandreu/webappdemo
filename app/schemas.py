from datetime import datetime

import strawberry


@strawberry.type
class User:
    id: int
    username: str
    email: str
    time_created: datetime
