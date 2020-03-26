from django.db import models

class Biodata(models.Model):
    npm = models.CharField(primary_key=True, max_length=15)
    nama = models.CharField(max_length=100, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    deskripsi = models.TextField()

    class Meta:
        managed = False
        db_table = 'biodata'

class JenjangPendidikan(models.Model):
    id_jenjang = models.AutoField(primary_key=True)
    nama_jenjang = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jenjang_pendidikan'


class Pendidikan(models.Model):
    id_pendidikan = models.AutoField(primary_key=True)
    id_jenjang = models.ForeignKey(JenjangPendidikan, models.DO_NOTHING, db_column='id_jenjang')
    nama_sekolah = models.CharField(max_length=200, blank=True, null=True)
    thn_lulus = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pendidikan'


