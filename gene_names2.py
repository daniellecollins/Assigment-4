#!/usr/bin/python
import fileinput
import re
import json

print '['

for line in fileinput.input(['/data/Homo_sapiens.GRCh37.75.gtf']):
  text_in_columns = re.split('\t',line)
  if len(text_in_columns)>3:
    if text_in_columns[2] == "gene":
      gene_name = re.findall('gene_name \"(.*?)\";',line)
      chromosome = text_in_columns[0]
      starting_position = text_in_columns[3]
      ending_position = text_in_columns[4]
      print '  {"gene_name": "' + gene_name[0] + '", ' + '"chr": "' + chromosome + '", ' + '"startPos": ' + starting_position + ', "endPos": ' + ending_position + '},'

print ']'
