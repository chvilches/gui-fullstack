from django.db import models


class CostCenter(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class DocumentCostCenter(models.Model):
    document = models.ForeignKey('sii.PurchaseBook', on_delete=models.CASCADE)
    cost_center = models.ForeignKey('CostCenter', on_delete=models.CASCADE)
    proportion = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    amount = models.IntegerField(default=0)


