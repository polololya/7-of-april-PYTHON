# 7-of-april-PYTHON
Test for handmade trimmer script

##### Handmade trimmer 1.0

Analyses phred quality in each read in fastq file with sliding window and crops the end of read, if quality drops below threshold
Also has arguments for deleting nucleotides from beggining and end of the read without any quality check

###### =======HELP=======
###### Arguments
```
Handmade-trimmer.py [i] [o] [HEAD] [TAIL] [WINDOW] [THRES]
-i Input filename (fastq format only)  
-o Output filename  
--HEAD Headcrop: number of nucleotides to be cropped from the begginig of read  
--TAIL Tailcrop: number of nucleotides to be cropped from the end of read  
--WINDOW Sliding window size. Default value = 4  
--THRES Threshold, if window average drops below it, nucleotides will be cropped. Default value = 30  
```

##### Usage example
```$ Handmade-trimmer.py -i input.fastq -o output.fastq --HEAD 5 --TAIL 10 --WINDOW 5 --THRES 30```
```
Trimmed 2000 FASTQ records  
Threshold value was set as 30  
5 nucleotides was cropped from the beggining and 10 at the end of each read  
```
