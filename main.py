import os 
from exiftool import ExifTool, ExifToolHelper
from model import gh0st_config

root_path = os.path.dirname(os.path.abspath(__file__))


def open_image_file(file_name):
    with open(file_name, 'rb') as file:
        return file


images = []

images_dir = os.path.join(root_path, 'photos')

for file_name in os.listdir(images_dir):
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        images.append(open_image_file(os.path.join(images_dir, file_name)))



def nuke_all_meta_data(image_path: str) -> bool:
    """Delete's all meta_data associated to an image.

    :param image_path: Path to the image.
    :return: True if the operation succeeded, False otherwise.

    """
    try:
        with ExifTool() as et:
            command = ['-all=', '-overwrite_original', image_path]
            et.execute(*command)
        return True
        
    except Exception as e:
        print(f"Error occured while deleting all metadata : {e}")
        return False

def set_tags_on_a_file(image_path: str, tags: dict) -> bool:
    """Set the tags on a file.

    :param image_path: Path to the image.
    :param tags: Tags to set.

    :return: True if the operation succeeded, False otherwise.

    """
    try:
        with ExifToolHelper() as et:
            et.set_tags(image_path, tags, params='-overwrite_orignal')
        return True
    except Exception as e:
        print(f"Error occured while setting tags : {e}")
        return False

image_file = os.path.join(images_dir, 'snakey.jpeg')
nuke_all_meta_data(image_file)
set_tags_on_a_file(image_file, gh0st_config.data)