# Heart Disease Prediction

A machine learning project that predicts the probability of heart disease using the K-Nearest Neighbors (KNN) algorithm.

## Features

- Data preprocessing
- KNN classification model
- Heart disease risk prediction
- CSV dataset support
- Simple testing structure

## Technologies Used

- Python
- Pandas
- CSV datasets

## Project Structure

```bash
HeartDisease/
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── etl/
│   └── etl.py
│
├── ML/
│   └── knn.py
│
├── test/
│   └── test.py
│
│── LICENSE
├── columns.txt
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/DoBao000/HeartDiseasePrediction.git
```

Move into the project:

```bash
cd HeartDiseasePrediction
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Project

```bash
python test/test.py
```

## Future Improvements

- Improve model accuracy
- Add more ML algorithms
- Docker support

## Author

Bảo Đỗ Hoàng