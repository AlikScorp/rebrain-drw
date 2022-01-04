from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Server(models.Model):

    name = models.CharField(verbose_name='Name', max_length=255)
    ip_address = models.GenericIPAddressField(verbose_name='IP', max_length=16, default='0.0.0.0')
    description = models.TextField(verbose_name='Description', max_length=255, default='no_description')
    server_is_active = models.BooleanField(verbose_name="Is server active", default=False)

    class Meta:
        managed = True
        verbose_name = 'Server'


class PerfMonLog(models.Model):
    created_at = models.DateTimeField(verbose_name="Created", auto_now_add=True)

    class Meta:
        db_table = "perf_mon_log"
        verbose_name = 'Performance Monitor Log'

    def __str__(self):
        return f"{self.pk}. {self.created_at}"


class HostInformation(models.Model):
    sys_name = models.CharField(verbose_name="System name", max_length=50)
    host_name = models.CharField(verbose_name="Host name", max_length=50)
    perf_mon_log = models.ForeignKey(PerfMonLog, related_name="host_information", on_delete=models.CASCADE)

    class Meta:
        db_table = "host_information"
        verbose_name = "Host information"

    def __str__(self):
        return f"sysname: {self.sys_name}, hostname: {self.host_name}"


class NetworkInformation(models.Model):
    interface = models.CharField(verbose_name="Interface", max_length=50)
    status = models.BooleanField(verbose_name="Status")
    mtu = models.IntegerField(verbose_name="MTU", default=0,
                              validators=[MinValueValidator(0), MaxValueValidator(20000)])
    perf_mon_log = models.ForeignKey(PerfMonLog, related_name="network_information", on_delete=models.CASCADE)

    class Meta:
        db_table = "network_information"
        verbose_name = "Network information"

    def __str__(self):
        return f"id: {self.pk}, interface: {self.interface}, status: {'Up' if self.status else 'Down'}, 'mtu': {self.mtu}"


class DiskInformation(models.Model):
    disk_name = models.CharField(verbose_name="Disk name", max_length=50)
    mount_point = models.CharField(verbose_name="Mount point", max_length=255)
    file_system_type = models.CharField(verbose_name="File system type", max_length=10)
    total = models.BigIntegerField(verbose_name="Total space", default=0, validators=[MinValueValidator(0)])
    used = models.BigIntegerField(verbose_name="Used space", default=0, validators=[MinValueValidator(0)])
    perf_mon_log = models.ForeignKey(PerfMonLog, related_name="disk_information", on_delete=models.CASCADE)

    class Meta:
        db_table = "disk_information"
        verbose_name = "Disk information"

    def __str__(self):
        return f"id: {self.pk}, disk: {self.disk_name}, mountpoint: {self.mount_point}, " \
               f"file_system_type: {self.file_system_type}, total: {self.total}, used: {self.used}"


class MemoryInformation(models.Model):
    total = models.BigIntegerField(verbose_name="Memory total", default=0, validators=[MinValueValidator(0)])
    used = models.BigIntegerField(verbose_name="Memory in use", default=0, validators=[MinValueValidator(0)])
    percent = models.FloatField(verbose_name="Memory percent", default=0.0,
                                validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    perf_mon_log = models.ForeignKey(PerfMonLog, related_name="memory_information", on_delete=models.CASCADE)

    class Meta:
        db_table = "memory_information"
        verbose_name = "Memory information"

    def __str__(self):
        return f"id: {self.pk}; memory_total: {self.total}; memory_used: {self.used}; memory_percent: {self.percent}"


class CPUInformation(models.Model):
    cpu_cores = models.IntegerField(verbose_name="Cores number", default=0,
                                    validators=[MinValueValidator(0), MaxValueValidator(100)])
    cpu_physical_cores = models.IntegerField(verbose_name="Physical cores", default=0,
                                             validators=[MinValueValidator(0), MaxValueValidator(100)])
    cpu_frequency_current = models.FloatField(verbose_name="CPU Frequency current", default=0.0,
                                              validators=[MinValueValidator(0.0), MaxValueValidator(10000.0)])
    cpu_frequency_minimum = models.FloatField(verbose_name="CPU Frequency minimum", default=0.0,
                                              validators=[MinValueValidator(0.0), MaxValueValidator(10000.0)])
    cpu_frequency_maximum = models.FloatField(verbose_name="CPU Frequency maximum", default=0.0,
                                              validators=[MinValueValidator(0.0), MaxValueValidator(10000.0)])
    perf_mon_log = models.ForeignKey(PerfMonLog, related_name="cpu_information", on_delete=models.CASCADE)

    class Meta:
        db_table = "cpu_information"
        verbose_name = "CPU information"

    def __str__(self):
        return f"id: {self.pk}; cpu_cores: {self.cpu_cores}; cpu_physical_cores: {self.cpu_physical_cores}; " \
               f"cpu_frequency: current - {self.cpu_frequency_current}, " \
               f"minimum - {self.cpu_frequency_minimum}, maximum - {self.cpu_frequency_maximum}"


class LoadAverage(models.Model):
    one_minute = models.FloatField(verbose_name="1 min.", default=0.0, validators=[MinValueValidator(0.0)])
    five_minutes = models.FloatField(verbose_name="5 min.", default=0.0, validators=[MinValueValidator(0.0)])
    fifteen_minutes = models.FloatField(verbose_name="15 min.", default=0.0, validators=[MinValueValidator(0.0)])
    perf_mon_log = models.ForeignKey(PerfMonLog, related_name="load_average", on_delete=models.CASCADE)

    class Meta:
        db_table = "load_average"
        verbose_name = "Load average"

    def __str__(self):
        return f"id: {self.pk}; 1 min.: {self.one_minute}; 5 min.: {self.five_minutes}; 15 min.: {self.fifteen_minutes}"
