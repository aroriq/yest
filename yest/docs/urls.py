from django.urls import path
from .views import customerList, DocsHiyomeisai
from docs import views
# app_name = 'docs_app'
urlpatterns = [
    # path("staff_top/", views.staff_top, name="staff_top"),
    # path("staff_new/", views.staff_new, name="staff_new"),
    # path("staff/<int:staff_id>/", views.staff_detail, name="staff_detail"),
    # path("staff/<int:staff_id>/edit/", views.staff_edit, name="staff_edit"),
    path("contract_top/", views.contract_top, name="contract_top"),
    path("contract_new/", views.contract_new, name="contract_new"),
    path("contract/<int:contract_id>/", views.contract_detail, name="contract_detail"),
    path("contract/<int:contract_id>/edit/", views.contract_edit, name="contract_edit"),

    path("meisai_print/<int:contract_id>/", views.meisai_print, name="meisai_print"),
    path("kanrimeisai_print/<int:contract_id>/", views.kanrimeisai_print, name="kanrimeisai_print"),
    path("zanmu_print/<int:contract_id>/", views.zanmu_print, name="zanmu_print"),
    path("report_print/<int:contract_id>/", views.report_print, name="report_print"),

    path("receipt/<int:contract_id>/", views.receipt_print, name="receipt_print"),
    path("receipt/<int:contract_id>/edit/", views.receipt_edit, name="receipt_edit"),

    path("keyreceipt_print/<int:contract_id>/", views.keyreceipt_print, name="keyreceipt_print"),
    path("fax_print/<int:contract_id>/", views.fax_print, name="fax_print"),

    path("culc/", views.CulcView.as_view(), name="culc"),

    path('customerlist/', customerList, name='customerlist'),
    path('hiyomeisai/', DocsHiyomeisai, name='hiyomeisai'),
    # path('review_detail/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
    # path('review_create/', ReviewCreate.as_view(), name='review_create'),
    # path('review_delete/<int:pk>', ReviewDelete.as_view(), name='review_delete'),
    # path('review_update/<int:pk>', ReviewUpdate.as_view(), name='review_update'),
]