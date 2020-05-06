from django.urls import path
from .views import *
from .delivery_views import *


urlpatterns = [
    path('create/', MTPCreateViewNew.as_view()),
    path('update/', MTPUpdateView.as_view()),
    path('drop-down/', MTPDropDownView.as_view()),
    # path('createnew/', MTPCreateViewNew.as_view())
    path('list/', MTPListView.as_view()),
    path('retrieve/', MTPRetrieveView.as_view()),
    path('test/test/<int:pk>', TestTestClass.as_view()),
    path('delivery/update/',UpdateDeliveryRecordView.as_view()),
    path('records/read/', MTPReadByHospital.as_view()),

    path('delete/', MTPDeleteView.as_view()),

    path('delivery/', CreateDeliveryRecordView.as_view()),
    path('delivery/list/', DeliveryRecordsListing.as_view()),
    path('delivery/read/', ReadDeliveryRecordView.as_view()),
    path('delivery/delete/', DeleteDeliveryRecord.as_view()),

]
