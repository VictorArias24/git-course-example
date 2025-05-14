import pickle


list_data = [
    {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 25,
        "email": "jane.smith@example.com"
    }
]


with open("dataset.pkl", "wb") as f:
    pickle.dump(list_data, f)

