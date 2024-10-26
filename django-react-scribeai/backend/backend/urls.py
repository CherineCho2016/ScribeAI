from django.urls import path
from scribeai.views import JsonRecordList, JsonRecordDetail

urlpatterns = [
    path('json-records/', JsonRecordList.as_view(), name='json-record-list'),
    path('json-records/<int:pk>/', JsonRecordDetail.as_view(), name='json-record-detail'),
]