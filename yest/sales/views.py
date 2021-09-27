from django.http import HttpResponse
from django.shortcuts import render
import io

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .models import SalesModel

#png画像形式に変換数関数
def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s

# html表示view
def analysis_screen(request):
    return render(request, 'analysis.html')

#画像埋め込み用view
def img_plot(request):
    # matplotを使って作図する
    #(ex)
    x = [1, 5, 9]
    y = [4, 6, 8]
    ax = plt.subplot()
    ax.scatter(x, y)
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type='image/png')
    return response


class sales_index(LoginRequiredMixin, generic.ListView): # generic.ListViewを継承
    model = SalesModel
    paginate_by = 5 
    ordering = ['-updated_dt']
    template_name = 'sales/index.html'


class sales_detail(generic.DetailView):
    model = SalesModel
    template_name = 'sales/sales_detail.html'

def stats_top(request):
    return render(request, 'sales/stats_top.html')

#画像埋め込み用view
def barchart(request):
    objects = ['12/10/2019','12/11/2020','15/10/2020']
    y_pos = np.arange(len(objects))
    qty = [10,20,25]
    plt.bar(y_pos, qty, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Quantity')
    plt.title('Sales')
    # plt.savefig('chart/barchart.png')
    # return render(request,'stats_top.html')
    response = HttpResponse(plt, content_type='image/png')
    return response



from django.views.generic import TemplateView
# from . import models
from . import graph

class Index2(TemplateView):

    #テンプレートファイル連携
    template_name = "Index2.html"

    #変数としてグラフイメージをテンプレートに渡す
    def get_context_data(self, **kwargs):

        #グラフオブジェクト
        qs    = SalesModel.objects.all()  #モデルクラス(ProductAテーブル)読込
        x     = [x.updated_dt for x in qs]           #X軸データ
        y     = [y.brokerage for y in qs]        #Y軸データ
        chart = graph.Plot_Graph(x,y)          #グラフ作成

        #変数を渡す
        context = super().get_context_data(**kwargs)
        context['chart'] = chart
        return context

    #get処理
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

#png画像形式に変換数関数
def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s


# html表示view
def analysis_screen(request):
    return render(request, 'analysis.html')

#画像埋め込み用view
def img_plot(request):
    # matplotを使って作図する
    # (ex)
    x = [1, 5, 9]
    y = [4, 6, 8]
    ax = plt.subplot()
    # ax.scatter(x, y)
    ax.bar(x=[1,2,3], height=[4,3,2])
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type='image/png')
    return response


def salesdata(request):
    alldata = SalesModel.objects.all().values()
    df = pd.DataFrame(alldata)
    
    df["total"]=df["brokerage"]+df["adfee"]+df["hangingfee"]+df["etc1fee"]+df["etc2fee"]
    df["receivedate_day"]=pd.to_datetime(df["receivedate"])
    df["receivedate_month"]=df["receivedate_day"].dt.strftime("%Y年%m月")
    df["receivedate_year"]=df["receivedate_day"].dt.strftime("%Y")
    
    # df_month = df.groupby("receivedate_month").sum()["brokerage"]
    df_year = pd.DataFrame(df.groupby("receivedate_year").sum()["total"])
    df_month = pd.DataFrame(df.groupby("receivedate_month").sum()["total"])
    df_staff = pd.DataFrame(df.groupby("responsiblestaff_id").sum()["total"])
    df_yearstaff = pd.DataFrame(df.groupby(["receivedate_year", "responsiblestaff_id"]).sum()["total"])
    df_monthstaff = pd.DataFrame(df.groupby(["receivedate_month", "responsiblestaff_id"]).sum()["total"])
    df_staffyear = pd.DataFrame(df.groupby(["responsiblestaff_id", "receivedate_year" ]).sum()["total"])
    df_staffmonth = pd.DataFrame(df.groupby(["responsiblestaff_id", "receivedate_month"]).sum()["total"])
   
    mydict = {
        "df": df.to_html(classes="table"),
        "df_year": df_year.to_html(header=False, classes="table",index_names=False ),
        "df_month": df_month.to_html(header=False, classes="table",index_names=False ),
        "df_staff": df_staff.to_html(header=False, classes="table",index_names=False  ),
        "df_yearstaff": df_yearstaff.to_html(header=False, classes="table" ,index_names=False ),
        "df_monthstaff": df_monthstaff.to_html(header=False, classes="table" ,index_names=False ),
        "df_staffyear": df_staffyear.to_html(header=False, classes="table" ,index_names=False ),
        "df_staffmonth": df_staffmonth.to_html(header=False, classes="table" ,index_names=False ),
        # "describe":df.describe().to_html,        
        # "df_month_chart": df99.plot
    }
    return render(request, 'sales/data.html', context=mydict)
