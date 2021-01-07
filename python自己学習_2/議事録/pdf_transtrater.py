#PDFファイル内の表をExcelに取り込むプログラム
#2020/8/30 伊沢　剛
import pandas as pd
import camelot.io as camelot
#pdfファイルのを読み込む
table = camelot.read_pdf("旅行スケジュール.pdf")
lists = [] #一時保存用リスト
for t in table:
    lists.append(t.df)
df = pd.concat(lists) #データフレームを結合
# excelファイルへ出力
with pd.ExcelWriter("outFile.xlsx") as writer:
    df.to_excel(writer, sheet_name='sheet1', index=False, header=False)