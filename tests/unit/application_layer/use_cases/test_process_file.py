import os
from flask import current_app
from unittest import mock
from werkzeug.datastructures import FileStorage
from pandas.core.frame import DataFrame

from src.app import db
from src.application_layer.use_cases.process_file import PaymentUseCase



@mock.patch('src.application_layer.use_cases.process_file.pd.DataFrame.to_sql')
@mock.patch('src.application_layer.use_cases.process_file.pd.read_csv')
@mock.patch('src.application_layer.use_cases.process_file.FileStorage.save')
def test_create_payments(mock_save, mock_csv_read, mock_to_sql, app):
    
    fileStorage = FileStorage(filename='Test file')
    mock_csv_read.return_value = DataFrame()
    
    PaymentUseCase.create_payments(file=fileStorage)
    
    mock_save.assert_called_once_with(os.path.join(current_app.config['FILE_UPLOADS'],fileStorage.filename))
    mock_csv_read.assert_called_once_with(os.path.join(current_app.config['FILE_UPLOADS'],fileStorage.filename), encoding='unicode_escape')
    mock_to_sql.assert_called_once_with('payments', db.get_engine(), index=True, index_label='id', if_exists="replace")
