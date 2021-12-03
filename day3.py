import pandas as pd
# q1
((int("".join(str(i) for i in (pd.read_csv('day3.txt',sep=' ',header=None,dtype='str')[0].str.split("",
                                                                      expand = True)[range(1,
                                                                                               len(pd.read_csv('day3.txt',sep=' ',
                                                                                                               header=None,dtype='str')[0].str.split("",expand = True).columns)-1)].applymap(int).sum()>len(pd.read_csv('day3.txt',sep=' ',header=None))/2).astype(int).values),2))
*
(int("".join(str(i) for i in (pd.read_csv('day3.txt',sep=' ',header=None,dtype='str')[0].str.split("",
                                                                      expand = True)[range(1,
                                                                                               len(pd.read_csv('day3.txt',sep=' ',
                                                                                                               header=None,dtype='str')[0].str.split("",expand = True).columns)-1)].applymap(int).sum()<len(pd.read_csv('day3.txt',sep=' ',header=None))/2).astype(int).values),2)))
