import torch
import numpy as np
import time


import sys, torch, platform

print("Python 解释器:", sys.executable)
print("系统:", platform.platform())
print("PyTorch 版本:", torch.__version__)
print("PyTorch CUDA 构建版本:", torch.version.cuda)   # 如果这里是 None，多半是 CPU 版
print("CUDA 是否可用:", torch.cuda.is_available())
