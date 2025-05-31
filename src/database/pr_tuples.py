from typing import NamedTuple
from datetime import datetime


class Post(NamedTuple):
    id: int
    description: str
    file_name: str
    is_timed: bool


class TimedPost(NamedTuple):
    id: int
    start_time: datetime
    end_time: datetime


class PostView(NamedTuple):
    id: int
    route: str
    name: str
