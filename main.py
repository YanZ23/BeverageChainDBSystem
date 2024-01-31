from functions import *


def main():
    username = input("Enter MySQL username: ")

    app = BeverageStoreApp(username)

    while True:
        print("\nWhat would you like to manage?")
        print("1. Store")
        print("2. Staff")
        print("3. Product")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            app.show_all_stores()
            store_menu(app)
        elif choice == '2':
            app.show_all_staff()
            staff_menu(app)
        elif choice == '3':
            app.show_all_products()
            product_menu(app)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

    app.close_connection()


def store_menu(app):
    while True:
        print("\nStore Operations")
        print("1. Create Store")
        print("2. View Stores")
        print("3. Update Store")
        print("4. Delete Store")
        print("5. Return to Main Menu")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            app.create_store()
        elif choice == '2':
            view_stores_menu(app)
        elif choice == '3':
            app.update_store_rent()
        elif choice == '4':
            app.delete_store()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def view_stores_menu(app):
    while True:
        print("\nView Stores Options")
        print("1. View Store by ID")
        print("2. View Stores by State")
        print("3. View Stores by City")
        print("4. View Stores Detailed Info")
        print("5. Return to Store Menu")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            app.read_store_by_id()
        elif choice == '2':
            app.read_store_by_state()
        elif choice == '3':
            app.read_store_by_city()
        elif choice == '4':
            app.get_store_details()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def staff_menu(app):
    while True:
        print("\nStaff Operations")
        print("1. Create Staff")
        print("2. View Staff")
        print("3. Update Staff")
        print("4. Delete Staff")
        print("5. Return to Main Menu")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            app.create_staff()
        elif choice == '2':
            view_staff_menu(app)
        elif choice == '3':
            update_staff_menu(app)
        elif choice == '4':
            app.delete_staff()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def update_staff_menu(app):
    while True:
        print("\nUpdate Staff Options")
        print("1. Update Staff's Position")
        print("2. Update Staff's Payroll")
        print("3. Update Staff's Workplace")
        print("4. Return to Staff Menu")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            app.update_staff_position()
        elif choice == '2':
            app.update_staff_payroll()
        elif choice == '3':
            app.update_staff_workplace()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


def view_staff_menu(app):
    while True:
        print("\nView Staff Options")
        print("1. View Staff by Position")
        print("2. View Staff by Store")
        print("3. Return to Staff Menu")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            app.read_staff_by_position()
        elif choice == '2':
            app.read_staff_by_store_id()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


def product_menu(app):
    while True:
        print("\nProduct Operations")
        print("1. Create Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Return to Main Menu")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            app.create_product()
        elif choice == '2':
            view_products_menu(app)
        elif choice == '3':
            app.update_product_price()
        elif choice == '4':
            app.delete_product()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def view_products_menu(app):
    while True:
        print("\nView Products Options")
        print("1. View Products by Category")
        print("2. View Products by Price Range")
        print("3. View Products by Ingredient")
        print("4. Return to Products Menu")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            app.read_product_by_category()
        elif choice == '2':
            app.read_product_by_price_range()
        elif choice == '3':
            app.read_product_by_ingredient()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
