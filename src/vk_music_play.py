import os
import sys
from vk_user import *
from urllib.request import urlopen
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

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


	def play_audio(audio):

		app = QCoreApplication(sys.argv)

		playlist = QMediaPlaylist()
		url = QUrl.fromLocalFile('.Downloads/One.mp3')
		playlist.addMedia(QMediaContent(url))
		playlist.setPlaybackMode(QMediaPlaylist.Loop)

		player = QMediaPlayer()
		player.setPlaylist(playlist)
		player.setVolume(60)
		player.play()

		app.exec()