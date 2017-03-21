# -*- coding: utf-8 -*-
import requests
import io

'''
需要先配置aria2c、生成bat脚本以及下载的路径，课程id列表填入需要下载的课程
'''
download_exe = r'E:\Program Files (x86)\aria2\aria2c.exe'
download_dir = r'e:\maizi'
urls_bat = r'e:\click_to_download.bat'
course_id_list = [313]


def download(course_id):
    result = []
    url = 'http://api.maiziedu.com/v2/getCoursePlayInfo/?courseId=%d&client=android' % course_id
    r = requests.get(url)
    json_data = r.json()
    course_name = json_data['data']['course_name']
    video_list = json_data['data']['video_list']

    for video in video_list:
        video_id = video['video_id']
        video_name = video['video_name']
        video_url = video['video_url']
        cmd = r'"%s" "%s" --file-allocation=none --max-connection-per-server=4  -d "%s\%s" -o "%d_%s.mp4"' \
              % (download_exe, video_url, download_dir, course_name, video_id, video_name)
        print(cmd)
        result.append(cmd)
    return result

def main():
    result = []
    for course_id in course_id_list:
        result = result + download(course_id)

    bat_file = io.open(urls_bat, 'w+', encoding='gbk')
    for cmd in result:
        bat_file.writelines(cmd + '\r\n')
    bat_file.close()

if __name__ == '__main__':
    main()