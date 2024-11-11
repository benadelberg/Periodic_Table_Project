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
            writer.writerow({'Symbol': 'Be', 'Name': 'Beryllium', 'Atomic Number': 4, 'Atomic Weight': 9.0122})
            writer.writerow({'Symbol': 'B', 'Name': 'Boron', 'Atomic Number': 5, 'Atomic Weight': 10.81})
            writer.writerow({'Symbol': 'C', 'Name': 'Carbon', 'Atomic Number': 6, 'Atomic Weight': 12.011})
            writer.writerow({'Symbol': 'N', 'Name': 'Nitrogen', 'Atomic Number': 7, 'Atomic Weight': 14.007})
            writer.writerow({'Symbol': 'O', 'Name': 'Oxygen', 'Atomic Number': 8, 'Atomic Weight': 15.999})
            writer.writerow({'Symbol': 'F', 'Name': 'Fluorine', 'Atomic Number': 9, 'Atomic Weight': 18.998})
            writer.writerow({'Symbol': 'Ne', 'Name': 'Neon', 'Atomic Number': 10, 'Atomic Weight': 20.180})
            writer.writerow({'Symbol': 'Na', 'Name': 'Sodium', 'Atomic Number': 11, 'Atomic Weight': 22.990})
            writer.writerow({'Symbol': 'Mg', 'Name': 'Magnesium', 'Atomic Number': 12, 'Atomic Weight': 24.305})
            writer.writerow({'Symbol': 'Al', 'Name': 'Aluminium', 'Atomic Number': 13, 'Atomic Weight': 26.982})
            writer.writerow({'Symbol': 'Si', 'Name': 'Silicon', 'Atomic Number': 14, 'Atomic Weight': 28.085})
            writer.writerow({'Symbol': 'P', 'Name': 'Phosphorus', 'Atomic Number': 15, 'Atomic Weight': 30.974})
            writer.writerow({'Symbol': 'S', 'Name': 'Sulfur', 'Atomic Number': 16, 'Atomic Weight': 32.06})
            writer.writerow({'Symbol': 'Cl', 'Name': 'Chlorine', 'Atomic Number': 17, 'Atomic Weight': 35.45})
            writer.writerow({'Symbol': 'Ar', 'Name': 'Argon', 'Atomic Number': 18, 'Atomic Weight': 39.95})
            writer.writerow({'Symbol': 'K', 'Name': 'Potassium', 'Atomic Number': 19, 'Atomic Weight': 39.098})
            writer.writerow({'Symbol': 'Ca', 'Name': 'Calcium', 'Atomic Number': 20, 'Atomic Weight': 40.078})
            writer.writerow({'Symbol': 'Sc', 'Name': 'Scandium', 'Atomic Number': 21, 'Atomic Weight': 44.956})
            writer.writerow({'Symbol': 'Ti', 'Name': 'Titanium', 'Atomic Number': 22, 'Atomic Weight': 47.867})
            writer.writerow({'Symbol': 'V', 'Name': 'Vanadium', 'Atomic Number': 23, 'Atomic Weight': 50.942})
            writer.writerow({'Symbol': 'Cr', 'Name': 'Chromium', 'Atomic Number': 24, 'Atomic Weight': 51.996})
            writer.writerow({'Symbol': 'Mn', 'Name': 'Manganese', 'Atomic Number': 25, 'Atomic Weight': 54.938})
            writer.writerow({'Symbol': 'Fe', 'Name': 'Iron', 'Atomic Number': 26, 'Atomic Weight': 55.845})
            writer.writerow({'Symbol': 'Co', 'Name': 'Cobalt', 'Atomic Number': 27, 'Atomic Weight': 58.933})
            writer.writerow({'Symbol': 'Ni', 'Name': 'Nickel', 'Atomic Number': 28, 'Atomic Weight': 58.693})
            writer.writerow({'Symbol': 'Cu', 'Name': 'Copper', 'Atomic Number': 29, 'Atomic Weight': 63.46})
            writer.writerow({'Symbol': 'Zn', 'Name': 'Zinc', 'Atomic Number': 30, 'Atomic Weight': 65.38})
            writer.writerow({'Symbol': 'Ga', 'Name': 'Gallium', 'Atomic Number': 31, 'Atomic Weight': 69.723})
            writer.writerow({'Symbol': 'Ge', 'Name': 'Germanium', 'Atomic Number': 32, 'Atomic Weight': 72.630})
            writer.writerow({'Symbol': 'As', 'Name': 'Arsenic', 'Atomic Number': 33, 'Atomic Weight': 74.922})
            writer.writerow({'Symbol': 'Se', 'Name': 'Selenium', 'Atomic Number': 34, 'Atomic Weight': 78.971})
            writer.writerow({'Symbol': 'Br', 'Name': 'Bromine', 'Atomic Number': 35, 'Atomic Weight': 79.904})
            writer.writerow({'Symbol': 'Kr', 'Name': 'Krypton', 'Atomic Number': 36, 'Atomic Weight': 83.798})
            writer.writerow({'Symbol': 'Rb', 'Name': 'Rubidium', 'Atomic Number': 37, 'Atomic Weight': 85.468})
            writer.writerow({'Symbol': 'Sr', 'Name': 'Strontium', 'Atomic Number': 38, 'Atomic Weight': 87.92})
            writer.writerow({'Symbol': 'Y', 'Name': 'Yttrium', 'Atomic Number': 39, 'Atomic Weight': 88.906})
            writer.writerow({'Symbol': 'Zr', 'Name': 'Zirconium', 'Atomic Number': 40, 'Atomic Weight': 91.224})
            writer.writerow({'Symbol': 'Nb', 'Name': 'Niobium', 'Atomic Number': 41, 'Atomic Weight': 92.906})
            writer.writerow({'Symbol': 'Mo', 'Name': 'Molybdenum', 'Atomic Number': 42, 'Atomic Weight': 95.95})
            writer.writerow({'Symbol': 'Tc', 'Name': 'Technetium', 'Atomic Number': 43, 'Atomic Weight': 97})
            writer.writerow({'Symbol': 'Ru', 'Name': 'Ruthenium', 'Atomic Number': 44, 'Atomic Weight': 101.07})
            writer.writerow({'Symbol': 'Rh', 'Name': 'Rhodium', 'Atomic Number': 45, 'Atomic Weight': 102.91})
            writer.writerow({'Symbol': 'Pd', 'Name': 'Palladium', 'Atomic Number': 46, 'Atomic Weight': 106.42})
            writer.writerow({'Symbol': 'Ag', 'Name': 'Silver', 'Atomic Number': 47, 'Atomic Weight': 107.87})
            writer.writerow({'Symbol': 'Cd', 'Name': 'Cadmium', 'Atomic Number': 48, 'Atomic Weight': 112.41})
            writer.writerow({'Symbol': 'In', 'Name': 'Indium', 'Atomic Number': 49, 'Atomic Weight': 114.82})
            writer.writerow({'Symbol': 'Sn', 'Name': 'Tin', 'Atomic Number': 50, 'Atomic Weight': 118.71})
            writer.writerow({'Symbol': 'Sb', 'Name': 'Antimony', 'Atomic Number': 51, 'Atomic Weight': 121.76})
            writer.writerow({'Symbol': 'Te', 'Name': 'Tellurum', 'Atomic Number': 52, 'Atomic Weight': 127.60})
            writer.writerow({'Symbol': 'I', 'Name': 'Iodine', 'Atomic Number': 53, 'Atomic Weight': 126.90})
            writer.writerow({'Symbol': 'Xe', 'Name': 'Xenon', 'Atomic Number': 54, 'Atomic Weight': 131.29})
            writer.writerow({'Symbol': 'Cs', 'Name': 'Caesium', 'Atomic Number': 55, 'Atomic Weight': 132.91})
            writer.writerow({'Symbol': 'Ba', 'Name': 'Barium', 'Atomic Number': 56, 'Atomic Weight': 137.33})
            writer.writerow({'Symbol': 'La', 'Name': 'Lanthanum', 'Atomic Number': 57, 'Atomic Weight': 138.91})
            writer.writerow({'Symbol': 'Ce', 'Name': 'Cerium', 'Atomic Number': 58, 'Atomic Weight': 140.12})
            writer.writerow({'Symbol': 'Pr', 'Name': 'Praseodymium', 'Atomic Number': 59, 'Atomic Weight': 140.91})
            writer.writerow({'Symbol': 'Nd', 'Name': 'Neodymium', 'Atomic Number': 60, 'Atomic Weight': 144.24})
            print("Created periodic_table.csv")

    if not os.path.exists('compounds.csv'):
        with open('compounds.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Compound Name', 'Base Elements', 'Proportions'])
            writer.writeheader()
            writer.writerow({'Compound Name': 'Water', 'Base Elements': 'H2O', 'Proportions': '2 H, 1 O'})
            print("Created compounds.csv")

def load_elements(file_name):
    elements = {}
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            elements[row['Symbol']] = {
                'name': row['Name'],
                'atomic_number': int(row['Atomic Number']),
                'atomic_weight': float(row['Atomic Weight'])
            }
    return elements

def load_compounds(file_name):
    compounds = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            compounds.append({
                'name': row['Compound Name'],
                'elements': row['Base Elements'],
                'proportions': row['Proportions']
            })
    return compounds

def view_periodic_table(elements):
    for symbol, details in elements.items():
        print(f"{symbol}: {details['name']} (Atomic Number: {details['atomic_number']}, Atomic Weight: {details['atomic_weight']})")