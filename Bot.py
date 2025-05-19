import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

bot = Bot(token="7772565207:AAFh4Oz0U7xerYRIV-bUYviMW3BD2lvyHa4")
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    builder = ReplyKeyboardBuilder()
    questions = [
        "Как адаптироваться в вузе?",
        "Где искать друзей и тусовки?",
        "Как не выгореть?",
        "Советы по учёбе",
        "Чем заняться после пар?"
    ]
    for question in questions:
        builder.add(types.KeyboardButton(text=question))
    builder.adjust(2)
    await message.answer(
        "Привет! Я бот-помощник первокурсника 🎓\n"
        "Выбери вопрос, чтобы получить совет 👇",
        reply_markup=builder.as_markup()
    )

@dp.message(Command("exit"))
async def send_goodbye(message: types.Message):
    await message.answer("Пока! Если что — пиши 💬", reply_markup=ReplyKeyboardRemove())

@dp.message(F.text.lower() == "как адаптироваться в вузе?")
async def adapt(message: types.Message):
    await message.answer("Дай себе время привыкнуть. Ходи на пары, общайся, участвуй в мероприятиях — со временем всё станет привычным.")

@dp.message(F.text.lower() == "где искать друзей и тусовки?")
async def social_life(message: types.Message):
    await message.answer("Загляни в студсовет, кружки по интересам, мероприятия. А ещё — не бойся первым начать разговор 😊")

@dp.message(F.text.lower() == "как не выгореть?")
async def burnout(message: types.Message):
    await message.answer("Делай перерывы, не забывай о сне и отдыхе. Спорт, прогулки и хобби — отличная профилактика выгорания.")

@dp.message(F.text.lower() == "советы по учёбе")
async def study_tips(message: types.Message):
    await message.answer("Заведи календарь дедлайнов, разбивай задачи на мелкие шаги и не бойся просить помощи у преподавателей или старшекурсников.")

@dp.message(F.text.lower() == "чем заняться после пар?")
async def after_classes(message: types.Message):
    await message.answer("Погуляй с друзьями, сходи в спортзал, посмотри кино или начни новый проект. Учёба — не вся жизнь 😉")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
