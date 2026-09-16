# =============================================
# STRINGS
# =============================================
print("="*60)
print("STRINGS")
print("="*60)
print()


myName="Suryansh Singh"
print(f"myName : {myName}")

uniCode = ord(myName[0])
print(f"Unicode of the first letter of myName : {myName} = {uniCode}")
charCode = chr(uniCode)
print(f"Character at the unicode : {uniCode} = {charCode}")
print()

print(f"1. String without slicing : {myName}")
print(f"2. String slicing : first letter : {myName[0]}")
print(f"3. String slicing : print Everything according to index : {myName[0 : 15 : 1]}")
print(f"4. String slicing : print Everything according to index but at step 2 : {myName[0 : 15 : 2]}")
print(f"5. String slicing : print Everything according to index in negative index : {myName[-16 : -1 : 1]}")


