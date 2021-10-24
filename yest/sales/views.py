from os import name
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import io

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

import matplotlib
from pandas.core.reshape.merge import merge
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import re

from docs.models import CorpModel, ContractModel
from sales.models import SalesModel
from sales import graph


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

# def create_svg(request,user_id):
#     alldata = SalesModel.objects.all().values()
#     df = pd.DataFrame(alldata)
#     df = df[df["responsiblestaff_id"]==user_id]

#     df["total"]=df["brokerage"]+df["adfee"]+df["hangingfee"]+df["etc1fee"]+df["etc2fee"]
#     df["receivedate_day"]=pd.to_datetime(df["receivedate"])
#     df["receivedate_month"]=df["receivedate_day"].dt.strftime("%Y-%m")
#     # df['receivedate_month'] = pd.to_datetime(df['receivedate_day']).dt.to_period('M')
#     df["receivedate_year"]=df["receivedate_day"].dt.strftime("%Y")

#     df=df[['id', 'responsiblestaff_id', 'brokerage', 'adfee', 'hangingfee', 'etc1fee', 'etc2fee', 'total', 'receive', 'receivedate',"receivedate_month", "receivedate_year"]]
#     df_month = pd.DataFrame(df.groupby("receivedate_month").sum()["total"])
    
#     graph.df2plt(df_month)
#     svg = graph.plt2svg()  #SVG化
#     plt.cla()  # グラフをリセット
#     response = HttpResponse(svg, content_type='image/svg+xml')
#     return response

def create_bar_svg(request,user_id):
    alldata = SalesModel.objects.all().values()
    df = pd.DataFrame(alldata)
    df = df[df["responsiblestaff_id"]==user_id]

    df["total"]=df["brokerage"]+df["adfee"]+df["hangingfee"]+df["etc1fee"]+df["etc2fee"]
    df["receivedate_day"]=pd.to_datetime(df["receivedate"])
    df["receivedate_month"]=df["receivedate_day"].dt.strftime("%Y-%m")
    # df["receivedate_year"]=df["receivedate_day"].dt.strftime("%Y")

    # df=df[['id', 'responsiblestaff_id', 'brokerage', 'adfee', 'hangingfee', 'etc1fee', 'etc2fee', 'total', 'receive', 'receivedate',"receivedate_month", "receivedate_year"]]
    df_month = pd.DataFrame(df.groupby("receivedate_month").sum()["total"])
    # graph.df2plt(df_month)

    d_today = datetime.date.today()
    monthstart=pd.Series(
        pd.date_range(end=d_today, periods=15, freq='MS')
    )
    year_month=monthstart.dt.strftime('%Y-%m')
    df1=pd.DataFrame({"receivedate_month":year_month})

    df2=pd.DataFrame(df_month['total']) 

    df=df1.merge(df2, how='left',on='receivedate_month')
    df=df.fillna(0)
    df['total']=df['total'].astype('int')

    x=df['receivedate_month']
    y=df["total"]

	# df = pd.DataFrame({'売上': sales,'回収': receive}, index=index)
    # plt.bar(index, {'売上': sales,'回収': receive}, color='#15173c')

    graph.df_to_plt(x, y, xlabel='Date', ylabel='total', title='Monthly Sales')

    svg = graph.plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response

def staff_detail(request,user_id):
    alldata = SalesModel.objects.all().values()
    df = pd.DataFrame(alldata)
    df = df[df["responsiblestaff_id"]==user_id]
    
    df["total"]=df["brokerage"]+df["adfee"]+df["hangingfee"]+df["etc1fee"]+df["etc2fee"]
    df["receivedate_day"]=pd.to_datetime(df["receivedate"])
    df["receivedate_month"]=df["receivedate_day"].dt.strftime("%Y-%m")
    df["receivedate_year"]=df["receivedate_day"].dt.strftime("%Y")

    df=df[['id', 'responsiblestaff_id', 'brokerage', 'adfee', 'hangingfee', 'etc1fee', 'etc2fee', 'total', 'receive', 'receivedate',"receivedate_month", "receivedate_year"]]

    df['responsiblestaff_id']=pd.to_numeric(df['responsiblestaff_id'], downcast='integer') 

    userdf = pd.DataFrame(User.objects.all().values())
    userdf['name']=userdf['first_name'] + userdf['last_name']
    userdf['responsiblestaff_id']=userdf['id']
    userdf = userdf[['responsiblestaff_id', 'name']] #, 'email', 'is_staff', 'is_active']]
    # pd.to_numeric(userdf['responsiblestaff_id'])

    df=pd.merge(df,userdf)

    df_name = pd.DataFrame(df.groupby("name").sum()["total"])
    df_name['total'] = df_name['total'].astype(int).apply('{:,}'.format)

    print(df_name)

    # df_month = df.groupby("receivedate_month").sum()["brokerage"]
    df_year = pd.DataFrame(df.groupby("receivedate_year").sum()["total"])
    df_year['total'] = df_year['total'].astype(int).apply('{:,}'.format)

    df_month = pd.DataFrame(df.groupby("receivedate_month").sum()["total"])
    df_month['total'] = df_month['total'].astype(int).apply('{:,}'.format)
   
    Sales = get_object_or_404(SalesModel, pk=user_id)

    mydict = {
        "df": df.to_html(classes="table"),
        "df_year": df_year.to_html(header=False, classes="table",index_names=False ),
        "df_month": df_month.to_html(header=True, classes="table",index_names=False ),
        # "describe":df.describe().to_html,        
        # "df_month_chart": df99.plot,
        "user_id":user_id,
        "Sales":Sales,
        "df_name": df_name.to_html(header=False, classes="table",index_names=False ),
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

    contract = get_object_or_404(ContractModel, pk=contract_id)
    return render(request, 'meisai_print.html',
                  {'contract': contract})

def get_short_name(self):
    return "%s" % (self.name.replace('株式会社イエストホーム', ''))

def get_normal_name(self):
    return "%s" % (self.name)

def sales_summary(request):
    # alldata = SalesModel.objects.all().values()
    df = pd.DataFrame(SalesModel.objects.all().values())

    df["total"]=df["brokerage"]+df["adfee"]+df["hangingfee"]+df["etc1fee"]+df["etc2fee"]
    df["receivedate_day"]=pd.to_datetime(df["receivedate"])
    df["receivedate_month"]=df["receivedate_day"].dt.strftime("%Y年%m月")
    df["receivedate_year"]=df["receivedate_day"].dt.strftime("%Y")

    df['responsiblestaff_id']=pd.to_numeric(df['responsiblestaff_id'], downcast='integer') 

    userdf = pd.DataFrame(User.objects.all().values())
    userdf['name']=userdf['first_name'] + userdf['last_name']
    userdf['responsiblestaff_id']=userdf['id']
    userdf = userdf[['responsiblestaff_id', 'name']] #, 'email', 'is_staff', 'is_active']]
    # pd.to_numeric(userdf['responsiblestaff_id'])

    df=pd.merge(df,userdf)

    CorpModel.add_to_class("__str__", get_short_name)
    corpdf = CorpModel.objects.all()
    print('pre corpdf')
    print(corpdf)
    corpdf = pd.DataFrame({'corp_id':range(len(corpdf)),'corp':corpdf})
    # corpdf = pd.DataFrame(corpdf)
    # corpdf['corp_id']=corpdf['id']

    print('corpdf')
    print(corpdf)
    corpdf['corp_id']=corpdf['corp_id']+1
    #corpdf=corpdf['corp'].replace(to_replace='株式会社イエストホーム', value='', regex=True)
    # contdf = ContractModel.objects.all().values()
    contdf = pd.DataFrame(ContractModel.objects.all().values())
    contdf = contdf[['id', 'completed','corp_id', 'item8bill']]#,'responsiblestaff_id'
    print('contdf')
    print(contdf)
    contdf['contract_id']=contdf['id']

    contcorpdf = pd.merge(contdf,corpdf,on='corp_id')
    print('contcorpdf')
    print(contcorpdf)

    df= pd.merge(df,contcorpdf,on='contract_id',sort=True)
    df=df.sort_values(by='id_x')
    print('df')
    print(df)

        # df_month = df.groupby("receivedate_month").sum()["brokerage"]
    df_year = pd.DataFrame(df.groupby("receivedate_year").sum()["total"])
    df_year['total'] = df_year['total'].astype(int).apply('{:,}'.format)

    df_month = pd.DataFrame(df.groupby("receivedate_month").sum()["total"])
    df_month['total'] = df_month['total'].astype(int).apply('{:,}'.format)

    df_staff = pd.DataFrame(df.groupby("name").sum()["total"])
    df_staff['total'] = df_staff['total'].astype(int).apply('{:,}'.format)

    df_corp = pd.DataFrame(df.groupby("corp_id").sum()["total"])   
    df_corp['total'] = df_corp['total'].astype(int).apply('{:,}'.format)
    print('df_corp')
    print(df_corp)
    
    df_corp2=merge(corpdf, df_corp,on='corp_id')
    df_corp2=df_corp2[['corp', 'total']] 

    df_yearstaff = pd.DataFrame(df.groupby(["receivedate_year", "name"]).sum()["total"])
    df_yearstaff['total'] = df_yearstaff['total'].astype(int).apply('{:,}'.format)

    df_monthstaff = pd.DataFrame(df.groupby(["receivedate_month", "name"]).sum()["total"])
    df_monthstaff['total'] = df_monthstaff['total'].astype(int).apply('{:,}'.format)

    df_staffyear = pd.DataFrame(df.groupby(["name", "receivedate_year" ]).sum()["total"])
    df_staffyear['total'] = df_staffyear['total'].astype(int).apply('{:,}'.format)

    df_staffmonth = pd.DataFrame(df.groupby(["name", "receivedate_month"]).sum()["total"])
    df_staffmonth['total'] = df_staffmonth['total'].astype(int).apply('{:,}'.format)

    df2=df[['name', 'contract_id','total', 'receivedate_day']]

    mydict = {
        "df": df.to_html(classes="table"),
        "df_year": df_year.to_html(header=False, classes="table",index_names=False ),
        "df_month": df_month.to_html(header=False, classes="table",index_names=False ),
        "df_staff": df_staff.to_html(header=False, classes="table",index_names=False  ),
        "df_corp": df_corp2.to_html(header=False, index=False, classes="table",index_names=False  ),
        "df_yearstaff": df_yearstaff.to_html(header=False, classes="table" ,index_names=False ),
        "df_monthstaff": df_monthstaff.to_html(header=False, classes="table" ,index_names=False ),
        "df_staffyear": df_staffyear.to_html(header=False, classes="table" ,index_names=False ),
        "df_staffmonth": df_staffmonth.to_html(header=False, classes="table" ,index_names=False ),
        # "describe":df.describe().to_html,        
        # "df_month_chart": df99.plot
        "df2": df2.to_html(classes="table"),
    }
    print("mydict['df_corp']")
    print(mydict['df_corp'])
    CorpModel.add_to_class("__str__", get_normal_name)
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
