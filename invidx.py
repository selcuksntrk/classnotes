import re, json, glob, string, os
from collections import defaultdict
from unidecode import unidecode

WORD = re.compile(r'\w+')

def clean_text(text):
    text = text.replace("\n"," ").replace("\r"," ")
    punc_list = '!"#$%^()*+,-./:;<=>?@[\]^_{|}~' + '0123456789'
    t = str.maketrans(dict.fromkeys(punc_list, " "))
    text = text.translate(t)
    t = str.maketrans(dict.fromkeys("'`",""))
    text = text.translate(t)
    return text

def reg_tokenize(text):
    text = clean_text(text)
    words = WORD.findall(text)
    return words

def index_dir():

    invidx = defaultdict(lambda: defaultdict(int))
    dir = os.getcwd()
    files1 = glob.glob(dir + "/**/**/*.md")
    files2 = glob.glob(dir + "/**/**/*.tex")
    files = files1 + files2
    files = sorted(files)
    for file in enumerate(files):
        doc = file[1].replace(dir,"")    
        for word in reg_tokenize(open(file[1]).read()):
            word = unidecode(word).lower()
            if len(word) < 2: continue
            invidx[word][doc] += 1
        print (doc)

    fout = open("/tmp/invidx.json","w")
    fout.write(json.dumps(invidx))
    fout.close()

    exit()
    
    # split the index

    invidx = json.loads(open("/tmp/invidx.json").read())
    invidx_dict = {}

    for c in  string.ascii_lowercase:
        invidx_dict[c] = defaultdict(lambda: defaultdict(int))

    for k,v in invidx.items():
        first_letter = k[0]
        if first_letter in string.ascii_lowercase:
            invidx_dict[first_letter][k] = v

    for k,v in invidx_dict.items():
        fout = open("idx/invidx-%s.json" % k,"w")
        fout.write(json.dumps(v))
        fout.close()    
    
if __name__ == "__main__": 

    index_dir()

