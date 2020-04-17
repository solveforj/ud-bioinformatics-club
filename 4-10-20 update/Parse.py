
# REMINDER: Change filepath to your system configuration
file = open("/Users/josephgalasso/Documents/COVIDGenomeAnalysis/MOA_fastas_96_genomes.txt", "r")
lines = file.readlines()

for i in range(len(lines)):
    line = lines[i]
    if line[0:4] == ">lcl":
        newHeader = line.replace("]", "")
        newHeader = newHeader.split(" [")
        accessionNumber = newHeader[0][5:].split("_")[0]
        proteinName = newHeader[1].split("=")[1]
        proteinID = newHeader[2].split("=")[1]
        newHeader = ">" + accessionNumber + "," +  proteinName + "," + proteinID + "\n"
        lines[i] = newHeader

file.close()

# REMINDER: Change file name to your preference
filename = "parsedMOA"

# REMINDER: Change filepath to your system configuration
out = open("/Users/josephgalasso/Documents/COVIDGenomeAnalysis/" + filename, 'w')
out.writelines(lines)
out.close()
