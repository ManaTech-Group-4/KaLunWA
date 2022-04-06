from datetime import datetime


def to_formal_mdy(date:datetime)->str:
        return f'{date.strftime("%B")} {date.day}, {date.year}'