import asyncio
from core.models import db_helper, User, Profile, Post


async def main():
    async with db_helper.session_factory() as session:
        pass


if __name__ == '__main__':
    asyncio.run(main())
