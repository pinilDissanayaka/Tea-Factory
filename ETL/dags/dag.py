from datetime import datetime, timedelta
from models import SupplyData
from database import session



def get_data():
    supply=session.query(SupplyData).filter_by(
        created_at=datetime.now() - timedelta(days=1)
    ).all()

    return supply


def send_notification(data):
    for d in data:
        print(d.quantity)

