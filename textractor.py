# python

# textractor.py

from tr import tr

chunk_size = 1024 # read files in this chunk size
file_list_location = 1024 * 32
contents_start = 1024 * 56

disc_img = 'data/disc-h1.dat'


# Take the disc files and split at 1k boundaries
# Save the xbg chunk which has the file list
# Content starts at xce

fh = open( disc_img, 'rb')

print ("File list")
fh.seek(file_list_location)
file_list_raw = fh.read(chunk_size)

print(file_list_raw)

fh.seek( contents_start )

print( "Start of data")
text_raw = fh.read(chunk_size)

print(text_raw)
print ("decoded")
text_readable = text_raw.decode( 'latin-1')
print (text_readable)

text_simple = tr( '\x80-\xff', '\x00-\x7f', text_readable)

print( text_simple)

# For each xce to end
# Convert high chars to low (  tr [\200-\377] [\000-\177] )
# Display and ask if contiguous with previous
#  Yes: write to same file
#  No: start new file

