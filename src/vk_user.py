import vk_api
from vk_api.audio import VkAudio

class vk_user:
	"""
	__vk_session
	__vk
	__vk_audio
	__audio_list
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

		try:
			self.__audio_list
		except AttributeError:
			self.__audio_list = self.__vk_audio.get()

		return self.__audio_list


	def print_audio_list(self):

		try:
			self.__audio_list
		except AttributeError:
			self.__audio_list = self.__vk_audio.get()

		for entry in self.__audio_list:
			print('Owner', entry['owner_id'], 'Artist:', entry['artist'],'Title:', entry['title'])


	def search_audio(self, templ=''):

		try:
			self.__audio_list
		except AttributeError:
			self.__audio_list = self.__vk_audio.get()

		artists = [track for track in self.__audio_list if templ in track['artist']]
		titles = [track for track in self.__audio_list if templ in track['title']]

		return [artists, titles]
