import vk_api
from vk_api.audio import VkAudio

class vk_user:
	"""
	__vk_session
	__vk
	__vk_audio
	"""

	def __init__(self, login = '', password = ''):

		self.__vk_session = vk_api.VkApi(login, password)

		try:
			self.__vk_session.auth()
		except vk_api.AuthError as error_msg:
			print(error_msg)
			return

		self.__vk = self.__vk_session.get_api()
		self.__vk_audio = VkAudio(self.__vk_session)


	def make_post(self, msg = ''):

		self.__vk.wall.post(message=msg)


	def get_audio_list(self):

		return self.__vk_audio.get()
