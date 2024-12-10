from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from googletrans import Translator

transl = Translator()

def go_poll(language):
    InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=transl.translate("Пройти опрос",  dest=language).text, callback_data="go_poll")]
        ])

def lturalplace(language):
        InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=transl.translate("Музеи",  dest=language).text, callback_data="museums")],
        [InlineKeyboardButton(text=transl.translate("Театры",  dest=language).text, callback_data="theaters")],
        [InlineKeyboardButton(text=transl.translate("Природа", dest=language).text, callback_data="nature")],
        [InlineKeyboardButton(text=transl.translate("Концерты", dest=language).text, callback_data="concerts")],
        ])

def kitchen(language):
        InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=transl.translate("Итальянская кухня",  dest=language).text, callback_data="italian_cuisine")],
        [InlineKeyboardButton(text=transl.translate("Грузинская кухня",  dest=language).text, callback_data="georgian_cuisine")],
        [InlineKeyboardButton(text=transl.translate("Американская кухня", dest=language).text, callback_data="american_cuisine")],
        [InlineKeyboardButton(text=transl.translate("Европейская кухня", dest=language).text, callback_data="european_cuisine")],
        [InlineKeyboardButton(text=transl.translate("Русская кухня", dest=language).text, callback_data="russian_cuisine")],
        [InlineKeyboardButton(text=transl.translate("Японская кухня", dest=language).text, callback_data="japanese_cuisine")],
        ])

    
    


   