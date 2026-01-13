# main.py

from knowgle_base import SYMPTOMS, DISEASES
from rules import WEIGHTED_RULES
from forward_chaining import diagnose_best

def ask_symptoms():
    print("\n=== SISTEM PAKAR DIAGNOSIS PENYAKIT TANAMAN PADI ===")
    print("Metode: Forward Chaining (pilih 1 hasil terbaik)\n")

    facts = set()
    for code, question in SYMPTOMS.items():
        ans = input(f"{code} - {question} (y/n): ").strip().lower()
        if ans == "y":
            facts.add(code)
    return facts

def main():
    facts = ask_symptoms()
    best, scores, matched = diagnose_best(facts, WEIGHTED_RULES)

    print("\n==============================")
    if best is None:
        print(">>> HASIL: Tidak ditemukan penyakit yang cocok.")
    else:
        print(">>> HASIL DIAGNOSA (1 TERBAIK):")
        print(f"Penyakit : {DISEASES[best]['name']}")
        print(f"Solusi   : {DISEASES[best]['solution']}")

        print("\nDetail pencocokan (bukti penalaran):")
        for s, w in matched.get(best, []):
            print(f"- {s} (bobot {w}) -> {SYMPTOMS[s]}")
        print(f"\nSkor akhir: {scores[best]}")
    print("==============================\n")

if __name__ == "__main__":
    main()
