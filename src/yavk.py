import sys
from vk_user import *


if __name__ == '__main__':

	if len(sys.argv) != 3:

		print('ERROR BAD_ARGS_NUM: yavk.py [login] [password]')
		exit()

	user = vk_user(sys.argv[1], sys.argv[2])
	user.make_post("Hello!")