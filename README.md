# eBay_vegetable_chickens
## add self-defined functions
## 20180804 feizhe 对POS_CASH_balance表做了修改
pos = pd.read_csv('POS_CASH_balance.csv')
x,y = one_hot_encoder(pd.DataFrame(pos['NAME_CONTRACT_STATUS']))
pos = pos.join(x)
del pos['NAME_CONTRACT_STATUS']
aggregations = {
    'MONTHS_BALANCE': ['max', 'mean', 'size'],
    'SK_DPD': ['max', 'mean','sum'],
    'SK_DPD_DEF': ['max', 'mean','sum'],
    'CNT_INSTALMENT':['mean'],
    'CNT_INSTALMENT_FUTURE':['mean','sum']}
pos_agg = pos.groupby('SK_ID_CURR').agg(aggregations)
pos_agg.columns = pd.Index(['POS_' + e[0] + "_" + e[1].upper() for e in pos_agg.columns.tolist()])
pos_agg['POS_COUNT'] = pos.groupby('SK_ID_CURR').size()
del pos
gc.collect()
pos_agg.head()

原来代码中对真个表onehot encoding了，多了很多没有意义的属性。
