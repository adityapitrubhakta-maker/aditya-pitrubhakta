
Organic Chemistry Toolkit

Features:
1. Calculate molecular formula
2. Calculate molecular weight
3. Identify common functional groups
4. Display canonical SMILES


from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors

FUNCTIONAL_GROUPS = {
    "Alcohol": "[OX2H][CX4]",
    "Carboxylic acid": "[CX3](=O)[OX2H1]",
    "Aldehyde": "[CX3H1](=O)[#6]",
    "Ketone": "[#6][CX3](=O)[#6]",
    "Amine": "[NX3;!$(NC=O)]",
    "Amide": "[NX3][CX3](=[OX1])[#6]",
    "Alkene": "[CX3]=[CX3]",
    "Alkyne": "[CX2]#[CX2]",
    "Ether": "[OD2]([#6])[#6]",
    "Nitrile": "[CX2]#N",
    "Haloalkane": "[F,Cl,Br,I][CX4]",
    "Aromatic ring": "a1aaaaa1",
}


def analyze_molecule(smiles):
    Analyze a molecule represented by a SMILES string.

    molecule = Chem.MolFromSmiles(smiles)

    if molecule is None:
        print("Invalid SMILES. Please enter a valid chemical structure."        return

    print("\n===== ORGANIC CHEMISTRY ANALYSIS =====")
    print("Input SMILES:", smiles)
    print("Canonical SMILES:", Chem.MolToSmiles(molecule))
    print("Molecular Formula:", rdMolDescriptors.CalcMolFormula(molecule))
    print("Molecular Weight:", round(Descriptors.MolWt(molecule), 3), "g/mol")
    print("Number of Atoms:", molecule.GetNumAtoms())

    print("\nFunctional Groups Found:")

    found_groups = []

    for group_name, smarts in FUNCTIONAL_GROUPS.items():
        pattern = Chem.MolFromSmarts(smarts)

        if pattern and molecule.HasSubstructMatch(pattern):
            found_groups.append(group_name)

    if found_groups:
        for group in found_groups:
            print("-", group)
    else:
        print("No listed functional groups detected.")

    print("\n======================================")


def main():
    print("ORGANIC CHEMISTRY TOOLKIT")
    print("Enter a molecule using SMILES notation.")
    print("Examples: CCO (ethanol), CC(=O)O (acetic acid)")
    print("Type 'exit' to quit.")

    while True:
        smiles = input("\nEnter SMILES: ").strip()

        if smiles.lower() == "exit":
            print("Thank you for using the toolkit!")
            break

        if not smiles:
            print("Please enter a SMILES string.")
            continue

        analyze_molecule(smiles)


if __name__ == "__main__":
    main()
