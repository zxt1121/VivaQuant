# -*- coding:utf-8 -*-
import tushare as ts
import pandas as pd
import sqlite3
import os

def save_hist_data(code, path, timeframe):
    fdb = path + 'hist.db'
    xd = ts.get_hist_data(code, start=None, end=None,ktype=timeframe)
    conn = sqlite3.connect(fdb)
    xd.to_sql(code, conn, if_exists='replace')
    conn.close()
    return xd


def get_hist_data(code, path):
    fdb = path + 'hist.db'
    #fcsv = path + code + '.csv'
    conn = sqlite3.connect(fdb)
    fexist = os.path.exists(fdb)

    if fexist:
        sql = "SELECT * FROM '%s'"%code
        #df = pd.read_sql(sql,conn)
        df=pd.read_sql_query(sql, conn, index_col='date')
        print(df.tail())
        #df.to_csv(fcsv)

save_hist_data('000875', 'Data\\', timeframe="D")
get_hist_data('000875','Data\\')