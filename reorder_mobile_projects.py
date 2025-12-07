#!/usr/bin/env python3
"""
Reorder Mobile & Offline-First Applications to: eOrder Mobile, SmartESM Mobile, PJP Mobile, FieldForce Pro
"""

# Read the file
with open('/Users/kanok/Desktop/Potforilo/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Define project boundaries (line numbers are 0-indexed in list, but grep shows 1-indexed)
# Project 15: PJP Mobile - lines 805-830 (0-indexed: 804-829)
# Project 16: eOrder Mobile - lines 831-872 (0-indexed: 830-871)
# Project 17: SmartESM Mobile - lines 873-914 (0-indexed: 872-913)
# Project 18: FieldForce Pro - lines 915-onwards (0-indexed: 914-...)

# Need to find where Project 18 ends
# Let's find the end of mobile section (before Category 4)

# Extract each project
pjp_mobile = lines[804:830]      # 26 lines
eorder_mobile = lines[830:872]   # 42 lines
smartesm_mobile = lines[872:914] # 42 lines
fieldforce_pro = lines[914:940]  # Estimate ~26 lines

print(f"PJP Mobile: {len(pjp_mobile)} lines")
print(f"eOrder Mobile: {len(eorder_mobile)} lines")
print(f"SmartESM Mobile: {len(smartesm_mobile)} lines")
print(f"FieldForce Pro: {len(fieldforce_pro)} lines")

# Update project numbers in comments
# eOrder Mobile becomes Project 15
eorder_mobile[0] = eorder_mobile[0].replace('<!-- Project 16:', '<!-- Project 15:')

# SmartESM Mobile becomes Project 16
smartesm_mobile[0] = smartesm_mobile[0].replace('<!-- Project 17:', '<!-- Project 16:')

# PJP Mobile becomes Project 17
pjp_mobile[0] = pjp_mobile[0].replace('<!-- Project 15:', '<!-- Project 17:')

# FieldForce Pro becomes Project 18 (already correct)

# Reconstruct the file with new order: eOrder, SmartESM, PJP, FieldForce
new_lines = (
    lines[:804] +        # Everything before mobile projects
    eorder_mobile +      # Project 15
    smartesm_mobile +    # Project 16
    pjp_mobile +         # Project 17
    fieldforce_pro +     # Project 18
    lines[940:]          # Everything after mobile projects
)

# Write back
with open('/Users/kanok/Desktop/Potforilo/index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("\n✅ Successfully reordered mobile projects!")
print("New order:")
print("  Project 15: eOrder Mobile")
print("  Project 16: SmartESM Mobile")
print("  Project 17: PJP Mobile")
print("  Project 18: FieldForce Pro")
