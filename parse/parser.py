
from vk_api import VkApi

vkSession = VkApi(
    token='token of your page')

vk = vkSession.get_api()

data = []

wall = vk.wall.get(owner_id=-202146149, count=100)

for i, post in enumerate(wall['items']):
    if i >= 2:
        if (len(post['text']) != 0):
            line = post['text'].replace('\n', '')
            if(line.find('"') != -1 and line.find('Праздник') == -1):
                data.append(line)

try:
    f = open('parse/data.txt', 'w')
except FileNotFoundError:
    print('File not found')

for line in data:
    f.write(line + ';\n')

f.close()
