from datetime import datetime
def get_days_from_today(date):
    try:
     given = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError , TypeError):
        return None
    today = datetime.today().date()
    return (today - given).days




