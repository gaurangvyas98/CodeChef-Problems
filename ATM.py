amt,bal=map(float,input().split())
if amt+0.5>bal:
    print("{:.2f}".format(bal))
elif amt%5!=0:
    print("{:.2f}".format(bal))
else:
    bal=bal-amt-0.5
    print("{:.2f}".format(bal))
