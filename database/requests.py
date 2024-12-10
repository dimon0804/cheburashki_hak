from sqlalchemy import select, update
from database.models import async_session, User

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
        language = select(User).where(User.telegram_id == user_id)
        return language.language
