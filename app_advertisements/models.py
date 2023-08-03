from django.db import models
from django.contrib import admin
from django.utils import timezone


class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text='Отметьте если торг уместен')
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone, html
        if self.created_dt.date() == timezone.now().date():
            created_time = self.created_dt.time().strftime("%H:%M:%S")
            return html.format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_dt.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.action(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone, html
        if self.updated_dt.date() == timezone.now().date():
            updated_time = self.updated_dt.time().strftime("%H:%M:%S")
            return html.format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', updated_time
            )
        return self.updated_dt.strftime("%d.%m.%Y в %H:%M:%S")
