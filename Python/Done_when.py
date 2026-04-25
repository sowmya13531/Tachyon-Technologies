import json

def load_data(file_name):
    with open(file_name, "r") as file:
        return json.load(file)

def filter_users(data, min_age):
    return [user for user in data if user["age"] > min_age]

def display_users(users):
    for user in users:
        print(f"{user['name']} - {user['age']}")

def main():
    data = load_data("data.json")
    filtered = filter_users(data, 21)
    display_users(filtered)

if __name__ == "__main__":
    main()