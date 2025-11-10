import json
def load_candidates_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
    
def get_candidates(candidate_id, data):
    candidate_id = int(candidate_id)
    for i in data:
        if i["id"] == int(candidate_id):
            return i

def get_candidates_by_name(candidate_name, data):
    result = []
    for i in data:
        if candidate_name.lower() in i["name"].lower():
            result.append(i)
    return result

def get_candidates_by_skill(skill_name, data):
    result = []
    for i in data:
        if skill_name.lower() in i["skills"].lower().split(", "):
            result.append(i)
    return result

