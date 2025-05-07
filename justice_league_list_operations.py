# Initial list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Step 1 - Initial list:")
print(justice_league)

# Step 2: Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\nStep 2 - After adding Batgirl and Nightwing:")
print(justice_league)

# Step 3: Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\nStep 3 - Wonder Woman is the leader:")
print(justice_league)

# Step 4: Separate Aquaman and Flash
flash_index = justice_league.index("Flash")
aquaman_index = justice_league.index("Aquaman")
min_index = min(flash_index, aquaman_index)
max_index = max(flash_index, aquaman_index)
justice_league.insert(min_index + 1, "Superman")
print("\nStep 4 - Conflict resolved by inserting Superman between Flash and Aquaman:")
print(justice_league)

# Step 5: Replace with a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nStep 5 - New team assembled by Superman:")
print(justice_league)

# Step 6: Sort alphabetically
justice_league.sort()
print("\nStep 6 - Alphabetically sorted team (new leader is at index 0):")
print(justice_league)
