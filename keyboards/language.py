from aiogram.utils.keyboard import InlineKeyboardBuilder
import config as cfg

# Создаём клавиатуру через InlineKeyboardBuilder
keyboard_builder = InlineKeyboardBuilder()

# Добавляем кнопки
for i, j in cfg.LANGDICT.items():
    keyboard_builder.button(text=j, callback_data=i)

# Формируем клавиатуру с разбивкой на ряды по 3 кнопки
keyboard_builder.adjust(3)
change_language = keyboard_builder.as_markup()
  
