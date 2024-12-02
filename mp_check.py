from moviepy.config import get_setting
print(get_setting("IMAGEMAGICK_BINARY"))

from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

print(get_setting("IMAGEMAGICK_BINARY"))