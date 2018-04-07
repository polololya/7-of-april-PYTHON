import argparse
import Bio
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument('-i', help='input filename')
parser.add_argument('-o', help='output filename')
parser.add_argument('--HEAD', default = 0, help='Headcrop: number of nucleotides to be cropped from the begginig of read')
parser.add_argument('--TAIL', default = 0, help='Tailcrop: number of nucleotides to be cropped from the end of read')
parser.add_argument('--WINDOW', type=int, default=4, help='Sliding window size. Default value = 4')
parser.add_argument('--THRES', type=int, default=30, help='Threshold, if window average drops below it, nucleotides will be cropped. Default value = 30')
args = parser.parse_args(args=[])

cropped_reads = [rec[args.HEAD:len(rec.seq)-args.TAIL] for rec in SeqIO.parse(open("test_classwork2.fastq"), "fastq")]
trimmed_reads = []
for read in cropped_reads:
    quality = read.letter_annotations['phred_quality']
    for i in range(0,len(quality)-args.WINDOW):
        current = quality[i:i+args.WINDOW] 
        if (sum(current) / len(current)) < args.THRES:
            trimmed_reads.append(read[0:i])
            break
with open ('trimmed.fastq','w') as output:
    count = SeqIO.write(records, output, "fastq")
    print ("Trimmed {} FASTQ records".format(count))
    print ("Threshold value was set as {}".format(args.THRES))
    if args.HEAD !=0 or args.TAIL != 0:
        print("{} nucleotides was cropped from the beggining and {} at the end of each read")