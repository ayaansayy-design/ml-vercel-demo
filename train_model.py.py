from sklearn.linear_model import LinearRegression
import pickle

# Training data (very simple)
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

model = LinearRegression()
model.fit(X, y)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model created successfully!")
