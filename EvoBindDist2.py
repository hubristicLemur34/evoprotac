from Bio.PDB import PDBParser
import numpy as np
import sys

#ADD COMMENTS TO UNDERSTAND WHAT IS GOING ON. 
#5-10 lines of calculation should ba separate function, make each part it's own function, it helps test individual parts 
def distanceCalculator2(PBDfile):
    
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("pdb", PBDfile)

#get_coords(stricture = structure)
    coords_A = []
    coords_B = []

    for model in structure:
        for chain in model:
            if chain.id == "A":
                for atom in chain.get_atoms():
                    coords_A.append(atom.coord)
            elif chain.id == "B":
                for atom in chain.get_atoms():
                    coords_B.append(atom.coord)

    coords_A = np.array(coords_A)
    coords_B = np.array(coords_B)

    min_dist = sys.maxsize
    min_pair = None

    for i in range(len(coords_A)):
        for j in range(len(coords_B)):
            d = np.linalg.norm(coords_A[i] - coords_B[j])
            if d < min_dist:
                min_dist = d
                Apair = i
                Bpair = j
                
    total1 = 0
    total2 = 0
    for p in range(len(coords_B)):
            r = np.linalg.norm(coords_A[Apair] - coords_B[p])
            total1 += r
    total1 /= len(coords_B)

    for p in range(len(coords_A)):
            m = np.linalg.norm(coords_B[Bpair] - coords_A[p])
            total2 += m
    total2 /= len(coords_A)
    total1 = float(total1)
    total2 = float(total2)
    return round(total1,2), round(total2,2)

print(distanceCalculator2(r"C:\Users\maria\OneDrive\Personal Documents\example_AF_output\PIN1_with_peptide_binder_unrelaxed_alphafold2_multimer_v3_model_1_seed_000.pdb"))

#python files are lowercase and underscores