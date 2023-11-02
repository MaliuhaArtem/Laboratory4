class Smartphone:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year
    def years_since_release(self):
        return 2023 - self.release_year
class Shop:
    def __init__(self):
        self.smartphones = []
    def add_smartphone(self, smartphone):
        self.smartphones.append(smartphone)
    def remove_smartphone(self, smartphone):
        if smartphone in self.smartphones:
            self.smartphones.remove(smartphone)
    def smartphones_after_year(self, year):
        return [s for s in self.smartphones if s.release_year >= year]
if __name__ == "__main__":
    shop = Shop()
    while True:
        name = input("Введіть назву смартфона (або 'q' для завершення): ")
        if name == 'q':
            break
        release_year = int(input("Введіть рік випуску смартфона: "))
        smartphone = Smartphone(name, release_year)
        shop.add_smartphone(smartphone)
    year_to_filter = int(input("Введіть рік для фільтрації: "))
    filtered_smartphones = shop.smartphones_after_year(year_to_filter)
    print("Смартфони, випущені у {} році або пізніше:".format(year_to_filter))
    if not filtered_smartphones:
        print("Не знайдено жодного смартфона.")
    else:
        for smartphone in filtered_smartphones:
            print("{} - рік випуску: {}. Пройшло {} років з випуску.".format(smartphone.name, smartphone.release_year, smartphone.years_since_release()))
    name_to_delete = input("Введіть назву смартфона для видалення (або 'q' для завершення): ")
    if name_to_delete != 'q':
        for smartphone in shop.smartphones:
            if smartphone.name == name_to_delete:
                shop.remove_smartphone(smartphone)
                print("Смартфон {} був видалений.".format(smartphone.name))

