from dataclasses import dataclass
from datetime import date
from src.application_layer.adapter.payment_repository import SQLAlchemyPaymentRepository
from src.application_layer.adapter.slip_services import SlipServices

@dataclass
class Payment:

    name: str
    governmentId: str
    email: str
    debtAmount: float
    debtDueDate: date
    debtID: str
            
    @classmethod
    def get_by_debtDueDate(cls, debtDueDate: date):
        return SQLAlchemyPaymentRepository.get_by_debtDueDate(debtDueDate=debtDueDate)
    
    @classmethod
    def send_slips(cls, payments: list['Payment']):
        SlipServices.send_slip_email(payments=payments)
        return 