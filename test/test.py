from etl import etl

def tranform_value(val, min_val, max_val):
    return (val - min_val)/(max_val - min_val)

def normalize(df):
    X, y = [], []
    min_age, max_age = min(df['Age']), max(df['Age'])
    min_bp, max_bp = min(df['BP']), max(df['BP'])
    min_cholesterol, max_cholesterol = min(df['Cholesterol']), max(df['Cholesterol'])

    print(min_bp, max_bp)

    for index, row in df.iterrows():
        sex = row['Sex']

        age = row['Age']
        age = tranform_value(age, min_age, max_age)

        st_depress = row['ST depression']

        bp = row['BP']
        bp = tranform_value(bp, min_bp, max_bp)
        print(bp)

        cholesterol = row['Cholesterol']
        cholesterol = tranform_value(cholesterol, min_cholesterol, max_cholesterol)

        X.append([age, sex, bp, cholesterol, st_depress])
        y.append(row['Heart Disease'])
    return (X, y)
# ----------------------

# --- EXTRACT DATA ---
df = etl.extract_train_data()
X_train, y_train = normalize(df)