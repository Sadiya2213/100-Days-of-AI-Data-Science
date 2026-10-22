base_tuple = ("Adenine","Guanine","Thymine")
print("1.Initial locked sequence:",base_tuple)

temp_list = list(base_tuple)
temp_list.append("Cytocine")
base_tuple=tuple(temp_list)

(base_1,base_2,base_3,base_4)=temp_list
print(f"2.Extracted core bases --> Base A: {base_1} , Base B: {base_2}")

print("\n--- Starting Automated Genome Scan Loop ---")
for base in temp_list:
    print(f"Scanning molecular structure for: {base}")
print("--- Scan Complete ---")