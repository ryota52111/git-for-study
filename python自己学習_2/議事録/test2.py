#coding:utf-8
import pandas as pd
import speech_recognition as sr
from datetime import datetime

#文字起こしファイルのファイル名を日付のtxtファイルとする
result_list = [] 
fileName = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')) +"会議メモ.xlsx" #保存するファイル名
df = pd.DataFrame(result_list,columns=['時刻', '内容'])#列名
with pd.ExcelWriter(fileName) as writer:
    df.to_excel(writer,index=False)#エクセルファイルに書き出し
    print(fileName+"という名前で保存しました。")

r = sr.Recognizer()
mic = sr.Microphone()

while True:
    print("Say something ...")

    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)

    print ("Now to recognize it...")

    try:
        print(r.recognize_google(audio, language='ja-JP'))

        # "ストップ" と言ったら音声認識を止める
        if r.recognize_google(audio, language='ja-JP') == "ストップ" :
            print("end")
            break
            result_list = [] 
            fileName = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')) +"会議メモ.xlsx" #保存するファイル名
            df = pd.DataFrame(result_list,columns=['時刻', '内容'])#列名
            with pd.ExcelWriter(fileName) as writer:
            df.to_excel(writer,index=False)#エクセルファイルに書き出し
            print(fileName+"という名前で保存しました。")

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))