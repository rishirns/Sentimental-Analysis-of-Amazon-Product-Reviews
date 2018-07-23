def remove_empty_lines(filename):
    """Overwrite the file, removing empty lines and lines that contain only whitespace."""
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for line in lines if line.strip())
        f.truncate()
# function to read kaggle training file, train and test a classifier 
#def processkaggle(dirPath,limitStr):

remove_empty_lines('/Users/rishi/Desktop/clothing_shoes_jewelry.txt')
f = open('/Users/rishi/Desktop/clothing_shoes_jewelry.txt', 'r')
answer = collections.defaultdict(list)
for line in f:
 	k, v = line.strip().split(':',1)
    answer[k.strip()].append(v.strip())
  # convert the limit argument from a string to an int
  #//limit = int(limitStr)
  #//os.chdir(dirPath)
  #//f = open('./train.tsv', 'r')
  # loop over lines in the file and use the first limit of them
cnt=0
phrasedata = []
for n in answer['reviewText']:
	phrasedata.append([])
    phrasedata[cnt].append(n)
    cnt += 1
cnt=0
timeyear = []
for nt in answer['reviewTime']:
	timeyear.append(nt)

print(timeyear[:10])
	#phrasedata[cnt].append(nt)
    #cnt += 1