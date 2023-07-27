import vk_api
import requests

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


class Bot:
    @staticmethod
    def get_price_post():
        return ""

    def start(self, login, password):
        requests.Session()
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth(token_only=True)

        vk = vk_session.get_api()
        for event in VkLongPoll(vk_session).listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы':
                    if event.from_user:
                        vk.messages.send(
                            user_id=event.user_id,
                            message='Test message',
                            attachment=self.get_price_post(),
                            random_id=get_random_id()
                        )
                    elif event.from_chat:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            message='Ваш текст'
                        )
