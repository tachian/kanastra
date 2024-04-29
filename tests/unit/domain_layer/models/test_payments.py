from datetime import datetime
from unittest import mock

from src.application_layer.adapter.payment_repository import SQLAlchemyPaymentRepository
from src.application_layer.adapter.slip_services import SlipServices
from src.domain_layer.models.payment import Payment


@mock.patch.object(SQLAlchemyPaymentRepository, 'get_by_debtDueDate')
def test_get_by_debtDueDate(mock_get_by_debtDueDate):
    
    search_date = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    Payment.get_by_debtDueDate(debtDueDate=search_date)
    
    mock_get_by_debtDueDate.assert_called_once_with(debtDueDate=search_date)
    
@mock.patch.object(SlipServices, 'send_slip_email')
def test_send_slips(mock_send_slip_email):
    
    payment = Payment(
        name='Teste',
        governmentId='Teste',
        email='teste@teste.com',
        debtAmount=100,
        debtDueDate=datetime.now(),
        debtID='Teste')
    list = [payment]
    Payment.send_slips(payments=list)
    
    mock_send_slip_email.assert_called_once_with(payments=list) 