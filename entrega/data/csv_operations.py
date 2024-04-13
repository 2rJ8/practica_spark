import csv
import os

# Function to create a new CSV file with sample data
class csv_op:
    def __init__(self, file_dir):
        self.file_dir = file_dir

    
    def create_csv_file(self,data):
        
        with open(self.file_dir, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            
        print(f"Created {self.file_dir}")

    # Function to read and display the content of a CSV file
    def read_csv_file(self):
        with open(self.file_dir, 'r',encoding="utf8") as file:
            reader = csv.reader(file)
            data=[]
            for row in reader:
                data.append(row)
                print(row)
            return data

    # Function to modify a CSV file by adding a new row
    def modify_csv_file(self, new_data):
        with open(self.file_dir, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_data)
        print(f"Modified {self.file_dir} by adding a new row")

    # Function to delete a CSV file
    def delete_csv_file(self):
        if os.path.exists(self.file_dir):
            os.remove(self.file_dir)
            print(f"Deleted {self.file_dir}")
        else:
            print(f"{self.file_dir} does not exist.")

    # Function to override a CSV file with new data
    def override_csv_file(self, new_data):
        with open(self.file_dir, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
        print(f"Overridden {self.file_dir} with new data")
