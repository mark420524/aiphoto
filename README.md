[参考项目](https://github.com/itainf/aiphoto)

***目前仅在centos7 python3.6环境下测试通过，其他系统暂未调试***



## 下载模型

需要下载两个模型，由于模型文件比较大，版本库没有上传

[shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) 下载完成后将其放在```m_dlib```文件下

[u2net](https://github.com/OPHoperHPO/image-background-remove-tool/releases/download/3.2/u2net.pth) 下载完成将其放在 ```u_2_net/saved_models/u2net```文件下

# aiphoto
最近要去办事情，很多地方都需要证件照，最近刚好在看AI，人脸识别，图形识别相关的知识，就打算利用这些技术开发一个证件照功能

蓝底原始图：

![image-20200715000133867](https://raw.githubusercontent.com/wiki/itainf/aiphoto/裁剪照片.assets/image-20200715000133867.png)

关键特征描述：

![image-20200715000232798](https://raw.githubusercontent.com/wiki/itainf/aiphoto/裁剪照片.assets/image-20200715000232798.png)

裁剪后的2寸照片：

![image-20200715000251662](https://raw.githubusercontent.com/wiki/itainf/aiphoto/裁剪照片.assets/image-20200715000251662.png)


# 文档

通过文档可以快速上手和了解项目。

1.[python环境搭建](https://github.com/itainf/aiphoto/wiki/python%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA)

2.[卷积神经网络模型人像分割](https://github.com/itainf/aiphoto/wiki/%E5%8D%B7%E7%A7%AF%E6%A8%A1%E5%9E%8B%E4%BA%BA%E5%83%8F%E5%88%86%E5%89%B2)

3.[利用PyMatting替换背景颜色](https://github.com/itainf/aiphoto/wiki/%E5%88%A9%E7%94%A8PyMatting%E7%B2%BE%E7%BB%86%E5%8C%96%E6%8A%A0%E5%9B%BE)


### 更新记录

2020年7月4日更新

本次更新版本： v20200704

本次更新了，通过卷积神经网络模型分割人像

文档： [卷积模型人像分割](https://github.com/itainf/aiphoto/wiki/%E5%8D%B7%E7%A7%AF%E6%A8%A1%E5%9E%8B%E4%BA%BA%E5%83%8F%E5%88%86%E5%89%B2)


