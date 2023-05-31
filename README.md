# kunitz_project
**kunitz_struct_align_clean.fasta** is the MSA file coming from PDBe Fold with which **kunitz_model.hmm** has been built.
**pdbefold_results.dat** contains some data about PDBe Fold run with the pdb_chain.txt identifier list.
**set1.txt** and **set2.txt** are the two subsets from which the optimal threshold has been computed.
**entry_eval.class** is the file with all SwissProt entries (positives + negatives) with the relative e-value.
**performance.py** calculates MCC and confusion matrix.
**positive_id_list.txt** is a list of the sequences (w/o traning sequences) that must be given in input while running performance.py.
Training FASTA sequences have been removed from positive dataset using **common_sequence_remover.py**.
