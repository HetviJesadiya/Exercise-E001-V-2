'''
Exercise: E001-V2
•	Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.
•	Add a new member function to generate “display_name”.
•	“display_name” has the text value as below.
          1.	Vehicle category without parent then “Vehicle” 
          2.	Car category with “Vehicle” as a parent then “Vehicle > Car”
          3.	Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”
•	Create 5 category objects with parent and child relation.
•	Create 3 product objects in each category.
•	Display Category with its Code, Display Name and all product details inside that category.
•	Display product list by category (group by category, order by category name).
'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} {self.price}"


class Category:
    category_counter = 1000  

    def __init__(self, name, parent=None, products=None):
        self.code = Category.category_counter
        Category.category_counter += 1
        self.name = name
        self.parent = parent
        self.display_name = self.generate_display_name()
        self.products = products if products else[]

    def generate_display_name(self):
        return f"{self.parent.display_name} > {self.name}" if self.parent else self.name


    def __str__(self):
        product_list = "\n  ".join(map(str, self.products)) if self.products else "No Products"
        return f"{self.code} | {self.display_name}\n  {product_list}"



vehicle = Category("Vehicle")
car = Category("Car", vehicle)
bike = Category("Bike", vehicle)
suv = Category("SUV", car)
electric_bike = Category("Electric Bike", bike)


vehicle.products = [
    Product("Pickup Truck ","Price : 48000"), 
    Product("School Bus ", "Price : 70000"), 
    Product("Luxury SUV ", "Price : 45000")
    ]

car.products = [
    Product("Tesla Model 3 ", "Price : 40000"),
    Product("Honda Accord ", "Price : 27000"), 
    Product("Chevrolet Camaro ", "Price : 52000")
    ]

bike.products = [
    Product("Royal Enfield ", "Price : 16000"),
    Product("KTM Duke ", "Price : 18000"), 
    Product("Suzuki Hayabusa ", "Price : 25000")
    ]

suv.products = [
    Product("Range Rover ", "Price : 90000"), 
    Product("Toyota Fortuner ", "Price : 45000"), 
    Product("Ford Explorer ", "Price : 60000")
    ]

electric_bike.products = [
    Product("Revolt RV400 ", "Price : 12000"), 
    Product("Ultraviolette F77 ", "Price : 15000"), 
    Product("Hero Electric Photon ", "Price : 8000")
    ]


categories = [vehicle, car, bike, suv, electric_bike]

for i in range(len(categories)):
    for j in range(0, len(categories) - i - 1):
        if categories[j].name > categories[j + 1].name:
            categories[j], categories[j + 1] = categories[j + 1], categories[j]


for category in categories:
    print(category)
    print("-" * 50)