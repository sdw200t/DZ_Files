import os, os.path

dict_files = {}
len_files = []
files = os.listdir(path=".")
for filename in files:
    if filename[len(filename)-3:] == 'txt':
        with open(filename, 'r', encoding='UTF-8') as f:
            info = {}
            text = ''
            count = 0
            for line in f:
                text += line
                count += 1
            dict_files[count] = {'text':text, 'filename':filename}
            len_files.append(count)

len_files.sort()
with open('rez.txt', 'w', encoding='UTF-8') as f:
    for i in len_files:
        f.write(dict_files[i]['filename']+'\n')
        f.write(str(i)+'\n')
        f.write(dict_files[i]['text']+'\n')


