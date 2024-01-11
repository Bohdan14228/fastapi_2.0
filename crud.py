import asyncio
from core.models import db_helper, User, Profile, Post
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    return user


async def get_user_buy_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    # result: Result = await session.execute(stmt)
    # user: User | None = result.scalar_one_or_none()
    user: User | None = await session.scalar(stmt)
    return user


async def create_user_profile(
        session: AsyncSession,
        user_id: int,
        first_name: str | None = None,
        last_name: str | None = None
) -> Profile:
    profile = Profile(
        user_id=user_id,
        firstname=first_name,
        lastname=last_name
    )
    session.add(profile)
    await session.commit()
    return profile


async def show_users_with_profiles(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    # result: Result = await session.execute(stmt)
    users = await session.scalars(stmt)
    for user in users:
        print(user)


async def main():
    async with db_helper.session_factory() as session:
#         # await create_user(session=session, username="john")
#         # await create_user(session=session, username="sam")
#         user_sam = await get_user_buy_username(session=session, username="sam")
#         user_john = await get_user_buy_username(session=session, username="john")
#         # await get_user_buy_username(session=session, username="bob")
#         await create_user_profile(
#             session=session,
#             user_id=user_john.id,
#             first_name="John"
#
#         )
#         await create_user_profile(
#             session=session,
#             user_id=user_sam.id,
#             first_name="Sam",
#             last_name="White"
#
#         )
        await show_users_with_profiles(session=session)


if __name__ == '__main__':
    asyncio.run(main())
