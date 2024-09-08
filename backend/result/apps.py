from django.apps import AppConfig


class ResultConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'result'

    def ready(self):
        from .models import Rank
        """ アプリ起動時にデフォルトの「メンバー」ランクを追加 """
        Rank.objects.get_or_create(rank='メンバー')