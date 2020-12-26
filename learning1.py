# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib,numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import Perceptron
from sklearn.metrics import jaccard_score

# =============================================================================
#预测简单
# users = ["User1", "User2", "User3", "User4", "User5"]
# items = ["Item A", "Item B", "Item C", "Item D", "Item E"]
# # 构建数据集
# datasets = [
#     ["buy",None,"buy","buy",None],
#     ["buy",None,None,"buy","buy"],
#     ["buy",None,"buy",None,None],
#     [None,"buy",None,"buy","buy"],
#     ["buy","buy","buy",None,"buy"],
# ]
# 
# datasets_num = []
# # a = [result if cond else result2 for x in y ] 
# for lines in datasets:
#     datasets_num.append([1 if a =="buy" else 0 for a in lines])
# 
# df = pd.DataFrame(datasets_num,columns=items,index = users)
# # print(df)
# 
# 
# from sklearn.metrics import jaccard_score
# # print(jaccard_score( df["Item A"],  df["Item B"]))
# from sklearn.metrics.pairwise import pairwise_distances
# user_similar = 1 - pairwise_distances(df.values, metric="jaccard")
# user_similar = pd.DataFrame(user_similar,columns=users,index=users)
# # print(user_similar)
# 
# item_similar = 1 - pairwise_distances(df.T.values, metric="jaccard")
# item_similar = pd.DataFrame(item_similar,columns=items,index=items)
# # print(item_similar)
# 
# from pprint import pprint
# topN_users = {}
# 
# for i in user_similar.index:
#     _df = user_similar.loc[i].drop([i])
#     _df_sorted = _df.sort_values(ascending=False)
#     topN2 = list(_df_sorted.index[:2])
#     topN_users[i]=topN2
# 
# # pprint(topN_users)
# 
# rs_resultes ={}
# 
# for user,sim_users in topN_users.items():
#     rs_resulte = set()
#     for sim_user in sim_users:
#         rs_resulte = rs_resulte.union(set(df.loc[sim_user].replace(0,np.nan).dropna().index))
#     rs_resulte -= set(df.loc[user].replace(0,np.nan).dropna().index)
#     rs_resultes[user] = rs_resulte
# print(rs_resultes)        
# =============================================================================

users = ["User1", "User2", "User3", "User4", "User5"]
items = ["Item A", "Item B", "Item C", "Item D", "Item E"]
# 用户购买记录数据集
datasets = [
    [5,3,4,4,None],
    [3,1,2,3,3],
    [4,3,4,3,5],
    [3,3,1,5,4],
    [1,5,5,2,1],
]

df = pd.DataFrame(datasets,columns = items,index = users)

user_similar = df.T.corr()
# print(user_similar.round(4))

item_similar = df.corr()

# print(item_similar)

import os 
import pandas as pd
import numpy as mp

DATA1_PATH = "C:/Users/GO/Desktop/1/CS/17 推荐系统基础/1-推荐系统基础/代码以及其他/day01/数据/ml-latest-small"
DATA_PATH = "C:/Users/GO/Desktop/1/CS/17 推荐系统基础/1-推荐系统基础/代码以及其他/day01/数据/ml-latest-small/ratings.csv"
CACHE_DIR = "C:/Users/GO/Desktop/1/CS/17 推荐系统基础/1-推荐系统基础/代码以及其他/day01/数据/ml-latest-small/cache/"

os.chdir(DATA1_PATH)

def load_data(data_path):
    cache_path = os.path.join(CACHE_DIR,"ratings_matrix.cache")
    print("开始加载数据集...")
    if os.path.exists(cache_path):
        print("加载缓存中...")
        ratings_matrix = pd.read_pickle(cache_path)
        print("从缓存加载数据集完毕")
    else:
        print("加载新数据中...")
        # 设置要加载的数据字段的类型
        dtype = {"userID":np.int32,"movieID":np.int32,"rating":np.float32}
        ratings = pd.read_csv(data_path,dtype=dtype,usecols=range(3))
        ratings_matrix = ratings.pivot_table(index = ["userId"],columns = ["movieId"],values = "rating")
        ratings_matrix.to_pickle(cache_path)
        print("数据集加载完毕")
    return ratings_matrix

def compute_pearson_similarity(ratings_matrix,based = 'user'):
    user_similarity_cache_path = os.path.join(CACHE_DIR,"user_similarity.cache")
    item_similarity_cache_path = os.path.join(CACHE_DIR,"item_similarity.cache")
    if based == "user":
        if os.path.exists(user_similarity_cache_path):
            print("正从缓存加载用户相似度矩阵")
            similarity = pd.read_pickle(user_similarity_cache_path)
        else:
            print("开始计算用户相似度矩阵")
            similarity = ratings_matrix.T.corr()
            similarity.to_pickle(user_similarity_cache_path)
    elif based == "item":
        if os.path.exists(item_similarity_cache_path):
                    print("正从缓存加载物品相似度矩阵")
                    similarity = pd.read_pickle(item_similarity_cache_path)
        else:
            print("开始计算物品相似度矩阵")
            similarity = ratings_matrix.corr()
            similarity.to_pickle(item_similarity_cache_path)
    else:
        raise Exception("unhandled values: %s" %based)
    print("相似度矩阵计算/加载完毕")
    return similarity

# =============================================================================
# if __name__ =='__main__':
#     ratings_matrix = load_data(DATA_PATH)
#     # print(ratings_matrix)
#     user_similar = compute_pearson_similarity(ratings_matrix,based="user")
#     print(user_similar)
#     print("================")
#     item_similar = compute_pearson_similarity(ratings_matrix,based="item")
#     print(item_similar)
# =============================================================================


# =============================================================================
# def predict(uid,iid,ratings_matrix,user_similar):
#     similar_users = user_similar[uid].drop([uid].dropna())
#     similar_users = similar_users.where(similar_users>0).dropna()
#     if similar_users.empty is True:
#         raise Exception("用户<%d>么有" %uid)
#         
#     ids = set(ratings_matrix[iid].dropna().index)&set(similar_users.index)
#     finally_similar_users = similar_users.loc[list(idx)]
#     
#     sum_up = 0
#     sum_down = 0
#     for sim_uid,similarity in finally_similar_users.iteritems():
#         sim_user_rated_movies = ratings_matrix.loc[sim_uid].dropna()
#         sim_user_rating_for_item = sim_user_rated_movies[iid]
#         sum_up +=sim_user_rating_for_item
#         sum_down += similarity
#         
#         predict_rating = sum_up/sum_down
#         print(predict_rating)
# =============================================================================

# ......

# =============================================================================
# def predict(uid, iid, ratings_matrix, user_similar):
#     '''
#     预测给定用户对给定物品的评分值
#     :param uid: 用户ID
#     :param iid: 物品ID
#     :param ratings_matrix: 用户-物品评分矩阵
#     :param user_similar: 用户两两相似度矩阵
#     :return: 预测的评分值
#     '''
#     print("开始预测用户<%d>对电影<%d>的评分..."%(uid, iid))
#     # 1. 找出uid用户的相似用户
#     similar_users = user_similar[uid].drop([uid]).dropna()
#     # 相似用户筛选规则：正相关的用户
#     similar_users = similar_users.where(similar_users>0).dropna()
#     if similar_users.empty is True:
#         raise Exception("用户<%d>没有相似的用户" % uid)
# 
#     # 2. 从uid用户的近邻相似用户中筛选出对iid物品有评分记录的近邻用户
#     ids = set(ratings_matrix[iid].dropna().index)&set(similar_users.index)
#     finally_similar_users = similar_users.loc[list(ids)]
# 
#     # 3. 结合uid用户与其近邻用户的相似度预测uid用户对iid物品的评分
#     sum_up = 0    # 评分预测公式的分子部分的值
#     sum_down = 0    # 评分预测公式的分母部分的值
#     for sim_uid, similarity in finally_similar_users.iteritems():
#         # 近邻用户的评分数据
#         sim_user_rated_movies = ratings_matrix.loc[sim_uid].dropna()
#         # 近邻用户对iid物品的评分
#         sim_user_rating_for_item = sim_user_rated_movies[iid]
#         # 计算分子的值
#         sum_up += similarity * sim_user_rating_for_item
#         # 计算分母的值
#         sum_down += similarity
# 
#     # 计算预测的评分值并返回
#     predict_rating = sum_up/sum_down
#     print("预测出用户<%d>对电影<%d>的评分：%0.2f" % (uid, iid, predict_rating))
#     return round(predict_rating, 2)
# 
# if __name__ == '__main__':
#     ratings_matrix = load_data(DATA_PATH)
# 
#     user_similar = compute_pearson_similarity(ratings_matrix, based="user")
#     # 预测用户1对物品1的评分
#     predict(1, 1, ratings_matrix, user_similar)
#     # 预测用户1对物品2的评分
#     predict(1, 2, ratings_matrix, user_similar)
# =============================================================================

def predict(uid,iid,ratings_matrix,user_similar):
    print("开始预测用户<%d>对电影<%d>的评分..."%(uid, iid))
    
    similar_users = user_similar[uid].drop([uid]).dropna()

    similar_users = similar_users.where(similar_users>0).dropna()
    if similar_users.empty is True:
        raise Exception("用户<%d>没有相似的用户" % uid)
        
    ids = set(ratings_matrix[iid].dropna().index)&set(similar_users.index)
    finally_similar_users = similar_users.loc[list(ids)]
    sum_up = 0 
    sum_dowm = 0
    for sim_uid,similarity in finally_similar_users.iteritems():
        sim_user_rated_movies = ratings_matrix.loc[sim_uid].dropna()
        sim_user_rating_for_item = sim_user_rated_movies[iid]
        sum_up += similarity * sim_user_rating_for_item
        sum_dowm += similarity
    
    predict_rating =sum_up/sum_dowm
    print("预测出用户<%d>对电影<%d>的评分：%0.2f" % (uid, iid, predict_rating))
    return round(predict_rating,2)
# =============================================================================
# 
# if __name__ == '__main__':
#     ratings_matrix = load_data(DATA_PATH)
#     user_similar = compute_pearson_similarity(ratings_matrix,based="user")
#     
#     predict(1,1,ratings_matrix,user_similar)
#     predict(1,2,ratings_matrix,user_similar)
# =============================================================================

# =============================================================================
# # ......
# def predict_all(uid, ratings_matrix, user_similar):
#     '''
#     预测全部评分
#     :param uid: 用户id
#     :param ratings_matrix: 用户-物品打分矩阵
#     :param user_similar: 用户两两间的相似度
#     :return: 生成器，逐个返回预测评分
#     '''
#     # 准备要预测的物品的id列表
#     item_ids = ratings_matrix.columns
#     # 逐个预测
#     for iid in item_ids:
#         try:
#             rating = predict(uid, iid, ratings_matrix, user_similar)
#         except Exception as e:
#             print(e)
#         else:
#             yield uid, iid, rating
# 
# if __name__ == '__main__':
#     ratings_matrix = load_data(DATA_PATH)
# 
#     user_similar = compute_pearson_similarity(ratings_matrix, based="user")
# 
#     for i in predict_all(1, ratings_matrix, user_similar):
#         pass
# =============================================================================

# =============================================================================
# def predict_all(uid,ratings_matrix,user_similar):
#     item_ids = ratings_matrix.columns
#     
#     for iid in item_ids:
#         try:
#             rating = predict(uid,iid,ratings_matrix,user_similar)
#         except Exception as e:
#             print(e)
#     else:
#         yield uid,iid, rating
# =============================================================================

# =============================================================================
# 
# def _predict_all(uid, item_ids, ratings_matrix, user_similar):
#     '''
#     预测全部评分
#     :param uid: 用户id
#     :param item_ids: 要预测的物品id列表
#     :param ratings_matrix: 用户-物品打分矩阵
#     :param user_similar: 用户两两间的相似度
#     :return: 生成器，逐个返回预测评分
#     '''
#     # 逐个预测
#     for iid in item_ids:
#         try:
#             rating = predict(uid, iid, ratings_matrix, user_similar)
#         except Exception as e:
#             print(e)
#         else:
#             yield uid, iid, rating
# 
# def predict_all(uid, ratings_matrix, user_similar, filter_rule=None):
#     '''
#     预测全部评分，并可根据条件进行前置过滤
#     :param uid: 用户ID
#     :param ratings_matrix: 用户-物品打分矩阵
#     :param user_similar: 用户两两间的相似度
#     :param filter_rule: 过滤规则，只能是四选一，否则将抛异常："unhot","rated",["unhot","rated"],None
#     :return: 生成器，逐个返回预测评分
#     '''
# 
#     if not filter_rule:
#         item_ids = ratings_matrix.columns
#     elif isinstance(filter_rule, str) and filter_rule == "unhot":
#         '''过滤非热门电影'''
#         # 统计每部电影的评分数
#         count = ratings_matrix.count()
#         # 过滤出评分数高于10的电影，作为热门电影
#         item_ids = count.where(count>10).dropna().index
#     elif isinstance(filter_rule, str) and filter_rule == "rated":
#         '''过滤用户评分过的电影'''
#         # 获取用户对所有电影的评分记录
#         user_ratings = ratings_matrix.loc[uid]
#         # 评分范围是1-5，小于6的都是评分过的，除此以外的都是没有评分的
#         _ = user_ratings<6
#         item_ids = _.where(_==False).dropna().index
#     elif isinstance(filter_rule, list) and set(filter_rule) == set(["unhot", "rated"]):
#         '''过滤非热门和用户已经评分过的电影'''
#         count = ratings_matrix.count()
#         ids1 = count.where(count > 10).dropna().index
# 
#         user_ratings = ratings_matrix.loc[uid]
#         _ = user_ratings < 6
#         ids2 = _.where(_ == False).dropna().index
#         # 取二者交集
#         item_ids = set(ids1)&set(ids2)
#     else:
#         raise Exception("无效的过滤参数")
# 
#     yield from _predict_all(uid, item_ids, ratings_matrix, user_similar)
# 
# if __name__ == '__main__':
#     ratings_matrix = load_data(DATA_PATH)
# 
#     user_similar = compute_pearson_similarity(ratings_matrix, based="user")
# 
#     for result in predict_all(1, ratings_matrix, user_similar, filter_rule=["unhot", "rated"]):
#         print(result)
# =============================================================================


def _predict_all(uid, item_ids, ratings_matrix, user_similar):
    '''
    预测全部评分
    :param uid: 用户id
    :param item_ids: 要预测的物品id列表
    :param ratings_matrix: 用户-物品打分矩阵
    :param user_similar: 用户两两间的相似度
    :return: 生成器，逐个返回预测评分
    '''
    # 逐个预测
    for iid in item_ids:
        try:
            rating = predict(uid, iid, ratings_matrix, user_similar)
        except Exception as e:
            print(e)
        else:
            yield uid, iid, rating

def predict_all(uid, ratings_matrix,user_similar,filter_rule = None):
    if not filter_rule:
        item_ids = ratings_matrix.columns
    elif isinstance(filter_rule, str) and filter_rule == "unhot":
        count  = ratings_matrix.count()
        item_ids = count.where(count > 10).dropna().index
    elif isinstance(filter_rule, str) and filter_rule == "rated":
        user_ratings =ratings_matrix.loc[uid]
        _ = user_ratings <6
        item_ids = _.where(_==False).dropna().index
    elif isinstance(filter_rule,list) and set(filter_rule) == set(["unhot","rated"]):
        count = ratings_matrix.count()
        ids1 = count.where(count > 10).dropna().index
        
        user_ratings = ratings_matrix.loc[uid]
        
        _ = user_ratings<6
        ids2 = _.where(_ == False).dropna().index
        
        
        
        
        
if __name__ == '__main__':
    ratings_matrix = load_data(DATA_PATH)
    user_similar = compute_pearson_similarity(ratings_matrix, based="user")
        
    for i in predict_all(1,ratings_matrix,user_similar):
        print(i)












