import pytest
from unittest import mock
from werkzeug.datastructures import FileStorage

from src.application_layer.use_cases.process_file import PaymentUseCase


@pytest.fixture()
def create_file():
    return FileStorage(filename='Test file')

def test_health(app):
    result = app.get("/api/health")

    assert result.json == {"service": "API Kanastra HealthCheck", "version": "1.0"}
    
@mock.patch.object(PaymentUseCase, 'create_payments')
def test_post_process_file(mock_create_payment, create_file, app):
        
    response = app.post("/api/process-file", data={"file":create_file})
    
    assert response.status == '201 CREATED'
    assert response.json == {"message": f"Payments created successfully"}
    mock_create_payment.assert_called_once()
    
@mock.patch('src.presentation_layer.views.api.logger.exception')
@mock.patch.object(PaymentUseCase, 'create_payments')
def test_post_process_file_status_500(mock_create_payment, mock_logger, create_file, app):
    msg = 'Failed to create process'
    mock_create_payment.side_effect = Exception(msg)
    
    response = app.post("/api/process-file", data={"file":create_file})
    
    assert response.status == '500 INTERNAL SERVER ERROR'
    assert response.json == {"message": "Error on create payment"}
    mock_logger.assert_called_once_with(
        "Failed to create process",
        extra={
            "props": {
                "request": "/api/process-file",
                "method": "POST",
                "file": create_file.filename,
                "error_message": str(msg),
            }
        }
    )

