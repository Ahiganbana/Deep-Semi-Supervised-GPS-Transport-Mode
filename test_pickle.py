import pickle
import pandas as pd


filename = '../Mode-codes-Revised/paper2_Trajectory_Label.pickle'
f = open(filename,'rb')
info = pickle.load(f)
# print(info)


pd.set_option('display.width',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth',None)

inf=str(info)
ft = open('../Mode-codes-Revised/paper2_Trajectory_Label_ncsv.csv', 'w')
ft.write(inf)