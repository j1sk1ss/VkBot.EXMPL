from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard


class Bot:
    def __init__(self, vk_session, body):
        for event in VkLongPoll(vk_session).listen():
            if not event.type == VkEventType.MESSAGE_NEW or not event.to_me or not event.text:
                continue

            keyboard = VkKeyboard()
            body.click(event, keyboard)
