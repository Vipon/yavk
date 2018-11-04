import sys
from vk_user import *


if __name__ == '__main__':

	if len(sys.argv) != 3:

		print('ERROR BAD_ARGS_NUM: yavk.py [login] [password]')
		exit()

	user = vk_user(sys.argv[1], sys.argv[2])
	audio_list = user.get_audio_list()
	print('I have', len(audio_list), 'audios.')

	print('Just audio list:')
	user.print_audio_list()

	print('\n\nSearch in audio list:')
	[artists, titles] = user.search_audio('One')
	for entry in artists:
		print('Artist:', entry['artist'],'Title:', entry['title'])
	for entry in titles:
		print('Artist:', entry['artist'],'Title:', entry['title'])

	exit()
