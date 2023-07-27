import vk_api
import requests

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

from enum import Enum

from enums.message_type import MessageType
from objects.interface_object.button import Button


class Bot:
    login = ""
    password = ""

    triggers = []

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def start(self):
        requests.Session()
        vk_session = vk_api.VkApi(self.login, self.password)
        vk_session.auth(token_only=True)

        vk = vk_session.get_api()

        for event in VkLongPoll(vk_session).listen():
            if not event.type == VkEventType.MESSAGE_NEW or not event.to_me or not event.text:
                continue

            match event.text:
                case "start":
                    button = [Button(), Button(), Button()]

            if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы':
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Test message',
                        attachment="",
                        random_id=get_random_id()
                    )
                elif event.from_chat:
                    vk.messages.send(
                        chat_id=event.chat_id,
                        message='Ваш текст'
                    )