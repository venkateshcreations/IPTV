
import json
import os

path2 = "Website-Clone-2/assets/data/india-channels.json"
path1_etv = "Website-Clone/assets/data/etv-channels.json"

with open(path2, "r", encoding="utf-8") as f:
    data2 = json.load(f)

# Remove ETV Telugu HD (any channel containing "ETV Telugu HD" in name)
keys_to_remove = [k for k, v in data2.items() if "ETV Telugu HD" in v.get("name", "")]
for k in keys_to_remove:
    del data2[k]
    print(f"Removed {k}")

# Add ETV Telugu and ETV Telugu Mirror from Website-Clone
if os.path.exists(path1_etv):
    with open(path1_etv, "r", encoding="utf-8") as f:
        etv_data = json.load(f)
        for k, v in etv_data.items():
            data2[k] = v
            print(f"Added {k}")

with open(path2, "w", encoding="utf-8") as f:
    json.dump(data2, f, separators=(",", ":"))
