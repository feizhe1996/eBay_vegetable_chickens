#Kaggle home credit self-defined function
def quan_coder(x,col=[1,2,3,4]):
    x = pd.Series(x)
    s = pd.qcut(x,4,labels = False)
    d = pd.get_dummies(s)
    d.columns = col
    return d

def show_mean(x):
    train_df1 = train_df.loc[train_df['TARGET']==1]
    train_df0 = train_df.loc[train_df['TARGET']==0]
    print("the mean of %s for paid group is %s" %(x,train_df0[x].mean()))
    print("the mean of %s for unpaid group is %s" %(x,train_df1[x].mean()))