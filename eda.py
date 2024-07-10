import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = pd.read_csv(url, names=names)

#sampledataset
print(data.head())

#describe data
plt.show()cribe())

sns.pairplot(data, hue='Outcome', diag_kind='kde')
plt.show()


# Histograms for each variable
data.hist(figsize=(12, 10))
plt.tight_layout()
plt.show()


# Boxplot for each variable
data.boxplot(figsize=(12, 8))
plt.title('Boxplot of Variables')
plt.show()

