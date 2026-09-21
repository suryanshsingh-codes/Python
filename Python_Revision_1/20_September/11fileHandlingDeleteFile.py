# =============================================
# 10. DELETE FILE
# =============================================
print("="*60)
print("10. DELETE FILE")
print("="*60)
print()

import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("newfile.txt deleted successfully")
else:
    print("newfile.txt does not exist")
print()