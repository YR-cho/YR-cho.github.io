from rdkit import Chem
import numpy as np
import sys

def non_hydrogen_atoms(mol):
    return [atom.GetIdx() for atom in mol.GetAtoms() if atom.GetSymbol() != 'H']

def calculate_rmsd(file1, file2):
    # sdf 파일로부터 분자 로드
    mol1 = Chem.SDMolSupplier(file1)[0]
    mol2 = Chem.SDMolSupplier(file2)[0]

    # 수소 제외
    non_hydrogen_mol1 = non_hydrogen_atoms(mol1)
    non_hydrogen_mol2 = non_hydrogen_atoms(mol2)

    # 원자 간의 거리를 계산
    differences = []
    for idx1, idx2 in zip(non_hydrogen_mol1, non_hydrogen_mol2):
        pos1 = np.array(mol1.GetConformer().GetAtomPosition(idx1))
        pos2 = np.array(mol2.GetConformer().GetAtomPosition(idx2))
        difference = np.linalg.norm(pos1 - pos2)
        differences.append(difference)

    rmsd = np.sqrt(np.mean(np.square(differences)))

    return rmsd

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py file1.sdf file2.sdf")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    rmsd = calculate_rmsd(file1, file2)
    print(f"RMSD: {rmsd:.3f} Å")