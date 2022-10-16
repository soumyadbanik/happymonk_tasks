import pandas as pd
from scipy import stats


def is_same(series1, series2):
    p_value = stats.kstest(series1, series2).pvalue
    if p_value <=0.05:
        print("p_value = {}. Dataset are not following same distribution".format(p_value))
    else:
        print("p_value = {}. Dataset are following same distribution".format(p_value))
        
if __name__=="__main__":
    
    df = pd.read_csv('IOT-temp.csv',
                index_col='noted_date',
                parse_dates=['noted_date'],
                ).drop(['id','room_id/id','out/in'], axis=1)
    set_B = df[0:10000]
    is_same(df['temp'], set_B['temp'])