"""

=======================================
Merge .tsv results files and sort lines
=======================================

@author: Micha Eichmann

Merge:
in case scrape.py exited with an error, was run multiple times, and thus, several .tsv files were created

Sort lines:
in any case

"""

import glob

read_files = glob.glob('*.tsv')
weekly_stats_file = 'chsb_weekly_stats.txt'


lines = []
for f in read_files:
    with open(f, 'r') as infile:
        for line in infile:
            if 'url\ttitle' not in line:
                lines.append(line)

lines.sort()

header = ['url\ttitle\t#\tName\tSymbol\tMarket\tCap\tPrice\tCirculating Supply\tVolume (24h)\t% 1h\t% 24h\t% 7d\n']
lines = header + lines

with open(weekly_stats_file, 'w') as outfile:
    outfile.writelines(lines)
