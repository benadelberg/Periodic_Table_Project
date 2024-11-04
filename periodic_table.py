import csv
import os

def create_csv_files():
    if not os.path.exists('periodic_table.csv'):
        with open('periodic_table.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Symbol', 'Name', 'Atomic Number', 'Atomic Weight'])
            writer.writeheader()
            writer.writerow({'Symbol': 'H', 'Name': 'Hydrogen', 'Atomic Number': 1, 'Atomic Weight': 1.0080})
            writer.writerow({'Symbol': 'He', 'Name': 'Helium', 'Atomic Number': 2, 'Atomic Weight': 4.0026})
            writer.writerow({'Symbol': 'Li', 'Name': 'Lithium', 'Atomic Number': 3, 'Atomic Weight': 6.94})
            writer.writerow({'Symbol': 'Be', 'Name': 'Berylliu', 'Atomic Number': 4, 'Atomic Weight': 9.0122})
            writer.writerow({'Symbol': 'B', 'Name': 'Boron', 'Atomic Number': 5, 'Atomic Weight': 10.81})
            writer.writerow({'Symbol': 'C', 'Name': 'Carbon', 'Atomic Number': 6, 'Atomic Weight': 12.011})
            writer.writerow({'Symbol': 'N', 'Name': 'Nitrogen', 'Atomic Number': 7, 'Atomic Weight': 14.007})
            writer.writerow({'Symbol': 'O', 'Name': 'Oxygen', 'Atomic Number': 8, 'Atomic Weight': 15.999})
            writer.writerow({'Symbol': 'F', 'Name': 'Fluorine', 'Atomic Number': 9, 'Atomic Weight': 18.998})
            writer.writerow({'Symbol': 'Ne', 'Name': 'Neon', 'Atomic Number': 10, 'Atomic Weight': 20.180})
            print("Created periodic_table.csv")

    if not os.path.exists('compounds.csv'):
        with open('compounds.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Compound Name', 'Base Elements', 'Proportions'])
            writer.writeheader()
            writer.writerow({'Compound Name': 'Water', 'Base Elements': 'H2O', 'Proportions': '2 H, 1 O'})
            print("Created compounds.csv")