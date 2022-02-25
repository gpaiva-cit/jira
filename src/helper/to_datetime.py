from datetime import datetime
from pytz import timezone


def to_datetime(day: str, time: str) -> datetime:
    """
    Args:
        day (str): Padrão dia/mês/ano
        time (str): Padrão hora/minuto

    Returns:
        datetime: Data e hora convertido em datetime, no fuso de São Paulo
    """

    day = day.split('/')
    day = {
        'day': int(day[0]),
        'month': int(day[1]),
        'year': int(day[2])
    }

    time = time.split(':')
    time = {
        'hour': int(time[0]),
        'minute': int(time[1])
    }

    return datetime(
        day['year'], day['month'], day['day'],
        time['hour'], time['minute']
    ).astimezone(
        timezone('America/Sao_Paulo')
    )
