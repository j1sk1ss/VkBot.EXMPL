import vk_api
import requests

from objects.chat_bot_object import Bot
from objects.interface_object.body import Body
from objects.interface_object.button import Button
from objects.interface_object.page import Page
from objects.module.action_page_reveal import ActionPageReveal
from objects.module.action_simple_message import ActionSimpleMessage

requests.Session()
vk_session = vk_api.VkApi("self.login", "self.password")
vk_session.auth(token_only=True)

vk = vk_session.get_api()

attention_page = Page.__init__(name="Уведомление", buttons=[
        Button.__init__(name="Вечером, после 21", keyboard=None, action_module=ActionSimpleMessage(vk, "Вечером", "120391023")),
        Button.__init__(name="Срочно", keyboard=None, action_module=ActionSimpleMessage(vk, "СРОЧНО", "120391023"))
    ], message="Хорошо. Я точно смогу выполнить Ваш заказ вечером после 21.00, однако, если нужно срочно, пожалуйста, "
               "нажмите на кнопку «СРОЧНО».(Если ответ не поступит в течении 5-10 мин, значит я нахожусь не в общаге "
               "или у меня нет доступа к сети)")

accept_page = Page.__init__(name="Заказ", buttons=[ # LINK TO SAVED USER
        Button.__init__(name="Принять", keyboard=None, action_module=ActionSimpleMessage(vk, "Вечером", "120391023")),
        Button.__init__(name="Отказать", keyboard=None, action_module=ActionSimpleMessage(vk, "СРОЧНО", "120391023"))
    ], message="Хорошо. Я точно смогу выполнить Ваш заказ вечером после 21.00, однако, если нужно срочно, пожалуйста, "
               "нажмите на кнопку «СРОЧНО».(Если ответ не поступит в течении 5-10 мин, значит я нахожусь не в общаге "
               "или у меня нет доступа к сети)")

body = Body([
    Page.__init__(name="Меню", buttons=[
        Button.__init__(name="Широкоформатная", keyboard=None, action_module=ActionPageReveal(vk, "", "", attention_page)),
        Button.__init__(name="Печать А4, фото", keyboard=None, action_module=ActionPageReveal(vk, "", "", attention_page)),
        Button.__init__(name="Брошюровка", keyboard=None, action_module=ActionPageReveal(vk, "", "", attention_page))
    ], message="Приветствую, вот вся информация", attachment="")
], vk)

bot = Bot.__init__(vk_session, body)
