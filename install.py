import os
os.system("cd ~")
#更新软件包
os.system("rm $PREFIX/etc/apt/sources.list")
os.system("cp conf/sources.list $PREFIX/etc/apt/sources.list")
os.system("apt update && apt upgrade -y")
#安装vim nginx php php-fpm
os.system("pkg install vim nginx php php-fpm -y")
#移植配置文件
os.system("mv $PREFIX/etc/nginx/nginx.conf $PREFIX/etc/nginx/nginx.conf.bak")
os.system("cp conf/nginx.conf $PREFIX/etc/nginx/nginx.conf")
os.system("cp conf/default.conf $PREFIX/etc/nginx/default.conf")
os.system("mv $PREFIX/etc/php-fpm.d/www.conf.bak")
os.system("cp conf/www.conf $PREFIX/etc/php-fpm.d/www.conf")
#创建网页目录
path = "/storage/emulated/0/www"
if  os.mkdir(path):
    print("=======================================================\n")
    print("请先执行termux-setup-storage,获取本机存储权限再执行python install.py\n")
    print("=======================================================")
if os.path.exists(path):
    print("=======================================================\n")
    print("1.创建www文件夹成功，路径为%s\n"%path)
    print("=======================================================")
else:
    print("创建www文件夹失败失败,请重试")

os.system("cp index.html $PREFIX/share/nginx/html/index.html")
os.system("cp -r web $PREFIX/share/nginx/html/web")

os.system("nginx")
os.system("php-fpm")
print("=======================================================\n")
print("2.管理地址为127.0.0.1:8900")
print("3.将项目放入该目录，游览器输入127.0.0.1:8080即可")
print("4.首页一定要命名为index.*,如index.html index.php\n")
print("=======================================================")


