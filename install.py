import os
#更新软件包
os.system("rm $PREFIX/etc/apt/sources.list")
os.system("cp sources.list $PREFIX/etc/apt/sources.list")
os.system("apt update && apt upgrade -y")
#安装vim nginx php php-fpm
os.system("pkg install vim nginx php php-fpm -y")
#移植配置文件
os.system("mv $PREFIX/etc/nginx/nginx.conf $PREFIX/etc/nginx/nginx.conf.bak")
os.system("cp nginx.conf $PREFIX/etc/nginx/nginx.conf")
os.system("mv $PREFIX/etc/php-fpm.d/www.conf.bak")
os.system("cp www.conf $PREFIX/etc/php-fpm.d/www.conf")
#创建网页目录
path = "/storage/emulated/0/www"
os.mkdir(path)
if os.path.exists(path):
    print("创建www文件夹成功，路径为%s"%path)
else:
    print("创建www文件夹失败失败,请重试")

os.system("cp index.html /storage/emulated/0/www/index.html")
os.system("cp -r web /storage/emulated/0/www/web")

os.system("nginx")
os.system("php-fpm")


