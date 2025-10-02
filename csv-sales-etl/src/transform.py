def transform_data(df):
    df['total']=df['quantity']*df['price']
    return df 