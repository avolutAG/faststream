from redis.asyncio.client import Redis as RedisClient

from faststream._compat import Annotated
from faststream.annotations import ContextRepo, Logger, NoCast
from faststream.redis.broker import RedisBroker as RB
from faststream.redis.message import RedisMessage as RM
from faststream.utils.context import Context

__all__ = (
    "Logger",
    "ContextRepo",
    "NoCast",
    "RedisMessage",
    "RedisBroker",
    "Redis",
)

RedisMessage = Annotated[RM, Context("message")]
RedisBroker = Annotated[RB, Context("broker")]
Redis = Annotated[RedisClient, Context("broker._connection")]
