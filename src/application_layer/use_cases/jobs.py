from datetime import datetime, timedelta

from src.domain_layer.models.payment import Payment

class JobsUseCase:
    
    @classmethod
    def send_slips(cls):
        
        search_date = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=10)
        payments = Payment.get_by_debtDueDate(debtDueDate=search_date)
        Payment.send_slips(payments=payments)