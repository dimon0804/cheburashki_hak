from aiogram import types, F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from googletrans import Translator
from datetime import datetime
from pytz import timezone
import requests
import math
from sqlalchemy.ext.asyncio import AsyncSession

import text
from keyboards.language import change_language
import keyboards.user_kb as user_kb
import config 
import database.requests as requremets


router = Router()
transl = Translator()

@router.message(Command(commands=["start"]))
async def start(msg: Message):
    user_id = msg.from_user.id
    user_registered = await requremets.is_user_registered(user_id)
    if user_registered:
        user_language = await requremets.get_user_language(user_id)
        await msg.reply(transl.translate(text.error_register,  dest=user_language).text)
        await msg.answer(transl.translate(text.menu, dest=user_language).text,
                                  reply_markup=user_kb.search(language=user_language))
        return
    await msg.answer(text.hello.format(fullname=msg.from_user.full_name), 
                     reply_markup=change_language)
    
@router.message(Command(commands=["info"]))
async def info(msg: Message):
    user_id = msg.from_user.id
    user_registered = await requremets.is_user_registered(user_id)
    if user_registered:
        user_language = await requremets.get_user_language(user_id)
        await msg.answer(transl.translate(text.menu, dest=user_language).text,
                                  reply_markup=user_kb.search(language=user_language))
        await msg.answer(transl.translate(text.description,  dest=user_language).text)
        return

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Радиус Земли в километрах
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

@router.callback_query(F.data == "search")
async def handle_find_closest(callback: types.CallbackQuery):
    user_data = await requremets.get_location(callback.from_user.id)
    user_lat = user_data.location_lat
    user_lon = user_data.location_lon

    # Получение всех мест из базы данных
    places = await requremets.get_all_places(user_data.interest)
    lat, lon = places.split(",")

    url = f"Ваш маршрут: https://yandex.by/maps/39/rostov-na-donu/?rtext={user_lat},{user_lon}~{lat},{lon}&rtt=auto&ruri=~&z=18.26"
    await callback.message.answer(url)


@router.callback_query(F.data == "go_poll")
async def go_poll_kb(callback: CallbackQuery, bot: Bot):
    await bot.delete_message(chat_id=callback.from_user.id, 
                             message_id=callback.message.message_id)
    user_language = await requremets.get_user_language(callback.from_user.id)
    await callback.message.answer((transl.translate(text.go_opros,  dest=user_language).text), 
                                  reply_markup=user_kb.interesting_places(language=user_language))

@router.callback_query(lambda c: c.data.startswith("place_"))
async def place_callback_handler(callback: CallbackQuery, bot: Bot):
    place = callback.data.split("_")[1]
    await bot.delete_message(chat_id=callback.from_user.id, 
                             message_id=callback.message.message_id)
    
    user_language = await requremets.get_user_language(callback.from_user.id)
    if place == "museums":
        await requremets.update_interest(callback.from_user.id, "museums")
    elif place == "theaters":
        await requremets.update_interest(callback.from_user.id, "theaters")
    elif place == "nature":
        await requremets.update_interest(callback.from_user.id, "nature")
    elif place == "concerts":
        await requremets.update_interest(callback.from_user.id, "concerts")

    await callback.message.answer(transl.translate(text.go_cuisine, dest=user_language).text,
                                  reply_markup=user_kb.kitchen(language=user_language))


@router.callback_query(lambda c: c.data.startswith("cuisine_"))
async def cuisine_callback_handler(callback: CallbackQuery, bot: Bot): 
    cuisine = callback.data.split("_")[1] 
    await bot.delete_message(chat_id=callback.from_user.id, 
                             message_id=callback.message.message_id)
    
    user_language = await requremets.get_user_language(callback.from_user.id)
    if cuisine == "italian": 
        await requremets.update_cuisine(callback.from_user.id, "italian") 
    elif cuisine == "georgian": 
        await requremets.update_cuisine(callback.from_user.id, "georgian") 
    elif cuisine == "american": 
        await requremets.update_cuisine(callback.from_user.id, "american") 
    elif cuisine == "european": 
        await requremets.update_cuisine(callback.from_user.id, "european")
    elif cuisine == "russian": 
        await requremets.update_cuisine(callback.from_user.id, "russian") 
    elif cuisine == "japanese": 
        await requremets.update_cuisine(callback.from_user.id, "japanese") 
    
    await callback.message.answer(transl.translate(text.go_geo, dest=user_language).text,
                                  reply_markup=user_kb.geo_keyboard(language=user_language))

# Обработчик для получения геолокации
@router.message(F.content_type == "location")
async def handle_location(message: Message):
    """
    Обрабатывает сообщение с геолокацией.
    """
    latitude = message.location.latitude
    longitude = message.location.longitude

    user_language = await requremets.get_user_language(message.from_user.id)

    await requremets.update_location_lat(message.from_user.id, latitude)
    await requremets.update_location_lon(message.from_user.id, longitude)

    await message.answer(transl.translate(text.go_time, dest=user_language).text,
                                  reply_markup=user_kb.time(language=user_language))

@router.callback_query(lambda c: c.data.startswith("time_"))
async def time_callback_handler(callback: CallbackQuery, bot: Bot): 
    time = callback.data.split("_")[1] 
    await bot.delete_message(chat_id=callback.from_user.id, 
                             message_id=callback.message.message_id)
    
    user_language = await requremets.get_user_language(callback.from_user.id)
    if time == "morning": 
        await requremets.update_time_of_day(callback.from_user.id, "morning") 
    elif time == "day": 
        await requremets.update_time_of_day(callback.from_user.id, "day") 
    elif time == "evening": 
        await requremets.update_time_of_day(callback.from_user.id, "evening") 
    elif time  == "night": 
        await requremets.update_time_of_day(callback.from_user.id, "night")

    await callback.message.answer(transl.translate(text.go_notifications, dest=user_language).text,
                                  reply_markup=user_kb.notifications(language=user_language))

@router.callback_query(lambda c: c.data.startswith("notifications_"))
async def notifications_callback_handler(callback: CallbackQuery, bot: Bot): 
    notifications = callback.data.split("_")[1] 
    await bot.delete_message(chat_id=callback.from_user.id, 
                             message_id=callback.message.message_id)
    
    user_language = await requremets.get_user_language(callback.from_user.id)
    if notifications == "yes": 
        await requremets.update_notify_discounts(callback.from_user.id, True) 
    elif notifications == "no": 
        await requremets.update_notify_discounts(callback.from_user.id, False) 

    await callback.message.answer(transl.translate(text.successfully_opros, dest=user_language).text,
                                  reply_markup=types.ReplyKeyboardRemove())
    await callback.message.answer(transl.translate(text.menu, dest=user_language).text,
                                  reply_markup=user_kb.search(language=user_language))


@router.callback_query(F.data.in_(config.LANGUES))
async def language(callback: CallbackQuery, bot: Bot):
    lang = callback.data
    user_id = callback.from_user.id
    fullname = callback.from_user.full_name
    
    # Форматируем даты
    moscow_tz = timezone(config.TIME_ZONE)
    registration_date = datetime.now(moscow_tz).strftime("%d.%m.%y %H:%M")
    last_active_date = datetime.now(moscow_tz).strftime("%d.%m.%y %H:%M")
    
    # Регистрируем пользователя
    await requremets.register_user(
        telegram_id=user_id,
        fullname=fullname,
        language=lang,
        registration_date=registration_date,
        last_active_date=last_active_date
    )
    
    await bot.delete_message(chat_id=callback.from_user.id, 
                             message_id=callback.message.message_id)
    hello_message = f"{callback.from_user.full_name}, Ваш язык установлен на {lang}."
    await callback.message.answer(transl.translate(hello_message,  dest=lang).text)
    await callback.message.answer(transl.translate(text.opros_approval,  dest=lang).text, 
                                  reply_markup=user_kb.go_poll(language=lang))
    
@router.message(F.text == "Мой профиль")
async def my_profile(msg: Message):
    user_id = msg.from_user.id
    user_info = await requremets.get_user_info(user_id)

    if not user_info:
        await msg.answer("Не удалось загрузить информацию о вашем профиле.")
        return

    profile_text = (
        f"Ваш профиль:\n"
        f"Имя: {user_info['fullname']}\n"
        f"Язык: {user_info['language']}\n"
        f"Дата регистрации: {user_info['registration_date']}\n"
        f"Интересы: {user_info['interest']}"
        f"Кухни: {user_info['cuisine']}\n"
        f"Время: {user_info['time_of_day']}\n"
        f"Уведомление: {user_info['notify_discounts']}\n"
    )
    await msg.answer(profile_text)
