from aiogram import types, F, Router, Bot
from aiogram.types import Message, CallbackQuery #, ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
# from aiogram.types import FSInputFile
# import asyncio
from googletrans import Translator
from datetime import datetime

import text
from keyboards import language
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
        return
    await msg.answer(text.hello.format(fullname=msg.from_user.full_name), 
                     reply_markup=language.change_language)


@router.callback_query(F.data.in_(config.LANGUES))
async def language(callback: CallbackQuery, bot: Bot, state: FSMContext):
    lang = callback.data
    user_id = callback.from_user.id
    fullname = callback.from_user.full_name
    
    # Форматируем даты
    registration_date = datetime.utcnow().strftime("%d,%m,%y %H,%M")
    last_active_date = datetime.utcnow().strftime("%d,%m,%y %H,%M")
    
    # Регистрируем пользователя
    await requremets.register_user(
        telegram_id=user_id,
        fullname=fullname,
        language=lang,
        registration_date=registration_date,
        last_active_date=last_active_date
    )
    
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    hello_message = f"Привет, {callback.from_user.full_name}! Ваш язык установлен на {lang}."
    await callback.message.answer(transl.translate(hello_message,  dest=lang).text)

@router.message(Command(commands=["info"]))
async def info(msg: Message):
    user_id = msg.from_user.id
    user_language = await requremets.get_user_language(user_id)
    await msg.answer(transl.translate(text.description,  dest=user_language).text)
