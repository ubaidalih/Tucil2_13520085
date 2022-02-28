import convexHull as ch
import pandas as pd
from sklearn import datasets

print("Available dataset :")
print("1. Iris Dataset")
print("2. Wine Dataset")
print("3. Breast Cancer Dataset")
inputDataset = int(input("Input dataset number : "))

if inputDataset == 1 :
    data = datasets.load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    print("Available data :")
    print("1. Sepal Length")
    print("2. Sepal Width")
    print("3. Petal Length")
    print("4. Petal Width")
    inputX = int(input("Input x coordinate number : "))
    inputY = int(input("Input y coordinate number : "))
    ch.displayConvexHull(df, data, inputX, inputY)

elif inputDataset == 2 :
    data = datasets.load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    print("Available data :")
    print("1. Alcohol")
    print("2. Malic acid")
    print("3. Ash")
    print("4. Alcalinity of ash")
    print("5. Magnesium")
    print("6. Total phenols")
    print("7. Flavanoids")
    print("8. Nonflavanoid phenols")
    print("9. Proanthocyanins")
    print("10. Color intensity")
    print("11. Hue")
    print("12. OD280/OD315 of diluted wines")
    print("13. Proline")
    inputX = int(input("Input x coordinate number : "))
    inputY = int(input("Input y coordinate number : "))
    ch.displayConvexHull(df, data, inputX, inputY)

elif inputDataset == 3 :
    data = datasets.load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    print("Available data :")
    print("1. Radius")
    print("2. Texture")
    print("3. Perimeter")
    print("4. Area")
    print("5. Smoothness")
    print("6. Compactness")
    print("7. Concavity")
    print("8. Concave Points")
    print("9. Symmetry")
    print("10. Fractal Dimension")
    inputX = int(input("Input x coordinate number : "))
    inputY = int(input("Input y coordinate number : "))
    ch.displayConvexHull(df, data, inputX, inputY)
else :
    print("Invalid Input.")


