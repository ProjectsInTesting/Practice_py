import openpyxl

# ---- 1. Define the Excel file path ------------------------
excel_file = "files/software_versions.xlsx"

# ---- 2. Load the Excel file and get the latest version ----
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook["Versions"]
latest_version = sheet["A" + str(sheet.max_row)].value  # Get the last version in the column

# ---- 3. Ask the user for the change type ------------------
change_type = input("Enter the change type (major, minor, patch): ").lower()

# ---- 4. Break the version text into separate strings ------
parts_as_text = latest_version.split(".")   # ["major", "minor", "patch"]

# ---- 5. Change the strings to numbers ---------------------
major_num = int(parts_as_text[0])
minor_num = int(parts_as_text[1])
patch_num = int(parts_as_text[2])

# ---- 6. Decide which number to bump -----------------------
if change_type == "major":
    major_num += 1
    minor_num = 0
    patch_num = 0
elif change_type == "minor":
    minor_num += 1
    patch_num = 0
elif change_type == "patch":
    patch_num += 1
else:
    print("Please use 'major', 'minor', or 'patch'.")
    exit()

# ---- 7. Turn the numbers back into strings ----------------
new_version_text = f"{major_num}.{minor_num}.{patch_num}"

# ---- 8. Save the new version to the Excel file ------------
sheet.append([new_version_text])  # Add the new version to the next row
workbook.save(excel_file)

# ---- 9. Show the result -----------------------------------
print(f"New version saved: {new_version_text}")
