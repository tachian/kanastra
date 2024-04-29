from datetime import datetime, timedelta
from unittest import mock
from src.application_layer.use_cases.jobs import JobsUseCase
from src.domain_layer.models.payment import Payment


@mock.patch.object(Payment, 'send_slips')
@mock.patch.object(Payment, 'get_by_debtDueDate')
def test_send_slips(mock_get_by_debtDueDate, mock_send_slips):
    
    payments =  list[Payment]
    mock_get_by_debtDueDate.return_value = payments
    
    JobsUseCase.send_slips()
    search_date = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=10)
    mock_get_by_debtDueDate.assert_called_once_with(debtDueDate=search_date)
    mock_send_slips.assert_called_once_with(payments=payments)
