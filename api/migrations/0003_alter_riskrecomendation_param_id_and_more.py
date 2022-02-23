# Generated by Django 4.0.2 on 2022-02-23 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_supportedapp_supportedappparam_riskrecomendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskrecomendation',
            name='param_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_recomendations', to='api.riskparam'),
        ),
        migrations.AlterField(
            model_name='supportedappparam',
            name='app_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supported_app_params', to='api.supportedapp'),
        ),
        migrations.AlterField(
            model_name='supportedappparam',
            name='param_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='supported_app_params', to='api.riskparam'),
        ),
    ]
