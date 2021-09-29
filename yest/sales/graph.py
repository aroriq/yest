import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.http import HttpResponse
import pandas as pd

def df2plt(df):
	
    index = df.index
    sales = df["total"]
    receive = df["total"]
	# df = pd.DataFrame({'売上': sales,'回収': receive}, index=index)

    # plt.bar(index, {'売上': sales,'回収': receive}, color='#15173c')
    plt.bar(index, sales, color='#15173c')
    plt.title("Monthly Sales", color='#15173c')
    plt.xlabel("Month")
    plt.ylabel("total")



def plt2svg():
    buf = BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s


#プロットしたグラフを画像データとして出力するための関数
def Output_Graph():
	buffer = BytesIO()                   #バイナリI/O(画像や音声データを取り扱う際に利用)
	plt.savefig(buffer, format="png")    #png形式の画像データを取り扱う
	buffer.seek(0)                       #ストリーム先頭のoffset byteに変更
	img   = buffer.getvalue()            #バッファの全内容を含むbytes
	graph = base64.b64encode(img)        #画像ファイルをbase64でエンコード
	graph = graph.decode("utf-8")        #デコードして文字列から画像に変換
	buffer.close()
	return graph

#png画像形式に変換数関数
def plt2png():
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s

    
#グラフをプロットするための関数
def Plot_Graph(x,y):
	plt.switch_backend("AGG")        #スクリプトを出力させない
	plt.figure(figsize=(10,5))       #グラフサイズ
	plt.bar(x,y)                     #グラフ作成
	plt.xticks(rotation=45)          #X軸値を45度傾けて表示
	plt.title("Revenue per Date")    #グラフタイトル
	plt.xlabel("Date")               #xラベル
	plt.ylabel("Reveue")             #yラベル
	plt.tight_layout()               #レイアウト
	graph = Output_Graph()           #グラフプロット
	return graph

#グラフ作成
def setPlt():
    x = ["07/01", "07/02", "07/03", "07/04", "07/05", "07/06", "07/07"]
    y = [3, 5, 0, 5, 6, 10, 2]
    plt.bar(x, y, color='#00d5ff')
    plt.title("f{Running Trend  -2020/07/07}", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("km")

