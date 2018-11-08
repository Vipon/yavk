import sys
from vk_user import *
from vk_music_play import *


if __name__ == '__main__':

	if len(sys.argv) != 3:

		print('ERROR BAD_ARGS_NUM: yavk.py [login] [password]')
		exit()

	user = vk_user(sys.argv[1], sys.argv[2])

	print('\n\nSearch in audio list:')
	[artists, titles] = user.search_audio('One')
	for entry in artists:
		print('Artist:', entry['artist'],'Title:', entry['title'], 'Url:', vk_music_play.get_audio_url(entry))
		#vk_music_play.download_audio(entry)
	for entry in titles:
		print('Artist:', entry['artist'],'Title:', entry['title'], 'Url:', vk_music_play.get_audio_url(entry))
		#vk_music_play.download_audio(entry)
		vk_music_play.play_audio(entry)

	i = int(0)
	while True:
		i += 1

	exit()
