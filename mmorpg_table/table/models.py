from django.contrib.auth.models import User
from django.db import models


class Categories(models.Model):
    """Класс Categories для создания экземпляров категорий, к которым относятся объявления"""
    categories = models.CharField(max_length=30)                                        # Категория (10 шт)


class Ads(models.Model):
    """Класс Ads для создания экземпляров объявлений"""
    date_time_generation = models.DateTimeField(auto_now_add=True)                      # Дата и время создания
    header = models.CharField(max_length=250)                                           # Заголовок
    text_and_multimedia = models.TextField()                           # !!!!! Требуется замена на WYSIWYG - поле
    id_users = models.ForeignKey(User, on_delete=models.CASCADE)                       # id автора объявления
    id_categories = models.ForeignKey(Categories, on_delete=models.CASCADE)             # id категории объявления


class Reviews(models.Model):
    """Класс Reviews для создания экземпляров откликов пользователей на объявления"""
    text = models.TextField()                                                           # текст комментария
    id_users_rev = models.ForeignKey(User, on_delete=models.CASCADE)                    # id автора комментария
    id_ads = models.ForeignKey(Ads, on_delete=models.CASCADE)                           # id статьи
    rev_status = models.BooleanField(default=False)                                     # принят или нет отзыв
