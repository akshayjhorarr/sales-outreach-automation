import csv

def generate_email(name, company):
    return f"""
    Hi {name},

    I noticed {company} is growing rapidly and wanted to share how our solutions can help streamline your sales outreach.

    Would you be open to a quick call this week?

    Best,
    Gaurav
    """

with open("leads.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = generate_email(row["Name"], row["Company"])
        print(f"--- Email to {row['Email']} ---")
        print(email)