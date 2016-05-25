import time
def homework():
   lsh='[LSH edited {0}]'.format(time.strftime('%Y.%m.%d , %H:%M:%S'))
    fin=open('output.txt', 'r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        fout.write(lsh)
        fout.write('\t')
        for word in words:
            if word == 'line':
                fout.write('\t')    
                word=word.upper()
            fout.write(word)
        fout.write('\n')
    fin.close()
    fout.close()
    
def homework2():
  fin=open('output.txt','r')
fout=open('outputUpper.text','w')
for line in fin:
        words=line.split()
        for word in words:
            if word=='line':
                word=word.upper()
        print '\n'
        #print line
fin.close()
fout.close()

def lab12():
    homework()
    homework2()

def main():
    lab12()
    raw_input()

if __name__=="__main__":
    main()