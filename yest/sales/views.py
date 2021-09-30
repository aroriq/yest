from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import io

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

from .models import SalesModel
from . import graph


class sales_list(LoginRequiredMixin, generic.ListView): # generic.ListViewを継承
    model = SalesModel
    paginate_by = 5 
    ordering = ['-updated_dt']
    template_name = 'sales/sales_list.html'

# class sales_detail(generic.DetailView):
#     model = SalesModel
#     template_name = 'sales/detail.html'


class staff_list(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    paginate_by = 5 
    # ordering = ['-updated_dt']
    template_name = 'sales/staff_list.html'

# def get_svg(request):
#     graph.setPlt()  
#     svg = graph.plt2svg()  #SVG化
#     plt.cla()  # グラフをリセット
#     response = HttpResponse(svg, content_type='image/svg+xml')
#     return response

def create_svg(request,user_id):
    alldata = SalesModel.objects.all().values()
    df = pd.DataFrame(alldata)
    df = df[df["responsiblestaff_id"]==user_id]

    df["total"]=df["brokerage"]+df["adfee"]+df["hangingfee"]+df["etc1fee"]+df["etc2fee"]
    df["receivedate_day"]=pd.to_datetime(df["receivedate"])
    df["receivedate_month"]=df["receivedate_day"].dt.strftime("%Y-%m")
    # df['receivedate_month'] = pd.to_datetime(df['receivedate_day']).dt.to_period('M')
    df["receivedate_year"]=df["receivedate_day"].dt.strftime("%Y")

    df=df[['id', 'responsiblestaff_id', 'brokerage', 'adfee', 'hangingfee', 'etc1fee', 'etc2fee', 'total', 'receive', 'receivedate',"receivedate_month", "receivedate_year"]]
    df_month = pd.DataFrame(df.groupby("receivedate_month").sum()["total"])
    
    graph.df2plt(df_month)
    svg = graph.plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response

def create_bar_svg(request,user_id):
    alldata = SalesModel.objects.all().values()
    df = pd.DataFrame(alldata)
    df = df[df["responsiblestaff_id"]==user_id]

    df["total"]=df["brokerage"]+df["adfee"]+df["hangingfee"]+df["etc1fee"]+df["etc2fee"]
    df["receivedate_day"]=pd.to_datetime(df["receivedate"])
    df["receivedate_month"]=df["receivedate_day"].dt.strftime("%Y-%m")
    # df['receivedate_month'] = pd.to_datetime(df['receivedate']).dt.to_period('M')
    # df["receivedate_year"]=df["receivedate_day"].dt.strftime("%Y")

    # df=df[['id', 'responsiblestaff_id', 'brokerage', 'adfee', 'hangingfee', 'etc1fee', 'etc2fee', 'total', 'receive', 'receivedate',"receivedate_month", "receivedate_year"]]
    df_month = pd.DataFrame(df.groupby("receivedate_month").sum()["total"])
    # graph.df2plt(df_month)

    d_today = datetime.date.today()
    monthlast=pd.Series(
        pd.date_range(end=d_today, periods=15, freq='M')
    )
    year_month=monthlast.dt.strftime('%Y-%m')
    df1=pd.DataFrame({"Date":year_month})

    df2x=pd.Series(df_month.index)
    df2y=pd.Series(df_month['total'])
    df2=pd.DataFrame({"Date":df2x, 'Sales':df2y})
    # df2=pd.DataFrame({"Date":['2021-06','2021-09'], "Sales":[111111,222222]})

    df=df1.merge(df2, how='left', on='Date')
    df=df.fillna(0)
    df['Sales']=df['Sales'].astype('int')

    x=df['Date']
    y=df["Sales"]

    # index = df.index
    # index = df['Date']
    # sales = df["Sales"]
    # receive = df["Receive"]

	# df = pd.DataFrame({'売上': sales,'回収': receive}, index=index)
    # plt.bar(index, {'売上': sales,'回収': receive}, color='#15173c')

    graph.df_to_plt(x, y, xlabel='Date', ylabel='total', title='Monthly Sales')

    svg = graph.plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response

def staff_detail(request,user_id):

    alldata = SalesModel.objects.all().values()
    #alldata = get_object_or_404(SalesModel)#, pk=user_id)
    df = pd.DataFrame(alldata)
    df = df[df["responsiblestaff_id"]==user_id]
    
    df["total"]=df["brokerage"]+df["adfee"]+df["hangingfee"]+df["etc1fee"]+df["etc2fee"]
    df["receivedate_day"]=pd.to_datetime(df["receivedate"])
    df["receivedate_month"]=df["receivedate_day"].dt.strftime("%Y-%m")
    df["receivedate_year"]=df["receivedate_day"].dt.strftime("%Y")

    df=df[['id', 'responsiblestaff_id', 'brokerage', 'adfee', 'hangingfee', 'etc1fee', 'etc2fee', 'total', 'receive', 'receivedate',"receivedate_month", "receivedate_year"]]
    
    # df_month = df.groupby("receivedate_month").sum()["brokerage"]
    df_year = pd.DataFrame(df.groupby("receivedate_year").sum()["total"])
    df_month = pd.DataFrame(df.groupby("receivedate_month").sum()["total"])
   
    mydict = {
        "df": df.to_html(classes="table"),
        "df_year": df_year.to_html(header=False, classes="table",index_names=False ),
        "df_month": df_month.to_html(header=False, classes="table",index_names=False ),
        # "describe":df.describe().to_html,        
        # "df_month_chart": df99.plot
    }
    return render(request,  'sales/staff_detail.html', context=mydict)

    
    # #変数としてグラフイメージをテンプレートに渡す
    # def get_context_data(self, **kwargs):

    #     #グラフオブジェクト
    #     qs    = SalesModel.objects.all()  #モデルクラス(ProductAテーブル)読込
    #     x     = [1,2,3]#[x.Date for x in qs]           #X軸データ
    #     y     = [1,2,6]#[y.Revenue for y in qs]        #Y軸データ
    #     chart = graph.Plot_Graph(x,y)          #グラフ作成

    #     #変数を渡す
    #     context = super().get_context_data(**kwargs)
    #     context['chart'] = chart
    #     return context

    # #get処理
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)


def sales_summary(request):
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
    return render(request, 'sales/sales_summary.html', context=mydict)



# # html表示view
# def analysis_screen(request):
#     return render(request, 'analysis.html')

# #画像埋め込み用view
# def img_plot(request):
#     # matplotを使って作図する
#     #(ex)
#     x = [1, 5, 9]
#     y = [4, 6, 8]
#     ax = plt.subplot()
#     ax.scatter(x, y)
#     png = plt2png()
#     plt.cla()
#     response = HttpResponse(png, content_type='image/png')
#     return response

#画像埋め込み用view
# def barchart(request):
#     objects = ['12/10/2019','12/11/2020','15/10/2020']
#     y_pos = np.arange(len(objects))
#     qty = [10,20,25]
#     plt.bar(y_pos, qty, align='center', alpha=0.5)
#     plt.xticks(y_pos, objects)
#     plt.ylabel('Quantity')
#     plt.title('Sales')
#     # plt.savefig('chart/barchart.png')
#     # return render(request,'stats_top.html')
#     response = HttpResponse(plt, content_type='image/png')
#     return response
