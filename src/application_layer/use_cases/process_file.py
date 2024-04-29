
import csv
import os
import pandas as pd
from src.app import db
from flask import current_app
from werkzeug.datastructures import FileStorage

from src.domain_layer.models.payment import Payment
from src.presentation_layer.mapping import ProcessFileMapping

class PaymentUseCase:
    
    @classmethod
    def create_payments(cls, file: FileStorage):
        
        file.save(os.path.join(current_app.config['FILE_UPLOADS'],file.filename))
        filepath = os.path.join(current_app.config['FILE_UPLOADS'], file.filename)

        uploaded_df = pd.read_csv(filepath, encoding='unicode_escape')
        uploaded_df.to_sql('payments', db.get_engine(), index=True, index_label='id', if_exists="replace")

                
