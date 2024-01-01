# Generated by Django 4.2.7 on 2024-01-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_rename_load_approve_transactions_loan_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='bank_rupt',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transactions_type',
            field=models.IntegerField(choices=[(1, 'Deposite'), (2, 'Withdraw'), (3, 'Loan'), (4, 'Loan Paid'), (5, 'Send Money')], null=True),
        ),
    ]
