from Bio.PDB import PDBParser
import numpy as np
import sys


#for that specific peptide, find the distance to the closest peptide in the other thing.
#make 3D array and find distance between A and B and go through array to find smallest distance for each A
#take averageds


#Open pdb and get lists of coordinates for each protein.
def get_coords(FILE):
    
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("pdb", FILE)

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
    return coords_A, coords_B

def smallest_distance(coords_A, coords_B):
    diffs = coords_A[:,None,:] - coords_B[None,:,:] #this subtracts both matricies to get the difference for each pair of points
    #axis 1 is the A peptides, axis 2 is B peptides, Axis 3 is xyz coords
    d2 = np.sum(diffs**2, axis=2) #finds distance, takes square of each component and adds them
    min_per_A = np.sqrt(d2.min(axis=1)) #look across the COLS and find the smallest distance returns an 1D array
    min_per_B = np.sqrt(d2.min(axis=0)) #look across ROWS and find smallest distance 1D array
    return round(float(min_per_A.mean()),2), round(float(min_per_B.mean()),2) 

coords_A, coords_B = get_coords(r"\\wsl.localhost\Ubuntu-22.04\home\marianne\results1_yaml\boltz_results_protein1\predictions\protein1\protein1_model_0.pdb")
print(smallest_distance(coords_A, coords_B))


