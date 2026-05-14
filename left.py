import json

name_path = r"data/cs2/names.json"

with open(name_path, "r", encoding="utf-8") as f:
    names = json.load(f)

total = 11841

existing_ids = {
    int(item["count_id"])
    for item in names
    if "count_id" in item
}

left_count_list = [
    i for i in range(total)
    if i not in existing_ids
]

print("已有数量:", len(existing_ids))
print("缺失数量:", len(left_count_list))
print("缺失 count_id:")
print(left_count_list)