#!/usr/bin/env python3
"""
Reorder AI & ML projects to: ContentAI Pro, HelpDesk AI, BeverageVision AI, GoldMind AI
"""

# Read the file
with open('/Users/kanok/Desktop/Potforilo/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Define project boundaries (line numbers are 0-indexed in list, but grep shows 1-indexed)
# Project 11: HelpDesk AI - lines 641-688 (0-indexed: 640-687)
# Project 12: BeverageVision AI - lines 689-714 (0-indexed: 688-713)
# Project 13: GoldMind AI - lines 715-740 (0-indexed: 714-739)
# Project 14: ContentAI Pro - lines 741-788 (0-indexed: 740-787)

# Extract each project
helpdesk_ai = lines[640:688]  # 48 lines
beverage_ai = lines[688:714]  # 26 lines
goldmind_ai = lines[714:740]  # 26 lines
contentai_pro = lines[740:788]  # 48 lines

print(f"HelpDesk AI: {len(helpdesk_ai)} lines")
print(f"BeverageVision AI: {len(beverage_ai)} lines")
print(f"GoldMind AI: {len(goldmind_ai)} lines")
print(f"ContentAI Pro: {len(contentai_pro)} lines")

# Update project numbers in comments
# ContentAI Pro becomes Project 11
contentai_pro[0] = contentai_pro[0].replace('<!-- Project 14:', '<!-- Project 11:')

# HelpDesk AI becomes Project 12
helpdesk_ai[0] = helpdesk_ai[0].replace('<!-- Project 11:', '<!-- Project 12:')

# BeverageVision AI becomes Project 13
beverage_ai[0] = beverage_ai[0].replace('<!-- Project 12:', '<!-- Project 13:')

# GoldMind AI becomes Project 14
goldmind_ai[0] = goldmind_ai[0].replace('<!-- Project 13:', '<!-- Project 14:')

# Reconstruct the file with new order: ContentAI, HelpDesk, BeverageVision, GoldMind
new_lines = (
    lines[:640] +  # Everything before AI projects
    contentai_pro +  # Project 11
    helpdesk_ai +    # Project 12
    beverage_ai +    # Project 13
    goldmind_ai +    # Project 14
    lines[788:]      # Everything after AI projects
)

# Write back
with open('/Users/kanok/Desktop/Potforilo/index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("\n✅ Successfully reordered AI projects!")
print("New order:")
print("  Project 11: ContentAI Pro")
print("  Project 12: HelpDesk AI")
print("  Project 13: BeverageVision AI")
print("  Project 14: GoldMind AI")
