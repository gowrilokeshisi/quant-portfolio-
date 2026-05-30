def create_features(df):
    df['debt_to_income'] = df['loan_amnt'] / (df['annual_inc'] + 1)
    return df
