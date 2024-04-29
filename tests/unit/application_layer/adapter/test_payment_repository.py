import pytest
from datetime import datetime
from unittest import mock

from src.app import db
from src.application_layer.adapter.payment_repository import SQLAlchemyPaymentRepository
from src.application_layer.persistency.tables import payment_table

@pytest.fixture()
def create_payment(app):
    payment = payment_table.insert().values(
        name = 'Teste',
        governmentId = '1234567890',
        email = 'teste@teste.com',
        debtAmount = 100,
        debtDueDate = datetime.strptime('2024-04-28', '%Y-%m-%d'),
        debtID = 'teste debtId')
    db.session.execute(payment)
    db.session.flush()

def test_get_by_debtDueDate(create_payment, app):
    
    debtDueDate = datetime.strptime('2024-04-28', '%Y-%m-%d')
    payments = SQLAlchemyPaymentRepository.get_by_debtDueDate(debtDueDate=debtDueDate)
    
    assert len(payments) == 1
    assert payments[0].name == 'Teste'
    
@mock.patch('src.application_layer.adapter.payment_repository.logger.exception')
@mock.patch('src.application_layer.adapter.payment_repository.db.session.query')
def test_get_by_debtDueDate_when_return_exception(mock_query, mock_logger, app):
    
    msg = 'Error while trying to get payments'
    mock_query.side_effect = Exception(msg)
    debtDueDate = datetime.strptime('2024-04-28', '%Y-%m-%d')
    
    with pytest.raises(Exception,
        match=msg):
        SQLAlchemyPaymentRepository.get_by_debtDueDate(debtDueDate=debtDueDate)
    
    mock_logger.assert_called_once_with(msg, extra={
        "props": {
            "service": "SQLite",
            "service method": "get_by_debtDueDate",
            "error_message": str(msg),
        }
    })