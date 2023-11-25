from aiogram import Router, types
from aiogram.filters import CommandStart
from db import Session, Users, Message, engine
import psycopg2

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Assalomu alaykum botga xush kelibsiz!!!")
    chat_id = message.from_user.id
    username = message.from_user.username
    created = message.date

    user = Users(
        chat_id=chat_id,
        username=username,
        created=created
    )

    session = Session()
    session.add(user)
    session.commit()


@router.message()
async def write_message(message: types.Message):
    text = message.text
    created = message.date
    username = message.from_user.username

    message_text = Message(
        text=text,
        created=created,
        username=username
    )

    session = Session()
    session.add(message_text)
    session.commit()
