

from printutils import log


def upload(folder_name: str):
    log('Uploading to Instagram...')
    for i in reversed(range(9)):
        with open(f"{folder_name}/sliced/img{i+1}.png", 'r') as file:
            pass

    log(done=True)
