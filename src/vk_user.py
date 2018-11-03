from vk_api import *


class vk_user:
	"""
	__vk_session
	__vk
	"""

	def __init__(self, login = '', password = ''):

		self.__vk_session = vk_api.VkApi(login, password)
		self.__vk_session.auth()

		self.__vk = self.__vk_session.get_api()


	def make_post(self, msg = ''):

		self.__vk.wall.post(message=msg)
