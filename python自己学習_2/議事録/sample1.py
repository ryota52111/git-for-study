import datetime
import pandas as pd
result_list = [] 
fileName = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')) +"会議メモ.xlsx" #保存するファイル名
df = pd.DataFrame(result_list,columns=['時刻', '内容'])#列名
with pd.ExcelWriter(fileName) as writer:
    df.to_excel(writer,index=False)#エクセルファイルに書き出し
    print(fileName+"という名前で保存しました。")
