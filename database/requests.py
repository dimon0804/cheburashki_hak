from sqlalchemy import select, update
from database.models import async_session, User, Place
# from sqlalchemy.ext.asyncio import AsyncSession

async def is_user_registered(user_id: int) -> bool:
    async with async_session() as session:
        query = select(User).where(User.telegram_id == user_id)
        result = await session.execute(query)
        return result.scalar() is not None
    
async def register_user(
    telegram_id: int, 
    fullname: str, 
    language: str, 
    registration_date: str, 
    last_active_date: str
):
    async with async_session() as session:
        new_user = User(
            telegram_id=telegram_id,
            fullname=fullname,
            language=language,
            registration_date=registration_date,
            last_active_date=last_active_date,
            role="user",  # Значение по умолчанию
            location_lat=None,
            location_lon=None,
            interest=None,
            cuisine=None,
            time_of_day=None,
            notify_discounts=True  # Значение по умолчанию
        )
        session.add(new_user)
        await session.commit()


async def get_user_language(user_id: int) -> str:
    async with async_session() as session:
        language = await session.scalar(select(User).where(User.telegram_id == user_id))
        return language.language

async def update_active(user_id, last_active_date):
    async with async_session() as session:
        await session.execute(update(User).where(User.telegram_id == user_id).values(last_active_date=last_active_date))
        await session.commit()

async def update_role(user_id, role):
    async with async_session() as session:
        await session.execute(update(User).where(User.telegram_id == user_id).values(role=role))
        await session.commit()

async def update_location_lat(user_id, location_lat):
    async with async_session() as session:
        await session.execute(update(User).where(User.telegram_id == user_id).values(location_lat=location_lat))
        await session.commit()

async def update_location_lon(user_id, location_lon):
    async with async_session() as session:
        await session.execute(update(User).where(User.telegram_id == user_id).values(location_lon=location_lon))
        await session.commit()

async def update_interest(user_id, interest):
    async with async_session() as session:
        await session.execute(update(User).where(User.telegram_id == user_id).values(interest=interest))
        await session.commit()

async def update_cuisine(user_id, cuisine):
    async with async_session() as session:
        await session.execute(update(User).where(User.telegram_id == user_id).values(cuisine=cuisine))
        await session.commit()

async def update_time_of_day(user_id, time_of_day):
    async with async_session() as session:
        await session.execute(update(User).where(User.telegram_id == user_id).values(time_of_day=time_of_day))
        await session.commit()

async def update_notify_discounts(user_id, notify_discounts):
    async with async_session() as session:
        await session.execute(update(User).where(User.telegram_id == user_id).values(notify_discounts=notify_discounts))
        await session.commit()

async def update_language(user_id, language):
    async with async_session() as session:
        await session.execute(update(User).where(User.telegram_id == user_id).values(language=language))
        await session.commit()      

async def get_user_info(user_id: int) -> str:
    async with async_session() as session:
        info = await session.scalar(select(User).where(User.telegram_id == user_id))
        return info

async def get_location(user_id: int) -> str:
    async with async_session() as session:
        location = await session.scalar(select(User).where(User.telegram_id == user_id))
        return location
    
async def get_all_places(interest):
    async with async_session() as session:
        result = await session.scalar(select(Place).where(Place.interest == interest))
        return result.location
    