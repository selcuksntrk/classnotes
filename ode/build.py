import os, sys, glob

pdfs = " ".join(sorted(list(glob.glob('./*/*.pdf'))))
d = os.environ['HOME']
if len(sys.argv) == 1:
    cmd = "pdfunite %s " + d + "/Downloads/ode_mattuck.pdf"
    os.system(cmd % pdfs)
    exit()
    
elif sys.argv[1] == 'all':
    for a in sorted(glob.glob("ode*")):
        os.chdir(a)
        os.system("pdflatex -shell-escape %s" % glob.glob("ode_mattuck_*.tex")[0] )
        os.chdir("..")
        
    
elif sys.argv[1] == 'clean':
    os.system("find . -name '_region_*' | xargs rm  -rf")
    os.system("find . -name '_minted-*' | xargs rm  -rf")
            
elif sys.argv[1] == 'tex':
    file = glob.glob('ode_mattuck_*.tex')
    os.system("pdflatex -shell-escape %s" % file[0])
    
elif sys.argv[1] == 'md':
    sys.path.append("../.."); import util
    file = glob.glob('*.tex')
    ftex = file[0]; path = os.getcwd()
    util.tex_mathjax_html(path + "/" + ftex, path + "/" + "out.html","adkasdf")
    
