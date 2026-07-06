\# 交通标志检测项目 README

\## 一、环境配置

1\. 环境版本：Python3.13，Torch2.6.0+CUDA12.4

2\. 安装依赖：

pip install -r requirements.txt



\## 二、数据集路径

1\. 原始TT100K数据集：D:\\yolovProject\\TT100K

2\. YOLO格式数据集：D:\\yolovProject\\TT100K\\TT100K\_YOLO

3\. 转换标注格式：

python convert\_tt100k.py

4\. 数据集配置文件：traffic.yaml



\## 三、训练命令

\# 开始训练YOLOv5s基线模型

python train\_baseline.py

训练结果自动保存到 runs/detect/traffic\_output



\# 模型评估测试

python predict\_test.py



\## 四、参数说明

1\. 模型：YOLOv5s

2\. 整体精度mAP50=0.829

3\. 三类标志中禁止通行识别效果最好，让行标志精度偏低

