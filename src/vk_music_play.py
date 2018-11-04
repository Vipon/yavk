import os
from vk_user import *
from urllib.request import urlopen


class vk_music_play:

	DOWNLOADS = 'Downloads' + os.sep # os.sep - crossplatform separator


	def get_audio_url(audio):

		return audio['url'].split('?')[0]


	def download_audio(audio):

		url = vk_music_play.get_audio_url(audio)
		remotefile = urlopen(url)

		if not os.path.exists(vk_music_play.DOWNLOADS):
			os.mkdir(vk_music_play.DOWNLOADS)

		localfile = open(vk_music_play.DOWNLOADS + audio['title'] + '.mp3', 'wb')
		localfile.write(remotefile.read())
		localfile.close()

		remotefile.close()
