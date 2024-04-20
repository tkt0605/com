# Generated by Django 5.0.4 on 2024-04-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("xlink", "0003_alter_account_detail_alter_account_hobby_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="detail",
            field=models.CharField(
                choices=[
                    ("高校生", "高校生"),
                    ("中学生", "中学生"),
                    ("・・・・", "・・・・"),
                    ("社会人", "社会人"),
                    ("小学生", "小学生"),
                    ("大学生", "大学生"),
                ],
                default="・・・・",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="hobby",
            field=models.CharField(
                choices=[
                    ("運動", "運動"),
                    ("読書", "読書"),
                    ("・・・・", "・・・・"),
                    ("プログラミング", "プログラミング"),
                    ("映画", "映画"),
                    ("ゲーム", "ゲーム"),
                    ("VR/AR", "VR/AR"),
                    ("PC", "PC"),
                    ("TV", "TV"),
                ],
                default="・・・・",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="icon",
            field=models.ImageField(
                default="media/defult/5770f01a32c3c53e90ecda61483ccb08.jpg/",
                upload_to="icon/",
                verbose_name="アイコン",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="image",
            field=models.ImageField(
                default="media/defult/real-grayscale-marble-texture-background_37787-1754.jpg/",
                upload_to="backimage/",
                verbose_name="バックイメージ",
            ),
        ),
    ]