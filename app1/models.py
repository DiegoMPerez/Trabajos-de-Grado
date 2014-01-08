# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class CorreccionDirector(models.Model):
    cod_desarrollo = models.ForeignKey('Desarrollodefases', db_column='cod_desarrollo')
    fecha_correccion = models.DateField()
    correccion = models.CharField(max_length=2000, blank=True)
    enviar_corre_director = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'correccion_director'

class CorreccionDocente(models.Model):
    cod_desarrollo = models.ForeignKey('Desarrollodefases', db_column='cod_desarrollo')
    fecha = models.DateField()
    correccion_docente = models.CharField(max_length=2000, blank=True)
    enviar_corre_docente = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'correccion_docente'

class Defensa(models.Model):
    cod_defensa = models.IntegerField(primary_key=True)
    cod_trab_grado = models.ForeignKey('TrabajoDeGrado', db_column='cod_trab_grado')
    cod_jurado = models.ForeignKey('Jurados', db_column='cod_jurado')
    fecha_defensa = models.DateField(blank=True, null=True)
    aprobacion = models.CharField(max_length=1, blank=True)
    correccion = models.CharField(max_length=1000, blank=True)
    resolucio_field = models.CharField(db_column='resolucio_', max_length=10000, blank=True) # Field renamed because it ended with '_'.
    class Meta:
        managed = False
        db_table = 'defensa'

class Desarrollodefases(models.Model):
    cod_desarrollo = models.IntegerField(primary_key=True)
    fase = models.ForeignKey('Fasesdesarrollo', db_column='fase', blank=True, null=True)
    id_version = models.IntegerField()
    desarrollo = models.CharField(max_length=2000)
    fecha_desarrollo = models.DateField(blank=True, null=True)
    enviar_a_corregir = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'desarrollodefases'

class Director(models.Model):
    cod_ced_director = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'director'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class Docente(models.Model):
    codceddocente = models.CharField(primary_key=True, max_length=10)
    nombres = models.CharField(max_length=50, blank=True)
    apellidos = models.CharField(max_length=50, blank=True)
    tipocontrato = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'docente'

class Estudiante(models.Model):
    cod_ced_estudiante = models.CharField(primary_key=True, max_length=10)
    nombres = models.CharField(max_length=50, blank=True)
    apellidos = models.CharField(max_length=50, blank=True)
    lvl = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'estudiante'

    def __unicode__(self):
        return self.nombres + "d" + self.apellidos

class Fasesdesarrollo(models.Model):
    fase = models.CharField(max_length=20)
    id_version = models.ForeignKey('Versionamiento', db_column='id_version')
    estado = models.CharField(max_length=2, blank=True)
    lineamientos = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'fasesdesarrollo'

class Jurados(models.Model):
    cod_jurado = models.IntegerField(primary_key=True)
    jurado1 = models.CharField(max_length=100, blank=True)
    jurado2 = models.CharField(max_length=100, blank=True)
    jurado3 = models.CharField(max_length=100, blank=True)
    secretario_abogado = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'jurados'

class TrabajoDeGrado(models.Model):
    cod_trab_grado = models.IntegerField(primary_key=True)
    cod_ced_docente = models.ForeignKey(Docente, db_column='cod_ced_docente', blank=True, null=True)
    cod_ced_estudiante = models.ForeignKey(Estudiante, db_column='cod_ced_estudiante', blank=True, null=True)
    cod_ced_director = models.ForeignKey(Director, db_column='cod_ced_director', blank=True, null=True)
    carrera = models.CharField(max_length=100, blank=True)
    tema = models.CharField(max_length=100, blank=True)
    autor = models.CharField(max_length=100, blank=True)
    director = models.CharField(max_length=100, blank=True)
    entidad_auspicia = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    investigacion = models.CharField(max_length=200, blank=True)
    presupuesto = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'trabajo_de_grado'

class Versionamiento(models.Model):
    id_version = models.IntegerField(primary_key=True)
    cod_trab_grado = models.ForeignKey(TrabajoDeGrado, db_column='cod_trab_grado')
    fecha = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'versionamiento'

