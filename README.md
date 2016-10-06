麦子学院视频下载
==========

#####测试环境： `win10 x64` + `PYTHON 2.7`
#####依赖包： `requests`
	pip install requests
#####下载工具： `aria2c`

###使用说明：


#####修改以下内容：
```
# aria2c的位置
download_exe = r'e:\aria2\aria2c.exe'

# 视频储存位置
download_dir = ur'e:\maizi'

# 生成的bat脚本路径
urls_bat = r'e:\click_to_download.bat'

# 此处为课程id列表（例如http://www.maiziedu.com/course/553）可同时下载多个
course_id_list = [381, 553]

```
#####运行生成的bat脚本（附效果图）
![](http://7xwgs3.com1.z0.glb.clouddn.com/%E6%95%88%E6%9E%9C.png)

