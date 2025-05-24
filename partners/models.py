from django.db import models

class PartnerApplication(models.Model):
    STATUS_CHOICES = [
        ('new', 'Нова'),
        ('in_review', 'На розгляді'),
        ('approved', 'Схвалена'),
        ('rejected', 'Відхилена'),
    ]
    
    company_name = models.CharField(max_length=100, verbose_name='Назва організації')
    contact_person = models.CharField(max_length=100, verbose_name='Контактна особа')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    website = models.URLField(blank=True, null=True, verbose_name='Веб-сайт')
    description = models.TextField(verbose_name='Опис')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    
    def __str__(self):
        return f"{self.company_name} - {self.get_status_display()}"
    
    class Meta:
        verbose_name = 'Заявка на партнерство'
        verbose_name_plural = 'Заявки на партнерство'
        ordering = ['-created_at']