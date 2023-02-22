from printutils import log
from pic_generation import generate_image
from configparser import ConfigParser
import os
from instagram_api import Instagram
import pathlib
from time import sleep


CONFIG = ConfigParser(allow_no_value=True)
THIS_FOLDER = os.path.dirname(os.path.realpath(__file__))


def main():
    if not check_config():
        log("Please check your config, quitting.", error=True)

    path = generate_image(CONFIG.get('openai', 'prompt'),
                          CONFIG.get('openai', 'api-key'))

    # ig = Instagram()
    # ig.login(CONFIG.get('instagram', 'username'),
    #          CONFIG.get('instagram', 'password'))

    # for i in reversed(range(9)):
    #     path = f"{THIS_FOLDER}/{path[2:]}/sliced/img{i+1}.png".replace(
    #         '/', '\\')
    #     ig.upload(path)
    #     sleep(5)


def check_config() -> bool:
    log('Checking the config...')
    if not os.path.exists('config.ini'):
        CONFIG.add_section('openai')
        CONFIG.add_section('instagram')
        CONFIG.set('openai', 'api-key', '')
        CONFIG.set('openai', 'prompt', 'cat --chaos 100')
        CONFIG.set('instagram', 'username', '')
        CONFIG.set('instagram', 'password', '')
        CONFIG.write(open('config.ini', 'w'))
        return False

    CONFIG.read('config.ini')
    api, prompt = CONFIG.items('openai')
    uname, pwd = CONFIG.items('instagram')

    if (not api[1]) or (not prompt[1]) or (not uname[1]) or (not pwd[1]):
        return False

    log(done=True)
    return True


if __name__ == "__main__":
    main()
