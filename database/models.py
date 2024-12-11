from sqlalchemy import BigInteger, String, Integer, Float, Boolean, func, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
import config as cfg


engine = create_async_engine(url=cfg.SQLALCHEMY_URL)
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    # Уникальный идентификатор пользователя
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)  # ID из Telegram
    fullname: Mapped[str] = mapped_column(String(100), nullable=False)  # Полное имя пользователя

    # Дата регистрации и последней активности
    registration_date: Mapped[str] = mapped_column(String, nullable=False)
    last_active_date: Mapped[str] = mapped_column(String, onupdate=func.now(), nullable=False)

    # Основные данные
    role: Mapped[str] = mapped_column(String(50), default="user", nullable=False)  #!! Роли: user, admin
    location_lat: Mapped[float] = mapped_column(Float, nullable=True)  # Широта
    location_lon: Mapped[float] = mapped_column(Float, nullable=True)  # Долгота
    interest: Mapped[str] = mapped_column(String(100), nullable=True)  # Основной интерес
    cuisine: Mapped[str] = mapped_column(String(100), nullable=True)  # Предпочитаемый тип кухни
    time_of_day: Mapped[str] = mapped_column(String(50), nullable=True)  # Удобное время суток для отдыха
    notify_discounts: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)  # Уведомлять о скидках
    language: Mapped[str] = mapped_column(String(10), default='en', nullable=False)  # Язык пользователя 


class Promotion(Base):
    """
    Таблица для хранения акций.
    """
    __tablename__ = "promotions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image_url: Mapped[str] = mapped_column(String(300), nullable=False)


class Place(Base):
    __tablename__ = 'places'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    location: Mapped[str] = mapped_column(nullable=False) 
    category: Mapped[str] = mapped_column(String(100), nullable=False)  # Категория (Ресторан", "Магазин")
    cuisine: Mapped[str] = mapped_column(String(100), nullable=True)   # Предпочитаемый тип кухни
    name: Mapped[str] = mapped_column(String(255), nullable=False)     # Название места
    interest: Mapped[str] = mapped_column(String(100), nullable=True)  # Основной интерес
    time_of_day: Mapped[str] = mapped_column(String(50), nullable=True)  # Удобное время суток

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
