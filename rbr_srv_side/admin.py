from django.contrib import admin
from .models import Server, PerfMonLog, HostInformation, NetworkInformation, \
    CPUInformation, MemoryInformation, DiskInformation, LoadAverage


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'name', 'description', 'server_is_active')


@admin.register(PerfMonLog)
class PerfMonLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')


@admin.register(HostInformation)
class HostInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sys_name', 'host_name', 'perf_mon_log')


@admin.register(NetworkInformation)
class NetworkInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'interface', 'status', 'mtu', 'perf_mon_log')


@admin.register(DiskInformation)
class DiskInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'disk_name', 'mount_point', 'file_system_type', 'total', 'used', 'perf_mon_log')


@admin.register(MemoryInformation)
class MemoryInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'used', 'percent', 'perf_mon_log')


@admin.register(CPUInformation)
class CPUInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpu_cores', 'cpu_physical_cores', 'cpu_frequency_current',
                    'cpu_frequency_minimum', 'cpu_frequency_maximum', 'perf_mon_log')


@admin.register(LoadAverage)
class LoadAverageAdmin(admin.ModelAdmin):
    list_display = ('id', 'one_minute', 'five_minutes', 'fifteen_minutes', 'perf_mon_log')

