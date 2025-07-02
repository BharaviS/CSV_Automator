from datetime import datetime
import csv

FILENAME = "users.csv"
TODAY = datetime.now().strftime("%d-%m-%Y")
TIME = datetime.now().strftime("%I:%M:%S %p")


def write_csv():
    try:
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Email", "Joined_Date"])
            writer.writerow(["Bharavi", "bharavi@mymail.com", TODAY])
        print("✅ CSV file created and first user written.")
    except Exception as e:
        print(f"[ERROR] write_csv: {e}")


def append_csv():
    try:
        with open(FILENAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Charai", "chari@mymail.com", TODAY])
            writer.writerow(["Sai", "sai@mymail.com", TODAY])
        print("✅ More users appended to CSV.")
    except Exception as e:
        print(f"[ERROR] append_csv: {e}")


def read_csv():
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            print(f"\n📄 Current CSV Content:")
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("[ERROR] CSV file not found.")
    except Exception as e:
        print(f"[ERROR] read_csv: {e}")


if __name__ == "__main__":
    write_csv()
    append_csv()
    read_csv()