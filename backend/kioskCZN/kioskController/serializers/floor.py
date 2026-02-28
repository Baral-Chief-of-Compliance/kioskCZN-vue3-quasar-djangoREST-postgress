from datetime import date

from rest_framework import serializers

from kioskController.models import Floor, Room, WorkerInDepartment


class FloorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floor
        fields = '__all__'


class WorkerInDepartmentShortSerializer(serializers.ModelSerializer):
    """Упрощенный сериализатор для сотрудников в комнате"""
    fio = serializers.SerializerMethodField()
    post_name = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    absent = serializers.SerializerMethodField()

    class Meta:
        model = WorkerInDepartment
        fields = ['id', 'fio', 'post_name', 'phone', 'email', 'absent', 'head_of_dep']

    def get_fio(self, obj):
        return obj.worker.fio if obj.worker else 'Неизвестно'

    def get_post_name(self, obj):
        return obj.post.name if obj.post else 'Отсутствует'

    def get_phone(self, obj):
        return obj.worker.phone if obj.worker else None

    def get_email(self, obj):
        return obj.worker.email if obj.worker else None

    def get_absent(self, obj):
        return obj.worker.absent if obj.worker else False


class RoomWithWorkersSerializer(serializers.ModelSerializer):
    """Сериализатор для комнаты с сотрудниками"""
    workers = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['id', 'name', 'vector_info', 'visible', 'workers']

    def get_workers(self, obj):
        """Получаем всех сотрудников, которые находятся в этой комнате и visible=True"""
        today = date.today()

        workers_in_dep = WorkerInDepartment.objects.filter(
            worker__room=obj,
            visible=True,
            date_get_info=today
        ).select_related('worker', 'post').distinct()
        
        return WorkerInDepartmentShortSerializer(workers_in_dep, many=True).data
    

class FloorFullInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для получения информации об этаже с кабинетами и сотрудниками"""
    rooms = serializers.SerializerMethodField()

    class Meta:
        model = Floor
        fields = ['id', 'number', 'building_img', 'rooms']

    def get_rooms(self, obj):
        """Получаем все комнаты этажа, у которых есть vector_info и visible=True"""
        rooms = Room.objects.filter(
            floor=obj,
            vector_info__isnull=False,  # есть vector_info
            visible=True                 # visible=True
        ).exclude(vector_info__exact='')  # дополнительно исключаем пустые строки
        
        return RoomWithWorkersSerializer(rooms, many=True).data