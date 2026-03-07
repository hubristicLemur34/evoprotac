from Bio.PDB import MMCIFParser, PDBIO
import numpy as np
import sys

def cif_to_pdb(cif_file, pdb_file=None):
    
    if pdb_file is None:
        pdb_file = cif_file.replace('.cif', '.pdb')
    
    # Parse CIF file
    parser = MMCIFParser()
    structure = parser.get_structure("structure", cif_file)
    
    # Write PDB file
    io = PDBIO()
    io.set_structure(structure)
    io.save(pdb_file)
    
    return pdb_file

print(cif_to_pdb(r"\\wsl.localhost\Ubuntu-22.04\home\marianne\results1_yaml\boltz_results_protein1\predictions\protein1\protein1_model_0.cif"))