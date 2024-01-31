import pymysql
from pymysql import Error
import getpass

class BeverageStoreApp:
    def __init__(self, username):
        password = getpass.getpass("Enter your password: ")
        self.connection = self.connect_to_database(username, password)
        if self.connection is None:
            exit("Failed to connect to the database.")

    def connect_to_database(self, username, password):
        try:
            connection = pymysql.connect(
                host='localhost',
                database='beverage_store',
                user=username,
                password=password
            )
            return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def show_all_stores(self):
        try:
            cursor = self.connection.cursor()
            show_all_stores = "SELECT * from stores"
            cursor.execute(show_all_stores)
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            print("\nList of All Stores:")
            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))

        except Error as e:
            print(f"Error: {e}")

    def create_store(self):
        # Get store details from user
        new_store_id = input("Enter new store ID: ")
        new_address_street = input("Enter new store street address: ")
        new_address_city = input("Enter new store city: ")
        new_address_state = input("Enter new store state: ")
        new_address_zip_code = input("Enter new store zip code: ")
        new_start_date = input("Enter start date (YYYY-MM-DD): ")
        new_rent = input("Enter rent amount: ")

        try:
            cursor = self.connection.cursor()
            cursor.callproc('create_store', [new_store_id, new_address_street, new_address_city, new_address_state,
                                             new_address_zip_code, new_start_date, new_rent])
            self.connection.commit()  # Commit the transaction
            print("Store created successfully.")
        except Error as e:
            print(f"Error: {e}")

    def delete_store(self):
        # Get the store ID to delete from the user
        store_id_to_delete = input("Enter the Store ID to delete: ")

        try:
            cursor = self.connection.cursor()
            cursor.callproc('delete_Store_byID', [store_id_to_delete])
            self.connection.commit()  # Commit the transaction
            print("Store deleted successfully.")
        except Error as e:
            print(f"Error: {e}")

    def update_store_rent(self):
        # Get store ID and new rent amount from user
        store_id_to_update = input("Enter the Store ID for rent update: ")
        new_rent = input("Enter the new rent amount: ")

        try:
            cursor = self.connection.cursor()
            # Convert input to appropriate data types
            store_id_to_update = int(store_id_to_update)
            new_rent = float(new_rent)

            # Call the stored procedure
            cursor.callproc('update_rent', [store_id_to_update, new_rent])
            self.connection.commit()  # Commit the changes
            print("Store rent updated successfully.")
        except Error as e:
            print(f"Error: {e}")

        except ValueError:
            print("Invalid input. Please enter numerical values.")

    def read_store_by_id(self):
        store_id_to_read = input("Enter the Store ID to read: ")
        try:
            cursor = self.connection.cursor()
            cursor.callproc('ReadStore_byID', [int(store_id_to_read)])
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))

        except Error as e:
            print(f"Error: {e}")

    def read_store_by_state(self):
        state_to_read = input("Enter the State to read stores from: ")
        try:
            cursor = self.connection.cursor()
            cursor.callproc('ReadStore_byState', [state_to_read])
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))
        except Error as e:
            print(f"Error: {e}")

    def read_store_by_city(self):
        city_to_read = input("Enter the City to read stores from: ")
        try:
            cursor = self.connection.cursor()
            cursor.callproc('ReadStore_byCity', [city_to_read])
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))
        except Error as e:
            print(f"Error: {e}")

    def get_store_details(self):
        # Get the store ID from the user
        store_id = input("Enter the Store ID: ")

        try:
            cursor = self.connection.cursor()
            # Convert input to an integer
            store_id = int(store_id)

            # Call the stored procedure
            cursor.callproc('GetStoreDetails', [store_id])
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))
        except Error as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please enter a numerical Store ID.")

    def show_all_staff(self):
        try:
            cursor = self.connection.cursor()
            show_all_staff = "SELECT * from staff"
            cursor.execute(show_all_staff)
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            print("\nList of All Staff:")
            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))

        except Error as e:
            print(f"Error: {e}")

    def create_staff(self):
        # Get staff details from user
        new_staff_id = input("Enter new staff ID: ")
        new_first_name = input("Enter staff's first name: ")
        new_last_name = input("Enter staff's last name: ")
        new_position = input("Enter staff's position: ")
        new_hire_date = input("Enter staff's hire date (YYYY-MM-DD): ")
        new_payroll = input("Enter staff's payroll: ")
        work_at_store_id = input("Enter store ID where staff will work: ")

        try:
            cursor = self.connection.cursor()
            # Convert input to appropriate data types
            new_staff_id = int(new_staff_id)
            new_payroll = float(new_payroll)
            work_at_store_id = int(work_at_store_id)

            # Call the stored procedure
            cursor.callproc('create_new_staff',
                            [new_staff_id, new_first_name, new_last_name, new_position, new_hire_date, new_payroll,
                             work_at_store_id])
            self.connection.commit()  # Commit the changes
            print("New staff member created successfully.")
        except Error as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please ensure all inputs are correct and try again.")

    def delete_staff(self):
        # Get the staff ID to delete from the user
        staff_id_to_delete = input("Enter the Staff ID to delete: ")

        try:
            cursor = self.connection.cursor()
            # Convert input to an integer
            staff_id_to_delete = int(staff_id_to_delete)

            # Call the stored procedure
            cursor.callproc('delete_staff_byID', [staff_id_to_delete])
            self.connection.commit()  # Commit the transaction
            print("Staff member deleted successfully.")
        except Error as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please enter a numerical Staff ID.")

    def update_staff_position(self):
        staff_id = input("Enter the Staff ID to update position: ")
        new_position = input("Enter the new position: ")

        try:
            cursor = self.connection.cursor()
            cursor.callproc('update_position', [int(staff_id), new_position])
            self.connection.commit()
            print("Staff position updated successfully.")
        except Error as e:
            print(f"Error: {e}")

    def update_staff_payroll(self):
        staff_id = input("Enter the Staff ID to update payroll: ")
        new_payroll = input("Enter the new payroll amount: ")

        try:
            cursor = self.connection.cursor()
            cursor.callproc('update_payroll', [int(staff_id), float(new_payroll)])
            self.connection.commit()
            print("Staff payroll updated successfully.")
        except Error as e:
            print(f"Error: {e}")

    def update_staff_workplace(self):
        staff_id = input("Enter the Staff ID to update workplace: ")
        new_workplace_id = input("Enter the new workplace ID: ")

        try:
            cursor = self.connection.cursor()
            cursor.callproc('update_work_place', [int(staff_id), int(new_workplace_id)])
            self.connection.commit()
            print("Staff workplace updated successfully.")
        except Error as e:
            print(f"Error: {e}")

    # problems here
    def read_staff_by_position(self):
        staff_position = input("Enter the position to find staff: ")

        try:
            cursor = self.connection.cursor()
            cursor.callproc('readStaff_byPosition', [staff_position])
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))

        except Error as e:
            print(f"Error: {e}")

    # problems here
    def read_staff_by_store_id(self):
        store_id = input("Enter the Store ID to find staff: ")

        try:
            cursor = self.connection.cursor()
            cursor.callproc('readStaff_byStoreID', [int(store_id)])
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))

        except Error as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please enter a numerical Store ID.")

    def show_all_products(self):
        try:
            cursor = self.connection.cursor()
            show_all_products = "SELECT * from products"
            cursor.execute(show_all_products)
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            print("\nList of All Products:")
            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))

        except Error as e:
            print(f"Error: {e}")

    def create_product(self):
        # Get product details from user
        new_product_name = input("Enter new product name: ")
        new_product_price = input("Enter new product price: ")
        new_category = input("Enter product category: ")

        try:
            cursor = self.connection.cursor()
            # Convert input to appropriate data types
            new_product_price = float(new_product_price)

            # Call the stored procedure
            cursor.callproc('create_new_product', [new_product_name, new_product_price, new_category])
            self.connection.commit()  # Commit the changes
            print("New product created successfully.")
        except Error as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please ensure all inputs are correct and try again.")

    def read_product_by_category(self):
        category = input("Enter the product category to search for: ")

        try:
            cursor = self.connection.cursor()
            cursor.callproc('readProduct_byCategory', [category])
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))

        except Error as e:
            print(f"Error: {e}")

    def read_product_by_price_range(self):
        try:
            price_lower_limit = float(input("Enter the lower limit of the price range: "))
            price_upper_limit = float(input("Enter the upper limit of the price range: "))

            cursor = self.connection.cursor()
            cursor.callproc('readProduct_byPriceRange', [price_lower_limit, price_upper_limit])
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))

        except Error as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please enter numerical values for the price range.")

    def display_all_ingredients(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT DISTINCT ingredient_name FROM ingredients ORDER BY ingredient_name")
            ingredients = cursor.fetchall()

            print("\nAvailable Ingredients:")
            for ingredient in ingredients:
                print(ingredient[0])
        except Error as e:
            print(f"Error retrieving ingredients: {e}")

    def read_product_by_ingredient(self):
        # First display all available ingredients
        self.display_all_ingredients()

        # Then, prompt the user to enter an ingredient
        ingredient_name = input("\nEnter the ingredient to search for products: ")

        try:
            cursor = self.connection.cursor()
            cursor.callproc('readProduct_byIngredient', [ingredient_name])
            rows = cursor.fetchall()

            if not rows:
                print(f"No products found with the ingredient: {ingredient_name}")
                return

            column_names = [description[0] for description in cursor.description]

            # Determine the maximum width for each column
            column_widths = []
            for i in range(len(column_names)):
                column_width = max(len(column_names[i]), max(len(str(row[i])) for row in rows))
                column_widths.append(column_width)

            # Print table header
            header = " | ".join(column.ljust(column_widths[i]) for i, column in enumerate(column_names))
            print(header)
            print("-" * len(header))  # Line to separate headers from rows

            # Print table rows
            for row in rows:
                formatted_row = [str(cell).ljust(column_widths[i]) for i, cell in enumerate(row)]
                print(" | ".join(formatted_row))

        except Error as e:
            print(f"Error: {e}")

    def update_product_price(self):
        product_name = input("Enter the product name to update price: ")
        try:
            new_price = float(input("Enter the new price for the product: "))

            cursor = self.connection.cursor()
            cursor.callproc('update_product_price', [product_name, new_price])
            self.connection.commit()
            print("Product price updated successfully.")
        except Error as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please enter a numerical value for the price.")

    def delete_product(self):
        product_name = input("Enter the product name to delete: ")

        try:
            cursor = self.connection.cursor()
            cursor.callproc('delete_product', [product_name])
            self.connection.commit()
            print("Product deleted successfully.")
        except Error as e:
            print(f"Error: {e}")
