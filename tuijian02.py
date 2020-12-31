# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 12:30:08 2020

@author: GO
"""

# =============================================================================
# class CollaborativeFiltering(object):
# 
#     based = None
# 
#     def __init__(self, k=40, rules=None, use_cache=False, standard=None):
#         '''
#         :param k: 取K个最近邻来进行预测
#         :param rules: 过滤规则，四选一，否则将抛异常："unhot", "rated", ["unhot","rated"], None
#         :param use_cache: 相似度计算结果是否开启缓存
#         :param standard: 评分标准化方法，None表示不使用、mean表示均值中心化、zscore表示Z-Score标准化
#         '''
#         self.k = 40
#         self.rules = rules
#         self.use_cache = use_cache
#         self.standard = standard
# 
# similar_users = self.similar[uid].drop([uid]).dropna().sort_values(ascending=False)[:self.k]
# 
# similar_items = self.similar[iid].drop([iid]).dropna().sort_values(ascending=False)[:self.k]
# =============================================================================

# =============================================================================
# import pandas as pd
# import numpy as np
# 
# 
# class BaselineCFBySGD(object):
# 
#     def __init__(self, number_epochs, alpha, reg, columns=["uid", "iid", "rating"]):
#         # 梯度下降最高迭代次数
#         self.number_epochs = number_epochs
#         # 学习率
#         self.alpha = alpha
#         # 正则参数
#         self.reg = reg
#         # 数据集中user-item-rating字段的名称
#         self.columns = columns
# 
#     def fit(self, dataset):
#         '''
#         :param dataset: uid, iid, rating
#         :return:
#         '''
#         self.dataset = dataset
#         # 用户评分数据
#         self.users_ratings = dataset.groupby(self.columns[0]).agg([list])[[self.columns[1], self.columns[2]]]
#         # 物品评分数据
#         self.items_ratings = dataset.groupby(self.columns[1]).agg([list])[[self.columns[0], self.columns[2]]]
#         # 计算全局平均分
#         self.global_mean = self.dataset[self.columns[2]].mean()
#         # 调用sgd方法训练模型参数
#         self.bu, self.bi = self.sgd()
# 
#     def sgd(self):
#         '''
#         利用随机梯度下降，优化bu，bi的值
#         :return: bu, bi
#         '''
#         # 初始化bu、bi的值，全部设为0
#         bu = dict(zip(self.users_ratings.index, np.zeros(len(self.users_ratings))))
#         bi = dict(zip(self.items_ratings.index, np.zeros(len(self.items_ratings))))
# 
#         for i in range(self.number_epochs):
#             print("iter%d" % i)
#             for uid, iid, real_rating in self.dataset.itertuples(index=False):
#                 error = real_rating - (self.global_mean + bu[uid] + bi[iid])
# 
#                 bu[uid] += self.alpha * (error - self.reg * bu[uid])
#                 bi[iid] += self.alpha * (error - self.reg * bi[iid])
# 
#         return bu, bi
# 
#     def predict(self, uid, iid):
#         predict_rating = self.global_mean + self.bu[uid] + self.bi[iid]
#         return predict_rating
# 
# 
# if __name__ == '__main__':
#     dtype = [("userId", np.int32), ("movieId", np.int32), ("rating", np.float32)]
#     dataset = pd.read_csv("C:/Users/GO/Desktop/1/CS/17 推荐系统基础/1-推荐系统基础/代码以及其他/day01/数据/ml-latest-small/ratings.csv", usecols=range(3), dtype=dict(dtype))
# 
#     bcf = BaselineCFBySGD(20, 0.1, 0.1, ["userId", "movieId", "rating"])
#     bcf.fit(dataset)
# 
#     while True:
#         uid = int(input("uid: "))
#         iid = int(input("iid: "))
#         print(bcf.predict(uid, iid))
#         
# =============================================================================
 
# =============================================================================
# import pandas as pd
# import numpy as np
# 
# 
# class BaselineCFBySGD(object):
# 
#     def __init__(self, number_epochs, alpha, reg, columns=["uid", "iid", "rating"]):
#         # 梯度下降最高迭代次数
#         self.number_epochs = number_epochs
#         # 学习率
#         self.alpha = alpha
#         # 正则参数
#         self.reg = reg
#         # 数据集中user-item-rating字段的名称
#         self.columns = columns
# 
#     def fit(self, dataset):
#         '''
#         :param dataset: uid, iid, rating
#         :return:
#         '''
#         self.dataset = dataset
#         # 用户评分数据
#         self.users_ratings = dataset.groupby(self.columns[0]).agg([list])[[self.columns[1], self.columns[2]]]
#         # 物品评分数据
#         self.items_ratings = dataset.groupby(self.columns[1]).agg([list])[[self.columns[0], self.columns[2]]]
#         # 计算全局平均分
#         self.global_mean = self.dataset[self.columns[2]].mean()
#         # 调用sgd方法训练模型参数
#         self.bu, self.bi = self.sgd()
# 
#     def sgd(self):
#         '''
#         利用随机梯度下降，优化bu，bi的值
#         :return: bu, bi
#         '''
#         # 初始化bu、bi的值，全部设为0
#         bu = dict(zip(self.users_ratings.index, np.zeros(len(self.users_ratings))))
#         bi = dict(zip(self.items_ratings.index, np.zeros(len(self.items_ratings))))
# 
#         for i in range(self.number_epochs):
#             print("iter%d" % i)
#             for uid, iid, real_rating in self.dataset.itertuples(index=False):
#                 error = real_rating - (self.global_mean + bu[uid] + bi[iid])
# 
#                 bu[uid] += self.alpha * (error - self.reg * bu[uid])
#                 bi[iid] += self.alpha * (error - self.reg * bi[iid])
# 
#         return bu, bi
# 
#     def predict(self, uid, iid):
#         predict_rating = self.global_mean + self.bu[uid] + self.bi[iid]
#         return predict_rating
# 
# 
# if __name__ == '__main__':
#     dtype = [("userId", np.int32), ("movieId", np.int32), ("rating", np.float32)]
#     dataset = pd.read_csv("C:/Users/GO/Desktop/1/CS/17 推荐系统基础/1-推荐系统基础/代码以及其他/day01/数据/ml-latest-small/ratings.csv", usecols=range(3), dtype=dict(dtype))
# 
#     bcf = BaselineCFBySGD(20, 0.1, 0.1, ["userId", "movieId", "rating"])
#     bcf.fit(dataset)
# 
#     while True:
#         uid = int(input("uid: "))
#         iid = int(input("iid: "))
#         print(bcf.predict(uid, iid))
# 
# =============================================================================



# =============================================================================
# import pandas as pd
# import numpy as np
# 
# def data_split(data_path, x=0.8, random=False):
#     '''
#     切分数据集， 这里为了保证用户数量保持不变，将每个用户的评分数据按比例进行拆分
#     :param data_path: 数据集路径
#     :param x: 训练集的比例，如x=0.8，则0.2是测试集
#     :param random: 是否随机切分，默认False
#     :return: 用户-物品评分矩阵
#     '''
#     print("开始切分数据集...")
#     # 设置要加载的数据字段的类型
#     dtype = {"userId": np.int32, "movieId": np.int32, "rating": np.float32}
#     # 加载数据，我们只用前三列数据，分别是用户ID，电影ID，已经用户对电影的对应评分
#     ratings = pd.read_csv(data_path, dtype=dtype, usecols=range(3))
# 
#     testset_index = []
#     # 为了保证每个用户在测试集和训练集都有数据，因此按userId聚合
#     for uid in ratings.groupby("userId").any().index:
#         user_rating_data = ratings.where(ratings["userId"]==uid).dropna()
#         if random:
#             # 因为不可变类型不能被 shuffle方法作用，所以需要强行转换为列表
#             index = list(user_rating_data.index)
#             np.random.shuffle(index)    # 打乱列表
#             _index = round(len(user_rating_data) * x)
#             testset_index += list(index[_index:])
#         else:
#             # 将每个用户的x比例的数据作为训练集，剩余的作为测试集
#             index = round(len(user_rating_data) * x)
#             testset_index += list(user_rating_data.index.values[index:])
# 
#     testset = ratings.loc[testset_index]
#     trainset = ratings.drop(testset_index)
#     print("完成数据集切分...")
#     return trainset, testset
# 
# def accuray(predict_results, method="all"):
#     '''
#     准确性指标计算方法
#     :param predict_results: 预测结果，类型为容器，每个元素是一个包含uid,iid,real_rating,pred_rating的序列
#     :param method: 指标方法，类型为字符串，rmse或mae，否则返回两者rmse和mae
#     :return:
#     '''
# 
#     def rmse(predict_results):
#         '''
#         rmse评估指标
#         :param predict_results:
#         :return: rmse
#         '''
#         length = 0
#         _rmse_sum = 0
#         for uid, iid, real_rating, pred_rating in predict_results:
#             length += 1
#             _rmse_sum += (pred_rating - real_rating) ** 2
#         return round(np.sqrt(_rmse_sum / length), 4)
# 
#     def mae(predict_results):
#         '''
#         mae评估指标
#         :param predict_results:
#         :return: mae
#         '''
#         length = 0
#         _mae_sum = 0
#         for uid, iid, real_rating, pred_rating in predict_results:
#             length += 1
#             _mae_sum += abs(pred_rating - real_rating)
#         return round(_mae_sum / length, 4)
# 
#     def rmse_mae(predict_results):
#         '''
#         rmse和mae评估指标
#         :param predict_results:
#         :return: rmse, mae
#         '''
#         length = 0
#         _rmse_sum = 0
#         _mae_sum = 0
#         for uid, iid, real_rating, pred_rating in predict_results:
#             length += 1
#             _rmse_sum += (pred_rating - real_rating) ** 2
#             _mae_sum += abs(pred_rating - real_rating)
#         return round(np.sqrt(_rmse_sum / length), 4), round(_mae_sum / length, 4)
# 
#     if method.lower() == "rmse":
#         rmse(predict_results)
#     elif method.lower() == "mae":
#         mae(predict_results)
#     else:
#         return rmse_mae(predict_results)
# 
# class BaselineCFBySGD(object):
# 
#     def __init__(self, number_epochs, alpha, reg, columns=["uid", "iid", "rating"]):
#         # 梯度下降最高迭代次数
#         self.number_epochs = number_epochs
#         # 学习率
#         self.alpha = alpha
#         # 正则参数
#         self.reg = reg
#         # 数据集中user-item-rating字段的名称
#         self.columns = columns
# 
#     def fit(self, dataset):
#         '''
#         :param dataset: uid, iid, rating
#         :return:
#         '''
#         self.dataset = dataset
#         # 用户评分数据
#         self.users_ratings = dataset.groupby(self.columns[0]).agg([list])[[self.columns[1], self.columns[2]]]
#         # 物品评分数据
#         self.items_ratings = dataset.groupby(self.columns[1]).agg([list])[[self.columns[0], self.columns[2]]]
#         # 计算全局平均分
#         self.global_mean = self.dataset[self.columns[2]].mean()
#         # 调用sgd方法训练模型参数
#         self.bu, self.bi = self.sgd()
# 
#     def sgd(self):
#         '''
#         利用随机梯度下降，优化bu，bi的值
#         :return: bu, bi
#         '''
#         # 初始化bu、bi的值，全部设为0
#         bu = dict(zip(self.users_ratings.index, np.zeros(len(self.users_ratings))))
#         bi = dict(zip(self.items_ratings.index, np.zeros(len(self.items_ratings))))
# 
#         for i in range(self.number_epochs):
#             print("iter%d" % i)
#             for uid, iid, real_rating in self.dataset.itertuples(index=False):
#                 error = real_rating - (self.global_mean + bu[uid] + bi[iid])
# 
#                 bu[uid] += self.alpha * (error - self.reg * bu[uid])
#                 bi[iid] += self.alpha * (error - self.reg * bi[iid])
# 
#         return bu, bi
# 
#     def predict(self, uid, iid):
#         '''评分预测'''
#         if iid not in self.items_ratings.index:
#             raise Exception("无法预测用户<{uid}>对电影<{iid}>的评分，因为训练集中缺失<{iid}>的数据".format(uid=uid, iid=iid))
# 
#         predict_rating = self.global_mean + self.bu[uid] + self.bi[iid]
#         return predict_rating
# 
#     def test(self,testset):
#         '''预测测试集数据'''
#         for uid, iid, real_rating in testset.itertuples(index=False):
#             try:
#                 pred_rating = self.predict(uid, iid)
#             except Exception as e:
#                 print(e)
#             else:
#                 yield uid, iid, real_rating, pred_rating
# 
# if __name__ == '__main__':
# 
#     trainset, testset = data_split("C:/Users/GO/Desktop/1/CS/17 推荐系统基础/1-推荐系统基础/代码以及其他/day01/数据/ml-latest-small/ratings.csv", random=True)
# 
#     bcf = BaselineCFBySGD(20, 0.1, 0.1, ["userId", "movieId", "rating"])
#     bcf.fit(trainset)
# 
#     pred_results = bcf.test(testset)
# 
#     rmse, mae = accuray(pred_results)
# 
#     print("rmse: ", rmse, "mae: ", mae)
# =============================================================================

# =============================================================================
# import pandas as pd
# import numpy as np
# 
# class BaselineCFBySGD(object):
#     def __init__(self,number_epochs,alpha,reg,column = ["uid","iid","rating"]):
#         self.number_epochs = number_epochs
#         self.alpha = alpha
#         self.reg = reg
#         self.column = column
#     
#     def fit(self,dataset):
#         self.dataset = dataset
#         self.users_ratings = dataset.groupby(self.column[0]).agg([list])[[self.column[1],self.columns[2]]]
# 
# =============================================================================


'''
LFM Model
'''
import pandas as pd
import numpy as np

# 评分预测    1-5
class LFM(object):

    def __init__(self, alpha, reg_p, reg_q, number_LatentFactors=10, number_epochs=10, columns=["uid", "iid", "rating"]):
        self.alpha = alpha # 学习率
        self.reg_p = reg_p    # P矩阵正则
        self.reg_q = reg_q    # Q矩阵正则
        self.number_LatentFactors = number_LatentFactors  # 隐式类别数量
        self.number_epochs = number_epochs    # 最大迭代次数
        self.columns = columns

    def fit(self, dataset):
        '''
        fit dataset
        :param dataset: uid, iid, rating
        :return:
        '''

        self.dataset = pd.DataFrame(dataset)

        self.users_ratings = dataset.groupby(self.columns[0]).agg([list])[[self.columns[1], self.columns[2]]]
        self.items_ratings = dataset.groupby(self.columns[1]).agg([list])[[self.columns[0], self.columns[2]]]

        self.globalMean = self.dataset[self.columns[2]].mean()

        self.P, self.Q = self.sgd()

    def _init_matrix(self):
        '''
        初始化P和Q矩阵，同时为设置0，1之间的随机值作为初始值
        :return:
        '''
        # User-LF
        P = dict(zip(
            self.users_ratings.index,
            np.random.rand(len(self.users_ratings), self.number_LatentFactors).astype(np.float32)
        ))
        # Item-LF
        Q = dict(zip(
            self.items_ratings.index,
            np.random.rand(len(self.items_ratings), self.number_LatentFactors).astype(np.float32)
        ))
        return P, Q

    def sgd(self):
        '''
        使用随机梯度下降，优化结果
        :return:
        '''
        P, Q = self._init_matrix()

        for i in range(self.number_epochs):
            print("iter%d"%i)
            error_list = []
            for uid, iid, r_ui in self.dataset.itertuples(index=False):
                # User-LF P
                ## Item-LF Q
                v_pu = P[uid] #用户向量
                v_qi = Q[iid] #物品向量
                err = np.float32(r_ui - np.dot(v_pu, v_qi))

                v_pu += self.alpha * (err * v_qi - self.reg_p * v_pu)
                v_qi += self.alpha * (err * v_pu - self.reg_q * v_qi)
                
                P[uid] = v_pu 
                Q[iid] = v_qi

                # for k in range(self.number_of_LatentFactors):
                #     v_pu[k] += self.alpha*(err*v_qi[k] - self.reg_p*v_pu[k])
                #     v_qi[k] += self.alpha*(err*v_pu[k] - self.reg_q*v_qi[k])

                error_list.append(err ** 2)
            print(np.sqrt(np.mean(error_list)))
        return P, Q

    def predict(self, uid, iid):
        # 如果uid或iid不在，我们使用全剧平均分作为预测结果返回
        if uid not in self.users_ratings.index or iid not in self.items_ratings.index:
            return self.globalMean

        p_u = self.P[uid]
        q_i = self.Q[iid]

        return np.dot(p_u, q_i)

    def test(self,testset):
        '''预测测试集数据'''
        for uid, iid, real_rating in testset.itertuples(index=False):
            try:
                pred_rating = self.predict(uid, iid)
            except Exception as e:
                print(e)
            else:
                yield uid, iid, real_rating, pred_rating

if __name__ == '__main__':
    dtype = [("userId", np.int32), ("movieId", np.int32), ("rating", np.float32)]
    dataset = pd.read_csv("C:/Users/GO/Desktop/1/CS/17 推荐系统基础/1-推荐系统基础/代码以及其他/day01/数据/ml-latest-small/ratings.csv", usecols=range(3), dtype=dict(dtype))

    lfm = LFM(0.02, 0.01, 0.01, 10, 5, ["userId", "movieId", "rating"])
    lfm.fit(dataset)

    while True:
        uid = input("uid: ")
        iid = input("iid: ")
        print(lfm.predict(int(uid), int(iid)))







