import vk_api
import requests

session = requests.Session()
login, password = 'Ваш логин, email или телефон', 'Ваш пароль'
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)