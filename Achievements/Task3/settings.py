# -*- coding = utf-8 -*-
# @Time: 2023/03/30
# @Author:MoyiTech
# @Software: PyCharm

config = {
    'epoch': 50,
    'batch_size': 512,
    'learning_rate': 8e-3,
    'device': 'cpu',
    "num_cols": ['regDate', 'creatDate', 'power', 'kilometer', 'v_0', 'v_1', 'v_2', 'v_3', 'v_4', 'v_5', 'v_6', 'v_7', 'v_8', 'v_9', 'v_10',
                 'v_11', 'v_12', 'v_13', 'v_14'],
    "cate_cols": ['model', 'brand', 'bodyType', 'fuelType', 'gearbox', 'seller', 'notRepairedDamage'],
    'models_dir': 'trained_models'
}
