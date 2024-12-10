from aiogram.fsm.state import StatesGroup, State

class StartPoll(StatesGroup):
    kitchen = State()
    