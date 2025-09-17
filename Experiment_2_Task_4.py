# Updated nested dictionary (beginner-friendly) for IIIT Ranchi with added names.
org = {
    "Administration": {
        "Director": "Prof. Rajeev Srivastava",
        "Registrar": "Registrar (In-Charge)"
    },
    "Departments": {
        "Computer Science & Engineering": {
            "HoD": "Dr. Kirti Kumari",
            "Faculty": {
                "Professors": ["Prof. Rajeev Srivastava"],
                "Associate Professors": [],
                "Assistant Professors": [
                    "Dr. Dhananjoy Bhakta",
                    "Dr. Jayadeep Pati",
                    "Dr. Roshan Singh",
                    "Dr. Rashmi Panda",
                    "Dr. Bharat Singh",
                    "Dr. Priyank Khare",
                    "Dr. Kirti Kumari",
                    "Dr. Tarun Biswas",
                    "Dr. Ranjan Kumar Behera",
                    "Dr. Gaurav Sundaram",
                    "Dr. Akash Srivastava",
                    "Dr. N. Kishore Babu",      
                    "Kishore Babu Nampalle",    
                    "Dr. Nitika Nigam",        
                    "Dr. Ankita Kumari",
                    "Dr. Rajesh Dwivedi",
                    "Dr. Anuj Singh",
                    "Dr. Rishikesh Dutta Tiwary"
                ]
            }
        },
        "Electronics & Communication Engineering": {
            "HoD": "Dr. Santosh Kumar Mahto",
            "Faculty": {
                "Professors": [],
                "Associate Professors": [],
                "Assistant Professors": [
                    "Dr. Santosh Kumar Mahto",
                    "Dr. Shashi Kant Sharma",
                    "Dr. Jitendra Kumar Mishra",
                    "Dr. Rajiv Kumar",
                    "Dr. Priyabrat Garanayak",
                    "Dr. Nishit Malviya",
                    "Dr. Puja Ghosh",
                    "Dr. Manju Mathew",
                    "Dr. Gaurav Sundaram",
                    "Dr. Akash Srivastava"
                ]
            }
        },
        "Sciences": {
            "HoD": "Dr. Sandhir Kumar Singh",
            "Faculty": {
                "Professors": [],
                "Associate Professors": [],
                "Assistant Professors": [
                    "Dr. Sandhir Kumar Singh",
                    "Dr. Puja Ghosh",
                    "Dr. Rohit Kandulna",
                    "Dr. Rishikesh Dutta Tiwary",
                    "Dr. Shahid Shadab Hassan"
                ]
            }
        },
        "Humanities & Management": {
            "HoD": "Dr. Sandhir Kumar Singh",
            "Faculty": {
                "Professors": [],
                "Associate Professors": [],
                "Assistant Professors": [
                    "Dr. Noopur",
                    "Dr. Manju Mathew"
                ]
            }
        }
    }
}

# Simple search (no functions) - case-insensitive exact and some alternate-name matches included.
print("Search for an Assistant Professor at IIIT Ranchi")
print("Type 'exit' or 'quit' to stop.\n")

while True:
    name_input = input("Enter the Assistant Professor's full name: ").strip()
    if not name_input:
        print("Please enter a name or type 'exit' to quit.")
        continue
    if name_input.lower() in ("exit", "quit"):
        print("Exiting. Bye!")
        break

    search_name = name_input.lower()
    found = False

    # 1) Check Administration top-level (just in case)
    for role, person in org["Administration"].items():
        if isinstance(person, str) and person.lower() == search_name:
            print(f"Found '{name_input}' in Administration as {role}.")
            found = True
            break
    if found:
        continue

    # 2) Iterate departments (level-by-level)
    for dept_name, dept_info in org["Departments"].items():
        # check HoD
        hod = dept_info.get("HoD", "")
        if isinstance(hod, str) and hod.lower() == search_name:
            print(f"Found '{name_input}' — Department: {dept_name} (HoD).")
            found = True
            break

        # check faculty groups (Professors, Associate Professors, Assistant Professors)
        faculty_groups = dept_info.get("Faculty", {})
        for group_name, members in faculty_groups.items():
            if isinstance(members, list):
                for mem in members:
                    if mem.lower() == search_name:
                        print(f"Found '{name_input}' — Department: {dept_name} (as {group_name}).")
                        found = True
                        break
            if found:
                break
        if found:
            break

    # 3) If not found after searching all levels:
    if not found:
        print(f"Assistant Professor '{name_input}' was not found in the current structure. 🔍")
    # loop continues so user can search again or type 'exit'
