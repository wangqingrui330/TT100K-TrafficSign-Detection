#TT100K交通标志检测系统

## 一、项目简介
本项目基于YOLOv5s轻量化目标检测模型，使用TT100K交通标志公开数据集，实现禁止通行、方向指示、减速让行三类道路标志识别。项目完成数据集格式转换、模型基线训练、多场景光照退化测试，对比晴天、阴天、雨雾工况下模型检测精度，验证模型在复杂道路环境下的识别鲁棒性。

 ## 二、团队成员与分工
| 姓名 | 学号 | 分工 |
| ---- | ---- | ---- |
| 唐镘柠、郭思忆 | 2024141450057、2024141450058| 实验报告撰写及数据整理 |
| 王清瑞、杨惠茹 | 2024141450112、2024141450110 | 环境搭建以及模型训练，实现交通标志检测 |
| 陈梓璇 |2024141450138 | 模型测试以及不同条件检测性能对比分析 |
## 三、环境配置
# Python版本
Python 3.8

# CUDA版本：
12.4，显卡RTX4050 Laptop

# 一键安装全部依赖
pip install -r code/requirements.txt

# 校验GPU环境是否可用
python code/check_gpu.py

## 四、数据集路径
1. 原始TT100K数据集：D:\yolovProject\TT100K
2. YOLO格式数据集：D:\yolovProject\TT100K\TT100K_YOLO
3. 转换标注格式：
python convert_tt100k.py
4. 数据集配置文件：traffic.yaml

## 五、运行方法
# 1. 转换数据集标注格式
python code/convert_tt100k.py

# 2. 启动YOLOv5s基线模型训练
python code/train_baseline.py

# 3. 模型推理与精度指标评估
python code/predict_test.py
## 六、实验结果
#1.
类别编号    类别名称    AP@0.5    AP@0.5:0.95
0    限速标志    86.72%    61.45%
1    禁止通行标志    84.19%    59.83%
2    直行 / 转弯标志    82.56%    57.21%
3    人行横道标志    80.34%    55.67%
4    停车让行标志    78.14%    54.59%

#2.
环境工况    样本数量    mAP@0.5    Precision    Recall    性能表现说明
晴天光照充足    25    87.61%    95.45%    84%    光线清晰，特征完整，检测效果最优
阴天弱光    25    81.27%    94.74%    76%    对比度下降，小幅漏检小标志
雨雾模糊    25    70.16%    94.74%    72%    图像细节丢失，小目标识别能力大幅下降

## 七、项目结构
yolovProject/
├── code/                    # 项目全部源代码
│   ├── README.md            # 项目说明文档
│   ├── requirements.txt     # Python依赖清单
│   ├── train_baseline.py    # 模型训练脚本
│   ├── predict_test.py      # 评估推理脚本
│   ├── convert_tt100k.py    # 数据集处理转换脚本
│   ├── check_gpu.py         # GPU环境检测脚本
│   ├── generate_blur.py     # 模糊图像数据增强
│   ├── generate_dark.py     # 暗光图像数据增强
│   └── traffic.yaml         # 数据集配置文件
├── report/
│   └── report.pdf           # 完整实验报告
├── results/
│   ├── loss_curve.png       # 训练损失曲线
│   ├── confusion_matrix.png # 分类混淆矩阵
│   └── comparison_table.png # 多工况实验对比图表
├── TT100K/                  # TT100K原始数据集
├── TT100K_YOLO/             # 转换后YOLO格式数据集
└── runs/detect/             # 训练、推理自动输出结果
