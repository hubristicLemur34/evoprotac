import json

def average(file, index):
    with open(file) as f:
        d = json.load(f)
    list1 = d['plddt'] 
    avg = 0
    for i in range(int(index[0]),int(index[1])):
        avg = list1[i] + avg
    avg = avg/(int(index[1])-int(index[0]))
    return round(avg, 2)

print(average(r"C:\Users\maria\OneDrive\Personal Documents\example_AF_output\PIN1_with_peptide_binder_scores_alphafold2_multimer_v3_model_1_seed_000.json",(0,48)))
#replace with correct path! KEEP THE R so program doesn't misinterpret \u or something, also INDEX takes 0 to the veru last number in the list 
