import csv
import os

def clean_csv():
    input_file = input("Enter csv file name: ").strip()

    if not input_file.endswith(".csv"):
        input_file += ".csv"

    input_path = f"data/{input_file}"
    print(input_path)

    try:
        with open("input_path", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            seen = set()
            cleaned_data = []

            for row in reader:
                name = row["name"].strip()
                email = row["email"].strip()

                #skipping missing values
                if not name or not email:
                    continue

                #creating a unique key
                row_key = (name, email)

                #skipping duplicate values
                if row_key in seen:
                    continue

                seen.add(row_key)

                cleaned_data.append({
                    "name": name,
                    "email": email,
                })

        os.makedirs("output", exist_ok=True)
        with open("output/cleaned_data.csv",
                          "w",
                          newline="",
                          encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "email"])
            writer.writeheader()
            writer.writerows(cleaned_data)

            print(
                        f"\nCleaning complete!"
                        f"\n Clean records: {len(cleaned_data)}"
                        f"\n Saved to output/cleaned_data.csv"
                    )

    except FileNotFoundError:
        print("CSV file not found")
    except KeyError:
        print("CSV must contain 'name' and 'email' columns")
clean_csv()