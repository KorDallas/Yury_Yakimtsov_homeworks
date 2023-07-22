# Есть словарь песен группы Depeche Mode violator songsdict = { 'World in
# My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
#  Выведите общее время звучания всех песен. Создайте список песен,
#  время звучаниях которых больше 5 минут Создайте новый словарь тех песен,
#  в название которых состоит из одного слова.

songsdict = {'World inMy Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
             'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18,
             'Clean': 5.68, }
len_of_songs = 0
songs_less_5min = []
dict_of_songs = {}
for key, value in songsdict.items():
    len_of_songs += value
    if value > 5:
        songs_less_5min.append(key)
    if " " not in key:
        dict_of_songs[key] = value
print(f'Общее время звучания песен = {len_of_songs} мин.')
print('Песни время звучания которых больше 5 мин.:', "\n" f'{songs_less_5min}')
print('Песни название которых состоит из одного слова:', '\n' f'{dict_of_songs}')
