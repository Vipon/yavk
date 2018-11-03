import sys
from vk_user import *


if __name__ == '__main__':

	if len(sys.argv) != 3:

		print('ERROR BAD_ARGS_NUM: yavk.py [login] [password]')
		exit()

	user = vk_user(sys.argv[1], sys.argv[2])
	audio_list = user.get_audio_list()

	for i in range(10):
		print(audio_list[i]['title'])

	exit()
