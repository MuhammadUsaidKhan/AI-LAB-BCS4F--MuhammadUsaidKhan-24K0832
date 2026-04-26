#LAB 10 Task 02
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
df = pd.read_csv("/content/spam.csv")
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['Message'])
y = df['Category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = SVC(kernel='linear')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\n--- Model Performance ---")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

new_email = ["Congratulations! You won a free iPhone"]
new_email_vec = vectorizer.transform(new_email)
prediction = model.predict(new_email_vec)
print("\nSpam Prediction (1=Spam, 0=Not Spam):", prediction[0])
