import re

def find_dsal(seq):
    valid_seqs_found = re.findall(r'CCGCGG|CCGTGG|CCACGG|CCATGG', seq)
    return len(valid_seqs_found)

def find_secl(seq):
    valid_seqs_found = re.findall(r'CC[ACGT][ACGT]GG', seq)
    return len(valid_seqs_found)

def find_cjul(seq):
    valid_seqs_found = re.findall(r'CA[CT][ACGT]{5}[GA]TG', seq)
    return len(valid_seqs_found)