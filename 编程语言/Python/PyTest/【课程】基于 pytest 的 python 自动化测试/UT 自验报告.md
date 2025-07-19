# UT 自验报告

## quantization.py && test_quantization.py

-   `/Users/xc/Documents/Code/D15F94/msit_ascend/msmodelslim/msmodelslim/app/naive_quantization/quantization.py`
-   `/Users/xc/Documents/Code/D15F94/msit_ascend/msmodelslim/test/cases/msmodelslim/app/naive_quantization/test_quantization.py`

### ![image-20250611210757950](./assets/UT%20%E8%87%AA%E9%AA%8C%E6%8A%A5%E5%91%8A/image-20250611210757950.png)

## naive_entrance && test_naive_entrance

-   `/Users/xc/Documents/Code/D15F94/msit_ascend/msmodelslim/msmodelslim/app/naive_quantization/naive_entrance.py`
-   `/Users/xc/Documents/Code/D15F94/msit_ascend/msmodelslim/test/cases/msmodelslim/app/naive_quantization/test_naive_entrance.py`

![image-20250611210640527](./assets/UT%20%E8%87%AA%E9%AA%8C%E6%8A%A5%E5%91%8A/image-20250611210640527.png)

## practice_data && test_practice_data

-   `/Users/xc/Documents/Code/D15F94/msit_ascend/msmodelslim/msmodelslim/app/naive_quantization/practice_data.py`
-   `/Users/xc/Documents/Code/D15F94/msit_ascend/msmodelslim/test/cases/msmodelslim/app/naive_quantization/test_practice_data.py`

![image-20250611210925643](./assets/UT%20%E8%87%AA%E9%AA%8C%E6%8A%A5%E5%91%8A/image-20250611210925643.png)

## main && test_main

-   `/Users/xc/Documents/Code/D15F94/msit_ascend/msmodelslim/msmodelslim/cli/__main__.py`
-   `/Users/xc/Documents/Code/D15F94/msit_ascend/msmodelslim/test/cases/msmodelslim/cli/test_main.py`

![image-20250611211116662](./assets/UT%20%E8%87%AA%E9%AA%8C%E6%8A%A5%E5%91%8A/image-20250611211116662.png)

## practice_manager && test_practice_manager

-   `/Users/xc/Documents/Code/D15F94/msit_ascend/msmodelslim/msmodelslim/infra/practice_manager.py`
-   `/Users/xc/Documents/Code/D15F94/msit_ascend/msmodelslim/test/cases/msmodelslim/infra/test_practice_manager.py`

![image-20250611211245198](./assets/UT%20%E8%87%AA%E9%AA%8C%E6%8A%A5%E5%91%8A/image-20250611211245198.png)

## 测试环境（仅供参考）

```py
# 测试框架和工具
pytest==8.4.0
pytest-cov==6.1.1
coverage==7.8.2
pluggy==1.6.0

# 项目依赖
numpy==2.3.0
PyYAML==6.0.2
argparse==1.4.0
dataclasses==0.6
typing==3.7.4.3
pathlib==1.0.1
tqdm==4.65.0
torch==2.0.1

# 开发工具
black==24.2.0
flake8==7.0.0
mypy==1.8.0

# 其他依赖
iniconfig==2.1.0
packaging==25.0
Pygments==2.19.1 
```

