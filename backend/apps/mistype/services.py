from apps.common.utils import HandleExceptions
from django.db import transaction

from .models import Miss


class MistypeService:

    @transaction.atomic
    @HandleExceptions()
    def insert_mistypes(self, user_id, miss_data):
        """ミスタイプをインサートまたは更新"""
        inserted_data = []

        for data in miss_data:
            miss_char = data.get('miss_char')
            miss_count = data.get('miss_count', 0)
            """miss_charがアルファベットかどうかをチェック"""
            if not miss_char.isalpha() or len(miss_char) != 1:
                continue

            miss_instance, created = Miss.objects.get_or_create(user_id=user_id,
                                                                miss_char=miss_char,
                                                                defaults={'miss_count': miss_count})

            if not created:
                miss_instance.miss_count += miss_count
                miss_instance.save()

            inserted_data.append({
                'user': user_id,
                'miss_char': miss_instance.miss_char,
                'miss_count': miss_instance.miss_count,
            })

        return inserted_data

    def get_top_mistypes(self, user_id, count):
        """トップミスタイプ取得"""
        return Miss.objects.filter(user_id=user_id).order_by('-miss_count')[:count]
