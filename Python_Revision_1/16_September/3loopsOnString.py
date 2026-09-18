# =============================================
# FOR LOOPS ON STRINGS
# =============================================
print("="*60)
print("FOR LOOPS ON STRINGS")
print("="*60)
print()

name = "Surya"
print(f"Value of name : {name}")
print(f"Length of name : {len(name)}")
print()



# WAY 1 : USING INDEX VALUES (range + indexing)
print("WAY 1 : USING INDEX VALUES")
print()

for i in range(len(name)):
    print(f"Index {i} : {name[i]}")
print()


# WAY 2 : ITERATING DIRECTLY OVER THE STRING
print("WAY 2 : ITERATING DIRECTLY OVER THE STRING")
print()

for ch in name:
    print(f"Character : {ch}")
print()



# range(0, len(name), 1)
print("range(0, len(name), 1)")
print()

for i in range(0, len(name), 1):
    print(f"Index {i} : {name[i]}")
print()


# REVERSE : range(len(name)-1, -1, -1)
print("range(len(name)-1, -1, -1)")
print()

for i in range(len(name)-1, -1, -1):
    print(f"Index {i} : {name[i]}")
print()


# 3. STEP 2 (ALTERNATE) : range(0, len(name), 2)
print("range(0, len(name), 2)")
print()

for i in range(0, len(name), 2):
    print(f"Index {i} : {name[i]}")
print()


