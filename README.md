[参考项目](https://github.com/itainf/aiphoto)

# aiphoto

测试通过系统及版本

1. centos7 python3.6
   
   依赖文件为 requirement.txt

2. ubuntu 22.04 python3.10 
   
   依赖文件为 requirement3.10_ubuntu22.txt

## 客户端

微信小程序

[早晚照](https://github.com/mark420524/photo)

## 下载模型

需要下载模型，由于模型文件比较大，版本库没有上传

[u2net](https://github.com/OPHoperHPO/image-background-remove-tool/releases/download/3.2/u2net.pth) 下载完成将其放在 ```u_2_net/saved_models/u2net```文件下


## 构建可能出现的问题

1. ImportError: libGL.so.1: cannot open shared object file: No such file or directory

```
 # 安装 libgl1 
 # ubuntu 
 $ sudo apt install libgl1
 # centos 
 $ sudo yum install mesa-libGL -y
```
