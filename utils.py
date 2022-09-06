import json


def load_json() -> list[dict]:
    with open("candidates.json", 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates

def format_candidates(candidates: list[dict]) -> str:
    """Список кандидатов"""
    result = "<pre>"

    for candidate in candidates:
        result += f"""
                {candidate['name']}/n
                {candidate['positions']}/n
                {candidate['skills']}/n
                        """
    result += '</pre>'
    return result


def get_all_candidates() -> list[dict]:
    return load_json()


def get_candidate_id(uid: int):
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate

    return None


def get_candidate_skill(skill: str) -> list[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)

    return result
