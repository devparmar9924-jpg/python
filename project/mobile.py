mobiles = []
def add_mobile():
    id = int(input("Enter Mobile ID: "))
    brand = input("Enter Brand: ")
    model = input("Enter Model: ")
    ram = input("Enter RAM: ")
    storage = input("Enter Storage: ")
    price = int(input("Enter Price: "))
    stock = int(input("Enter Stock: "))
    mobile = {
        "id": id,
        "brand": brand,
        "model": model,
        "ram": ram,
        "storage": storage,
        "price": price,
        "stock": stock
    }
    mobiles.append(mobile)
    print("Mobile added successfully!")

def display_mobile():
    for mobile in mobiles:
        print(mobile)

def search_mobile():
    id = int(input("Enter Mobile ID: "))
    for mobile in mobiles:
        if mobile["id"] == id:
            print(mobile)
            return
    print("Mobile not found!")


def update_price():
    id = int(input("Enter Mobile ID: "))
    new_price = int(input("Enter New Price: "))
    for mobile in mobiles:
        if mobile["id"] == id:
            mobile["price"] = new_price
            print("Price updated successfully!")
            return
    print("Mobile not found!")

def delete_mobile():
    id = int(input("Enter Mobile ID: "))
    for mobile in mobiles:
        if mobile["id"] == id:
            mobiles.remove(mobile)
            print("Mobile deleted successfully!")
            return
    print("Mobile not found!")