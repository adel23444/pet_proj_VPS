from django.db import models


class VPS(models.Model):
    STARTED = 1
    STOPPED = 0
    BLOCKED = -1

    STATUS_CHOISES = (
        (STARTED, "started"),
        (STOPPED, "stopped"),
        (BLOCKED, "blocked")
    )

    uid = models.IntegerField(
        verbose_name='UID',
        help_text='UID',
        db_column="UID",
        primary_key=True,
        null=False,
    )
    cpu = models.IntegerField(
        verbose_name='Ядра CPU',
        help_text='Ядра CPU',
        db_column="CPU",
        null=False
    )
    ram = models.IntegerField(
        verbose_name='Объем RAM (в ГБ)',
        help_text='Объем RAM (в ГБ)',
        db_column="RAM",
        null=False
    )
    hdd = models.IntegerField(
        verbose_name='Объем HDD (в ТБ)',
        help_text='Объем HDD (в ТБ)',
        db_column="HDD",
        null=False
    )
    status = models.IntegerField(
        verbose_name="Статус",
        help_text="Статус",
        db_column="status",
        choices=STATUS_CHOISES
    )

    def __str__(self):
        return f'CPU: {self.cpu}\nRAM: {self.ram}\nHDD: {self.hdd}\nUID: {self.uid}\n Curr status: {self.status}'