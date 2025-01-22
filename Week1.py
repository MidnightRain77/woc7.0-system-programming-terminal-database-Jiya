#Working with json less goo
import json

'''data = {"name": "Jiya", "age": 19}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    loaded_data = json.load(file)
print("Loaded Data:", loaded_data)'''


#OOP Concepts
'''class KeyValueStore:
    def __init__(self):
        self.store = {}

    def add(self, key, value):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key, "Not Found")

kv = KeyValueStore()
kv.add("language", "Python")
print(kv.get("language"))'''


# OOP Key-Value Store with JSON
class KeyValueStore:
    def __init__(self, filename):
        self.filename = filename
        self.store = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.store = json.load(file)
        except FileNotFoundError:
            self.store = {}

    def add(self, key, value):
        self.store[key] = value
        self.save_data()
        print(f"Added key: '{key}', value: '{value}'")

    def get(self, key):
        return self.store.get(key, "Not Found")

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.store, file, indent=4)
        print(f"Data saved to {self.filename}")


if __name__ == "__main__":
    kv_store = KeyValueStore("data.json")

    kv_store.add("name", "Jiya")
    kv_store.add("age", 19)
    kv_store.add("language", "Python in PyCharm")
    kv_store.add("city", "Himatnagar")

    print("Name:", kv_store.get("name"))
    print("Age:", kv_store.get("age"))
    print("Language:", kv_store.get("language"))
    print("Country:", kv_store.get("country"))
