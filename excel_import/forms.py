# 创建人;Ye
# 创建时间 : 19.4.12  11:30

from excel_import import models
from django import forms
from django.forms.models import modelform_factory


class BxContrastForm(forms.ModelForm):
    class Meta:
        model = models.BxContrast
        fields = '__all__'


BxDeviceForm = modelform_factory(models.BxDevice, fields="__all__")

BxEverydayContrastDataForm = modelform_factory(models.BxEverydayContrastData, fields="__all__")

BxEverydayDataForm = modelform_factory(models.BxEverydayData, fields="__all__")

BxLiveUrlForm = modelform_factory(models.BxLiveUrl, fields="__all__")

BxPerformArrangeForm = modelform_factory(models.BxPerformArrange, fields="__all__")

BxRoiTrafficForm = modelform_factory(models.BxRoiTraffic, fields="__all__")

BxStationDetailForm = modelform_factory(models.BxStationDetail, fields="__all__")

BxTextForm = modelform_factory(models.BxText, fields="__all__")
