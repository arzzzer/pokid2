from django.db import models


class Child(models.Model):
    child_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField(blank=True, null=True)
    doctor_id = models.IntegerField(blank=True, null=True)
    mac_address = models.TextField(blank=True, null=True)
    child_name = models.TextField(blank=True, null=True)
    child_surname = models.TextField(blank=True, null=True)
    temp_min = models.FloatField(blank=True, null=True)
    temp_max = models.FloatField(blank=True, null=True)
    pulse_min = models.IntegerField(blank=True, null=True)
    pulse_max = models.IntegerField(blank=True, null=True)
    ox_min = models.IntegerField(blank=True, null=True)
    ox_max = models.IntegerField(blank=True, null=True)
    satur_min = models.IntegerField(blank=True, null=True)
    satur_max = models.IntegerField(blank=True, null=True)
    timer = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'child'


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.TextField()
    doctor_surname = models.TextField(blank=True, null=True)
    work_place = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    d_login = models.TextField(blank=True, null=True)
    d_password = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'doctor'


class Measure(models.Model):
    measure_id = models.AutoField(primary_key=True)
    is_saved = models.IntegerField(blank=True, null=True)
    is_okay = models.IntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    pulse = models.IntegerField(blank=True, null=True)
    ox = models.IntegerField(blank=True, null=True)
    satur = models.IntegerField(blank=True, null=True)
    date_time = models.TextField(blank=True, null=True)
    child_id = models.IntegerField()

    def __str__(self):
        return str(self.measure_id)

    class Meta:
        db_table = 'measure'


class Message(models.Model):
    date_time = models.AutoField(primary_key=True)
    sender = models.IntegerField()
    recipient = models.IntegerField()
    text = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'message'


class Parent(models.Model):
    parent_id = models.AutoField(primary_key=True, blank=True)
    p_login = models.TextField()
    p_password = models.TextField(blank=True, null=True)
    parent_name = models.TextField()
    parent_surname = models.TextField()

    class Meta:
        db_table = 'parent'