from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from googletrans import Translator

transl = Translator()

def go_poll(language):
        go_poll = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=transl.translate("Пройти опрос",  dest=language).text, callback_data="go_poll")]
                ])
        return go_poll

def interesting_places(language):
        interesting_places = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=transl.translate("Музеи",  dest=language).text, callback_data="place_museums")],
        [InlineKeyboardButton(text=transl.translate("Театры",  dest=language).text, callback_data="place_theaters")],
        [InlineKeyboardButton(text=transl.translate("Природа", dest=language).text, callback_data="place_nature")],
        [InlineKeyboardButton(text=transl.translate("Концерты", dest=language).text, callback_data="place_concerts")],
        ])
        return interesting_places

def kitchen(language):
        kitchen = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=transl.translate("Итальянская кухня",  dest=language).text, callback_data="cuisine_italian")],
        [InlineKeyboardButton(text=transl.translate("Грузинская кухня",  dest=language).text, callback_data="cuisine_georgian")],
        [InlineKeyboardButton(text=transl.translate("Американская кухня", dest=language).text, callback_data="cuisine_american")],
        [InlineKeyboardButton(text=transl.translate("Европейская кухня", dest=language).text, callback_data="cuisine_european")],
        [InlineKeyboardButton(text=transl.translate("Русская кухня", dest=language).text, callback_data="cuisine_russian")],
        [InlineKeyboardButton(text=transl.translate("Японская кухня", dest=language).text, callback_data="cuisine_japanese")],
        ])
        return kitchen

def geo_keyboard(language):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=transl.translate("Отправить геологацию",  dest=language).text, request_location=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

def time(language):
        time = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=transl.translate("Утром",  dest=language).text, callback_data="time_morning")],
        [InlineKeyboardButton(text=transl.translate("День",  dest=language).text, callback_data="time_day")],
        [InlineKeyboardButton(text=transl.translate("Вечер", dest=language).text, callback_data="time_evening")],
        [InlineKeyboardButton(text=transl.translate("Ночь", dest=language).text, callback_data="time_night")],
        ])
        return time 

def notifications(language):
        notifications = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=transl.translate("Да",  dest=language).text, callback_data="notifications_yes")],
        [InlineKeyboardButton(text=transl.translate("Нет",  dest=language).text, callback_data="notifications_no")],
        ])
        return notifications

def change(language):
        change = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=transl.translate("Изменить данные",  dest=language).text, callback_data="change")]
        ]
        )
        return change

# def change_geolocation(language):
#         change_geolocation = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text=transl.translate("Изменить геолокацию",  dest=language).text, callback_data="change_geolocation")]
#         [InlineKeyboardButton(text=transl.translate("Изменить место",  dest=language).text, callback_data="change_location")]
#         [InlineKeyboardButton(text=transl.translate("Изменить интерес",  dest=language).text, callback_data="change_place")]
#         [InlineKeyboardButton(text=transl.translate("Изменить кухню",  dest=language).text, callback_data="change_cuisine")]
#         [InlineKeyboardButton(text=transl.translate("Изменить время",  dest=language).text, callback_data="change_time")]
#         [InlineKeyboardButton(text=transl.translate("Изменить уведомления",  dest=language).text, callback_data="change_notifications")]
#         ])
#         return change_geolocation

def search(language):
        search = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=transl.translate("Найти ближайшие места",  dest=language).text, callback_data="search")]
                ])
        return search
      

        

