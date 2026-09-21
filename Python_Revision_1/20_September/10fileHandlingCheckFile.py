# =============================================
# 9. CHECK FILE EXISTS — WITHOUT 'with'
# =============================================
print("="*60)
print("9. CHECK FILE EXISTS")
print("="*60)
print()

import os

if os.path.exists("demo.txt"):
    print("demo.txt exists")
else:
    print("demo.txt does not exist")
print()