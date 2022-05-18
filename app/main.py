import asyncio
from typing import AsyncGenerator, List

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info

import app.db_functions as df
from app.schemas import User


@strawberry.type
class Mutation:
    add_user: User = strawberry.field(resolver=df.add_user)
    update_user: User = strawberry.field(resolver=df.update_user)
    delete_user: User = strawberry.field(resolver=df.delete_user)


@strawberry.type
class Query:
    users: List[User] = strawberry.field(resolver=df.get_users)


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)


schema = strawberry.Schema(Query, Mutation, Subscription)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
