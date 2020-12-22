from django.db import models


# клиент
class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    policy_number = models.PositiveIntegerField() # номер страхового полиса

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name,)

# фонд
class Fund(models.Model):
    balance = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

# договор
class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)
    date = models.DateField() # дата заключения
    insurance_amount = models.PositiveIntegerField() # сумма размера страхования
    conditions = models.TextField()

    def __str__(self):
        return "%s: %s" % (self.date, self.client, )
