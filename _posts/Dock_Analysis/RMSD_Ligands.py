from rdkit import Chem
from rdkit.Chem import AllChem

# 사용자로부터 SDF 파일 이름을 입력 받음
sdf_file1 = input("첫 번째 SDF 파일 이름을 입력하세요: ")
sdf_file2 = input("두 번째 SDF 파일 이름을 입력하세요: ")

# SDF 파일에서 분자를 로드
mol1 = Chem.SDMolSupplier(sdf_file1)[0]
mol2 = Chem.SDMolSupplier(sdf_file2)[0]

# 분자가 성공적으로 로드되었는지 확인
if mol1 is not None and mol2 is not None:
    # 분자의 콘포머를 생성
    AllChem.EmbedMolecule(mol1, AllChem.ETKDG())
    AllChem.EmbedMolecule(mol2, AllChem.ETKDG())

    # 두 콘포머 간의 RMSD 계산
    rmsd = AllChem.GetBestRMS(mol1, mol2)

    print(f"{sdf_file1}와 {sdf_file2} 간의 RMSD: {rmsd:.2f} Ångstroms")
else:
    print("SDF 파일에서 분자를 로드하는 중 오류가 발생했습니다.")