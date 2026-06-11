from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    image = Image.open(image_path)
    metadata = image._getexif()

    if not metadata:
        print("No metadata found.")
        return

    for tag, value in metadata.items():
        tag_name = TAGS.get(tag)
        print(f"{tag_name}: {value}")

extract_metadata("sample.jpg")
