# rules.py

WEIGHTED_RULES = [
    # =========================
    # K01 - Bercak dan Daun Coklat
    # (yang dari tabel basis pengetahuan yang Anda punya)
    # =========================
    {"disease": "K01", "symptom": "G03", "weight": 1.0},
    {"disease": "K01", "symptom": "G02", "weight": 0.5},
    {"disease": "K01", "symptom": "G01", "weight": 1.0},
    {"disease": "K01", "symptom": "G08", "weight": 0.5},
    {"disease": "K01", "symptom": "G06", "weight": 0.0},
    {"disease": "K01", "symptom": "G09", "weight": 0.0},
    {"disease": "K01", "symptom": "G11", "weight": 0.0},
    {"disease": "K01", "symptom": "G10", "weight": 0.0},
    {"disease": "K01", "symptom": "G13", "weight": 0.0},

    # =========================
    # K02 - Blas (dibuat dari pemetaan gejala paling relevan)
    # =========================
    {"disease": "K02", "symptom": "G06", "weight": 1.0},  # menyerang tangkai malai
    {"disease": "K02", "symptom": "G04", "weight": 0.5},  # menyerang buah baru tumbuh
    {"disease": "K02", "symptom": "G01", "weight": 0.5},  # malai
    {"disease": "K02", "symptom": "G10", "weight": 0.5},  # kualitas gabah kurang baik
    {"disease": "K02", "symptom": "G11", "weight": 0.5},  # jumlah gabah menurun
    {"disease": "K02", "symptom": "G03", "weight": 0.5},  # menyerang gabah/pelepah/daun

    # =========================
    # K03 - Pelepah Daun
    # =========================
    {"disease": "K03", "symptom": "G09", "weight": 1.0},  # menyerang pelepah yang membentuk anakan
    {"disease": "K03", "symptom": "G03", "weight": 0.5},  # menyerang gabah/pelepah/daun
    {"disease": "K03", "symptom": "G08", "weight": 0.5},  # daun terkulai
    {"disease": "K03", "symptom": "G12", "weight": 0.5},  # daun mengering dan mati

    # =========================
    # K04 - Fusarium
    # =========================
    {"disease": "K04", "symptom": "G07", "weight": 1.0},  # akar membusuk
    {"disease": "K04", "symptom": "G05", "weight": 1.0},  # padi dewasa busuk dan kering
    {"disease": "K04", "symptom": "G08", "weight": 0.5},  # daun terkulai
    {"disease": "K04", "symptom": "G12", "weight": 0.5},  # daun mengering dan mati

    # =========================
    # K05 - Kresek Hawar Daun
    # =========================
    {"disease": "K05", "symptom": "G13", "weight": 1.0},  # menyerang daun padi dan titik tumbuh
    {"disease": "K05", "symptom": "G12", "weight": 1.0},  # daun mengering dan mati
    {"disease": "K05", "symptom": "G08", "weight": 0.5},  # daun terkulai
    {"disease": "K05", "symptom": "G03", "weight": 0.5},  # menyerang gabah/pelepah/daun
]
