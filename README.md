

1. Run generateBatchFile.py
    !!!! IGV requires that all file paths be full. So when running on a mac start from /Users/...

    python generateBatchFile.py <sample_loc> <vcfFile_loc> <snapShot_loc> <batchFile_loc>
        
        <sample_loc> Must be the path to a directory containing the .bam & .bai files of the samples you wish to load
    
        <vcfFile_loc> A .vcf file with the locations you wish to take screen shots of
    
        <snapShot_loc> Where you want the screen shots to be saved to
    
        <batchFile_loc> The location to write the igv batch file generated from the preceding information

2. Run the batch file in IGV 
    
    - Open IGV & load reference
    - From the menu bar click "Tools --> Run Batch Script..." & navigate to the .txt file generated by generateBatchFile.py
