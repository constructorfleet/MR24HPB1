from dependency_injector import containers, providers

from MR24HPB1.data.sensor.sensor import Sensor


class SensorContainer(containers.DeclarativeContainer):
    frame = providers.Singleton(

    )
    sensor = providers.Dependency(Sensor)

