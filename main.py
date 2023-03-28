import sys
from vk import VK
from yd import YD

VK_Token = '...'
VK_Version = '...'
Ya_Token = '...'

VK_id = '...'

if not VK_id.isdecimal():
    print("Ошибка! Не корректный ввод!")
    sys.exit()
else:
    VK_id = int(VK_id)
    vk_user = VK(VK_Token, VK_Version)
    album_id = vk_user.get_albums(VK_id)
    photos_count = input('Введите число фото: ')
    if not photos_count.isdecimal():
        vk_user = VK(VK_Token, VK_Version)
        urls_dict = vk_user.get_photos(VK_id, album_id)
        ya_disk = YD(Ya_Token)
        ya_disk.upload(urls_dict, VK_id)
    else:
        photos_count = int(photos_count)
        vk_user = VK(VK_Token, VK_Version)
        urls_dict = vk_user.get_photos(VK_id, album_id, photos_count)
        ya_disk = YD(Ya_Token)
        ya_disk.upload(urls_dict, VK_id)
