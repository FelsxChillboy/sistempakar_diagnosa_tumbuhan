# forward_chaining.py

from collections import defaultdict

def diagnose_best(facts, weighted_rules):
    """
    facts: set gejala True, contoh {"G01","G03","G12"}
    weighted_rules: list of {"disease","symptom","weight"}

    return: (best_disease, score_dict, matched_details)
    """
    scores = defaultdict(float)
    matched = defaultdict(list)

    for r in weighted_rules:
        if r["symptom"] in facts:
            scores[r["disease"]] += float(r.get("weight", 1.0))
            matched[r["disease"]].append((r["symptom"], float(r.get("weight", 1.0))))

    if not scores:
        return None, {}, {}

    # pilih skor tertinggi; kalau seri, pilih yang jumlah gejala match lebih banyak
    best = sorted(
        scores.keys(),
        key=lambda d: (scores[d], len(matched[d])),
        reverse=True
    )[0]

    return best, dict(scores), dict(matched)
