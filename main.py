import vk_api
import requests

from objects.interface_object.body import Body
from objects.interface_object.button import Button
from objects.interface_object.page import Page
from objects.module.action_simple_message import ActionSimpleMessage

requests.Session()
vk_session = vk_api.VkApi("self.login", "self.password")
vk_session.auth(token_only=True)

vk = vk_session.get_api()

body = Body([
    Page.__init__(name="Меню", buttons=[
        Button.__init__(name="Широкоформатная", keyboard=None,
                        link="Уведомление"),
        Button.__init__(name="Печать А4, фото", keyboard=None,
                        link="Уведомление"),
        Button.__init__(name="Брошюровка", keyboard=None,
                        link="Уведомление"),
        Button.__init__(name="Прочее", keyboard=None,
                        link="Уведомление")
    ], message="Приветствую, вот вся информация", attachment=""),
    Page.__init__(name="Уведомление", buttons=[
        Button.__init__(name="Вечером, после 21", keyboard=None,
                        link="Уведомление", action_module=ActionSimpleMessage(vk, "", "")),
        Button.__init__(name="Срочно", keyboard=None,
                        link="Уведомление", action_module=ActionSimpleMessage(vk, "", "")),
        Button.__init__(name="Прочее", keyboard=None,
                        link="Уведомление", action_module=ActionSimpleMessage(vk, "", "")),
    ], message="Хорошо. Я точно смогу выполнить Ваш заказ вечером после 21.00, однако, если нужно срочно, пожалуйста, "
               "нажмите на кнопку «СРОЧНО».(Если ответ не поступит в течении 5-10 мин, значит я нахожусь не в общаге "
               "или у меня нет доступа к сети)")
], vk)
