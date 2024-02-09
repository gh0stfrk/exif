import os 
from exiftool import ExifTool, ExifToolHelper
from PIL import Image
from model import gh0st_config


root_path = os.path.dirname(os.path.abspath(__file__))





images = []

images_dir = os.path.join('/home/salman/', 'unsplash')

for file_name in os.listdir(images_dir):
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        images.append(os.path.join(images_dir, file_name))



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
            et.set_tags(image_path, tags, params=['-overwrite_original'])
        return True
    except Exception as e:
        print(f"Error occured while setting tags : {e}")
        return False


def increase_file_size(image_path, target_size_bytes):
    """Increase the size of a file.

    :param image_path: Path to the image.

    """
    with Image.open(image_path) as image:
        # Calculate the factor by which to scale the image's size
        original_size_bytes = image.size[0] * image.size[1] * 3  # Assuming 3 bytes per pixel
        scaling_factor = (target_size_bytes / original_size_bytes) ** 0.5
    
        # Resize the image to increase its size
        new_width = int(image.size[0] * scaling_factor)
        new_height = int(image.size[1] * scaling_factor)
        image = image.resize((new_width, new_height), Image.LANCZOS)

        image.save(image_path, optimize=True, quality=300)


    print(f"File size increased for {image_path}")

    return True


for image in images:
    image_file = image

    nuke_all_meta_data(image_file)
    set_tags_on_a_file(image_file, gh0st_config.data)

    increase_file_size(image_file, 60000)