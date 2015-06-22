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

**Make sure to use full paths for all directorys.
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
    try: 
        sample_dir,vcfFile_loc,snapShotDir,batchFile_loc = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    except:
        print "Invalid parameters"
        sample_dir = raw_input("Enter directory containing samples(.bam & .bai) you wish to load: ")
        vcfFile_loc = raw_input("Enter the location of a .vcf file of sites: ")
        snapShotDir = raw_input("Enter the directory to save screen shots: ")
        batchFile_loc = raw_input("Specify file name & location to write igv batch file: ")

    #Create batch file to write igv commands
    batchFile = open(batchFile_loc,"w")
    
    #Get a list of samples to load into igv
    sample_files = getSampleList(sample_dir)
    
    #Get a list of locations from a .vcf file
    locations = loadPositions(vcfFile_loc)

    writeBatchHeader(batchFile,sample_files,snapShotDir)
    writeBatchSnapCommands(locations,batchFile)


