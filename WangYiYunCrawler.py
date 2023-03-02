# 导入第三方数据请求模块
import requests
import re
import os

fillname = "music\\"

if not os.path.exists(fillname):
    os.mkdir(fillname)

url = 'https://music.163.com/discover/toplist?id=19723756'

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

# print(response.text)

html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)

# print(html_data)

for num_id, title in html_data:
    # http://music.163.com/song/media/outer/url?id=1395222212.mp3
    music_url = f"http://music.163.com/song/media/outer/url?id={num_id}.mp3"
    # 发送音乐播放地址发送请求，获取二进制内容
    music_content = requests.get(url=music_url, headers=headers).content

    with open(fillname + title + '.mp3', mode='wb') as f:
        f.write(music_content)
    print(num_id, title)

