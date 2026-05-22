import math
from etl import etl

# --- EUCLID DISTANCE ---
def euclid_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
# -----------------------

# --- NORMALIZE DATA ---
def transform_value(val, min_val, max_val):
    if max_val == min_val:
        return 0
    return (val - min_val)/(max_val - min_val)

def normalize(df):
    X, y = [], []
    min_age, max_age = min(df['Age']), max(df['Age'])
    min_bp, max_bp = min(df['BP']), max(df['BP'])
    min_cholesterol, max_cholesterol = min(df['Cholesterol']), max(df['Cholesterol'])
    for index, row in df.iterrows():
        sex = row['Sex']

        age = row['Age']
        age = transform_value(age, min_age, max_age)

        st_depress = row['ST depression']

        bp = row['BP']
        bp = transform_value(bp, min_bp, max_bp)

        cholesterol = row['Cholesterol']
        cholesterol = transform_value(cholesterol, min_cholesterol, max_cholesterol)

        X.append([age, sex, bp, cholesterol, st_depress])
        y.append(row['Heart Disease'])
    return (X, y)
# ----------------------

# --- EXTRACT DATA ---
df = etl.extract_train_data()
X_train, y_train = normalize(df)
# --------------------

# --- KNN ---
class KNN:
    def __init__(self, k=5):
        self.k = k
        self.X = []
        self.y = []

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, p):
        results = []
        n = len(self.X)
        for i in range(n):
            distance = euclid_distance(self.X[i], p)
            results.append([distance, self.y[i]])

        results.sort(key=lambda x: x[0])

        yes, no = 0, 0
        for j in range(self.k):
            if results[j][1] == 'Presence':
                yes += 1
            else:
                no += 1

        evaluation = (yes / self.k) * 100
        return str(f"{evaluation:.2f}") + ' % you cause a heart disease'
# -----------

# --- IMPLEMENT ---
def implement(norms=[0, 0, 0, 0, 0], k=3):
    knn = KNN(k)
    knn.fit(X_train, y_train)
    result = knn.predict(norms)
    return result
# -----------------