import base64

from django import template

register = template.Library()


@register.filter
def get_image_file_as_base64_data(image):
    image_bytes = image.read()
    base64_bytes = base64.b64encode(image_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string