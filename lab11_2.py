
import json

cities = {
    "Київ": 482,
    "Чернігів": 907,
    "Львів": 1256,
    "Харків": 1654,
    "Одеса": 1794
}

with open("cities.json", "w", encoding="utf-8") as file:
    json.dump(cities, file, ensure_ascii=False, indent=4)

oldest_city = min(cities, key=cities.get)

print("Місто з найбільшим віком:", oldest_city)
print("Рік заснування:", cities[oldest_city])
print("Дані збережено у файл cities.json")
