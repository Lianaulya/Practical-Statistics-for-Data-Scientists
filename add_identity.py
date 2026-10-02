import json, glob, os

IDENTITY_CELL = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "---\n",
        "## Identitas Mahasiswa\n",
        "\n",
        "| | |\n",
        "|---|---|\n",
        "| **Nama** | Muammar Yaldi Fadhil |\n",
        "| **NIM** | 101032300019 |\n",
        "| **Kelas** | TK-47-03 |\n",
        "| **Mata Kuliah** | Machine Learning |\n",
        "\n",
        "---"
    ]
}

base = r'C:\Users\ASUS\.gemini\antigravity\scratch\Practical-Statistics-for-Data-Scientists'
notebooks = [
    'Chapter1_EDA.ipynb',
    'Chapter2_SamplingDistributions.ipynb',
    'Chapter3_StatisticalExperiments.ipynb',
    'Chapter4_Regression.ipynb',
]

for fname in notebooks:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Insert identity cell after the first cell (Colab badge)
    nb['cells'].insert(1, IDENTITY_CELL)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    print(f"Updated: {fname} ({len(nb['cells'])} cells total)")

print("\nAll notebooks updated with student identity!")
