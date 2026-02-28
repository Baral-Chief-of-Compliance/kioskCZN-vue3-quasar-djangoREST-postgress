from rest_framework import serializers

from kioskController.models import Worker, WorkerInDepartment


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'


class WorkerInDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerInDepartment
        fields = '__all__'


class WorkerInDepartmentSearch(serializers.Serializer):
    """Сериализатор для поиска сотрудников"""
    worker_id = serializers.IntegerField(min_value=1)
    pc = serializers.IntegerField(min_value=1)
    department_name = serializers.CharField(max_length=256)


class WorkInDepartmentFullInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для получения полной информации о сотруднике"""

    fio = serializers.SerializerMethodField(
        'get_fio'
    )

    post_name = serializers.SerializerMethodField(
        'get_post_name'
    )

    room_name = serializers.SerializerMethodField(
        'get_room_name'
    )

    room_id = serializers.SerializerMethodField(
        'get_room_id'
    )

    room_show = serializers.SerializerMethodField(
        'get_room_show_status'
    )

    floor = serializers.SerializerMethodField(
        'get_floor'
    )

    class Meta:
        model = WorkerInDepartment
        fields = '__all__'

    
    def get_fio(self, obj: WorkerInDepartment):
        """Получить фио сотрудника"""
        worker = obj.worker
        if worker:
            return worker.fio
        else:
            return 'Неизветно'

    def get_post_name(self, obj: WorkerInDepartment):
        """Получить наименование должности сотрудника"""
        post = obj.post

        if post:
            return post.name
        else:
            return 'Отсутствует'

    def get_room_name(self, obj: WorkerInDepartment):
        """Получить наименование кабинета сотрудника"""

        worker = obj.worker

        if worker:
            room = worker.room
            if room:
                return room.name
            else:
                return 'Отсутствует'
        else:
            return 'Отсутствует'

    def get_room_id(self, obj: WorkerInDepartment):
        """Получить id кабинета сотрудника"""
        
        worker = obj.worker

        if worker:
            room = worker.room
            if room:
                return room.id
            else:
                return None
        else:
            return None
        
    def get_floor(self, obj: WorkerInDepartment):
        """Получить этаж, на котором находится кабинет пользователя"""
        room_id = self.get_room_id(obj)

        if room_id:
            room = obj.worker.room
            floor = room.floor
            if floor:
                return floor.number
            else:
                None
        else:
            return None
        
    def get_room_show_status(self, obj: WorkerInDepartment):
        room_id = self.get_room_id(obj)

        if room_id:
            room = obj.worker.room
            if room.vector_info:
                return True
            else:
                return False
        else:
            return False