# python

# textractor.py

from tr import tr

chunk_size = 1024 # read files in this chunk size
file_list_location = 1024 * 32
contents_start = 1024 * 56

disc_img = 'data/disc-h1.dat'
output_stem = 'output/disc-h1'


# Take the disc files and split at 1k boundaries
# Save the xbg chunk which has the file list
# Content starts at xce

data_fh = open( disc_img, 'rb')

# The files on the disk are listed in this chunk.
# Make it more readable and write the list to screen for now and to file
print ("File list")
data_fh.seek(file_list_location)
file_list_raw = data_fh.read(chunk_size)

## Should refine this to extract the strings
file_list_readable = tr( '\xe5',' ', file_list_raw.decode( 'latin-1') )

#print(file_list_readable)
fl_fh = open ( output_stem + '-files', 'wb')
fl_fh.write( str.encode(file_list_readable))
fl_fh.close

# Move on to where the content starts
data_fh.seek( contents_start )

# Set up the loop
count = 1
contig_fh = open( output_stem + '-' + str(count), 'wb')
text_raw = data_fh.read(chunk_size)
while (len(text_raw) == 1024 ):
  text_readable = tr( '\x80-\xff', '\x00-\x7f', text_raw.decode( 'latin-1') )
  print (text_readable)
  # print ('<>')
  
  # Check if this continues the text and start a new file if needed
  contig = input ("\033[92m" + "Is this contiguous? " + "\033[94m")
  if contig == 'b':
    break

  if contig == 'n':
    contig_fh.close
    count = count + 1
    contig_fh = open( output_stem + '-' + str(count) + '.ws', 'wb')
  

  contig_fh.write(text_raw)
  text_raw = data_fh.read(chunk_size)

contig_fh.close
print(str(count) + ' new text files created')
