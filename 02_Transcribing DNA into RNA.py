def DNA_to_RNA(DNA):
    RNA = []
    for i in list(DNA):
        if i == 'T':
            RNA.append('U')
        else:
            RNA.append(i)
    return ''.join(RNA)


print(DNA_to_RNA('TCCGAATGGTGTTCTAGCTACCTGTGCTAAACAAATAGCCATGTTATATTACCGGGCATTCATGTGCGGACCACGCCAGTCGAGTGAATTCCACACACCCCAGAATAACGCACCGAGTGGCGTCAAACTCTGCCAGTAAGGGCTTTATCAGATACCGGGAACCATTCTGAGCGTGTATACAAACTAGTCAAGGCATATTCCTCGACGAAAAAACATCGATTCGCGCCAAGTTATCTTATGAATGGCTTGAACAATGCCGGCGCGCACAGTATGAAGGTCCGTTCATGGCAGTACGAAAATGTCATCGAAACACCTTTCGAGTGGATCGGTAGTTAACTATGCGTGGCACGGTAGCTGAGATCGTCGCCCGGAACTACCCCTACTTCGGTGCTAGGCAAGTAGTACCCACATTACTTGCGAGGTATAAATTCTGACTGGTAATTCCCAATTGCTGGCGAGTACCGGTGTTTCACGCCACTGTTGAGGGATTAGGATTCCGCCCGAGCGTGGCATTATGTGGACGTTGGGCACTGTAAAAGGGTCTCGCACACGCTCTTGTGTATCCAACGAGCAGGTAAGAGCATATGTTCATACTAGCCTTCTCTTAACATAGTATTAAGAGCTTGCACGACAGGTCGTAAGGCCTTTGCCGGGGTTCCAGTTCTATGCCAGGTCGATTCCGATAGCCACTTGCTTACCTCAAGGAGCAACGGAAATTGTGGGCGGATTCTGGATTTAGCGTCTGGAGCGTCGCCGAGGAGCGATTCAGAAGGTCTCGAGGTAAGTTAGTCCATTTTCTTACTTATTGACTCGTTGTTCAACACCACTTCTATGAACCGGCGGTATAGACGACTAAGGACGTGGAACAGCAGTCCAAAACATGTGAGTTTGAAGAAATTTACTAGCGAAGGCCTTCAACTGCGTGACGTAGGA'))
