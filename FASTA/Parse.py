
# REMINDER: Change filepath to your system configuration
file = open("FASTA/MOA_fastas_96_genomes.txt", "r")
lines = file.readlines()

def getIDName(newHeader, id):
    for item in newHeader:
        itemID = item.split("=")[0]
        if itemID == id:
            return item.split("=")[1]


for i in range(len(lines)):
    line = lines[i]
    if line[0:4] == ">lcl":
        newHeader = line.replace("]", "")
        newHeader = newHeader.split(" [")
        accessionNumber = newHeader[0][5:].split("prot")[0][0:-1]
        proteinName = getIDName(newHeader, "protein")
        proteinID = getIDName(newHeader, "protein_id")
        
        #proteinName = newHeader[1].split("=")[1]
        #proteinID = newHeader[2].split("=")[1]
        
        newHeader = ">" + accessionNumber + "," +  proteinName + "," + proteinID + "\n"
        lines[i] = newHeader

file.close()

# REMINDER: Change file name to your preference
filename = "parsed_MOA"

# REMINDER: Change filepath to your system configuration
out = open("FASTA/" + filename, 'w')
out.writelines(lines)
out.close()
