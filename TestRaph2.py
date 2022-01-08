ch="salut\nje suis\nMisha\nbye"
hc=ch[::-1]
i=hc.find("\n")
ch=ch[:len(ch)-i-1]
print("ch est la suivante",ch[:len(ch)-i-1])