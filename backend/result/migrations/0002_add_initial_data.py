from django.db import migrations

def create_initial_data(apps, schema_editor):
    """ Rankモデルにデータを追加 """
    Rank = apps.get_model('result', 'Rank')
    Rank.objects.get_or_create(rank_id=1, defaults={'rank': "メンバー", 'del_flg': False})
    Rank.objects.get_or_create(rank_id=2, defaults={'rank': "主任", 'del_flg': False})
    Rank.objects.get_or_create(rank_id=3, defaults={'rank': "係長", 'del_flg': False})
    Rank.objects.get_or_create(rank_id=4, defaults={'rank': "課長", 'del_flg': False})
    Rank.objects.get_or_create(rank_id=5, defaults={'rank': "部長", 'del_flg': False})
    Rank.objects.get_or_create(rank_id=6, defaults={'rank': "取締役", 'del_flg': False})
    Rank.objects.get_or_create(rank_id=7, defaults={'rank': "社長", 'del_flg': False})

    """ Langモデルにデータを追加　 """
    Lang = apps.get_model('result', 'Lang')
    Lang.objects.get_or_create(lang_id=1, defaults={'lang': "日本語", 'del_flg': False})
    Lang.objects.get_or_create(lang_id=2, defaults={'lang': "英語", 'del_flg': False})

    """ Diffモデルにデータを追加 """
    Diff = apps.get_model('result', 'Diff')
    Diff.objects.get_or_create(diff_id=1, defaults={'diff': "イージー", 'del_flg': False})
    Diff.objects.get_or_create(diff_id=2, defaults={'diff': "ノーマル", 'del_flg': False})
    Diff.objects.get_or_create(diff_id=3, defaults={'diff': "ハード", 'del_flg': False})

    """ Userモデルにデータを追加 """
    User = apps.get_model('result', 'User')
    Rank = apps.get_model('result', 'Rank')

    """ 既存の rank_id=1 の Rank インスタンスを取得または作成 """
    rank, _ = Rank.objects.get_or_create(rank_id=1, defaults={'rank': "メンバー", 'del_flg': False})

    # User モデルにデータを追加
    user, _ = User.objects.get_or_create(user_id=1, defaults={'rank_id': rank})

    # Scoreモデルにデータを追加
    Score = apps.get_model('result', 'Score')
    lang = Lang.objects.get_or_create(lang_id=1)[0]
    diff = Diff.objects.get_or_create(diff_id=1)[0]
    
    # 正しいフィールド値を使用
    Score.objects.get_or_create(user_id=user, lang_id=lang, diff_id=diff, defaults={'score': 10})

class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
