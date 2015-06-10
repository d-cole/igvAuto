import sys
import os
#IGV batch file format
#
#new
#load /full path to sample.bam
#snapshotDirectory /dir to folder for screen shots
#goto pseudo19:3274882
#snapshot image_file_name.png

# repeat for each screenshot
"""
generateBatchFile.py

The program generates a IGV formatted batch file to automate taking screenshots of genomic sites
How to run:

python generateBatchFile.py <dir of sampl .bam files>  <dir of folder to store screen shots>  <dir of vcf file to load locations from>  <location to write batch file>
"""


def getSampleList(sample_dir):
    """
    Creates a list of .bam files in the provided directory
    """
    sample_list = []
    for f in os.listdir(sample_dir):
        if f.endswith(".bam"):
            sample_list.append(sample_dir + f)
    return sample_list

def writeBatchHeader(outFile,files,snapShotDir):
    """
    Writes the batch file header
    new

    load file...

    snapshotDirectory <dir to put screenshots>
    """
    outFile.write("new \n")
    for f in files:
        outFile.write("load " + f + "\n")

    outFile.write("snapshotDirectory " + snapShotDir + "\n")

def writeBatchSnapCommands(locations,outFile):
    """
    Writes out 'goto' and 'snapshot' commands for each 
    location in the provided list
    """
    for loc in locations:
        outFile.write("goto " + loc + "\n")
        outFile.write("snapshot " + loc + ".png \n")

def loadPositions(vcfFile_loc):
    """
    Generates a list of locations from a provided vcf file
    """
    pos = []
    with open(vcfFile_loc) as vcfFile: 
        for line in vcfFile:
            if len(line) > 1:
              if line[0] != "#":
                   line_col = str.split(line)
                   pos.append(line_col[0] + ":" + line_col[1])

    return pos

if __name__ == "__main__":
    sample_dir,snapShotDir,vcfFile_loc,batchFile_loc = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]

    batchFile = open(batchFile_loc,"w")
    sample_files = getSampleList(sample_dir)
    locations = loadPositions(vcfFile_loc)


    writeBatchHeader(batchFile,sample_files,snapShotDir)
    writeBatchSnapCommands(locations,batchFile)


