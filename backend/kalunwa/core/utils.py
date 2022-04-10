from datetime import datetime


def to_formal_mdy(date:datetime)->str:
        if date:
                return f'{date.strftime("%B")} {date.day}, {date.year}' 
        else: return None