def bar(num,denom,length=50,fillchar='#',emptychar='_',leftchar='[',rightchar=']'):
    fillnum = ((int)( (num/denom) * length))
    return leftchar + ( fillnum * fillchar ).ljust(length,emptychar)  + rightchar