from rest_framework import serializers
from .models import Server, PerfMonLog, HostInformation, \
    NetworkInformation, MemoryInformation, CPUInformation, DiskInformation, LoadAverage


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ['id', 'ip_address', 'description', 'name', 'server_is_active']


class ServerSerializerShort(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ['ip_address', 'server_is_active']


class HostInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostInformation
        fields = ['id', 'sys_name', 'host_name']


class NetworkInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkInformation
        fields = ['id', 'interface', 'status', 'mtu']


class DiskInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiskInformation
        fields = ['id', 'disk_name', 'mount_point', 'file_system_type', 'total', 'used']


class CPUInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUInformation
        fields = ['id', 'cpu_cores', 'cpu_physical_cores',
                  'cpu_frequency_current', 'cpu_frequency_minimum', 'cpu_frequency_maximum']


class MemoryInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryInformation
        fields = ['id', 'total', 'used', 'percent']


class LoadAverageInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadAverage
        fields = ['id', 'one_minute', 'five_minutes', 'fifteen_minutes']


class PerfMonLogSerializer(serializers.ModelSerializer):
    host_information = HostInformationSerializer(many=True)
    network_information = NetworkInformationSerializer(many=True)
    disk_information = DiskInformationSerializer(many=True)
    cpu_information = CPUInformationSerializer(many=True)
    memory_information = MemoryInformationSerializer(many=True)
    load_average = LoadAverageInformationSerializer(many=True)

    class Meta:
        model = PerfMonLog
        fields = ['id', 'created_at', 'host_information', 'network_information',
                  'disk_information', 'cpu_information', 'memory_information', 'load_average']

    def create(self, validated_data):

        host_information = validated_data.pop('host_information')
        network_information = validated_data.pop('network_information')
        disk_information = validated_data.pop('disk_information')
        cpu_information = validated_data.pop('cpu_information')
        memory_information = validated_data.pop('memory_information')
        load_average = validated_data.pop('load_average')

        perf_mon_log = PerfMonLog.objects.create(**validated_data)

        for item in host_information:
            HostInformation.objects.create(perf_mon_log=perf_mon_log, **item)

        for item in network_information:
            NetworkInformation.objects.create(perf_mon_log=perf_mon_log, **item)

        for item in disk_information:
            DiskInformation.objects.create(perf_mon_log=perf_mon_log, **item)

        for item in cpu_information:
            CPUInformation.objects.create(perf_mon_log=perf_mon_log, **item)

        for item in memory_information:
            MemoryInformation.objects.create(perf_mon_log=perf_mon_log, **item)

        for item in load_average:
            LoadAverage.objects.create(perf_mon_log=perf_mon_log, **item)

        return perf_mon_log
