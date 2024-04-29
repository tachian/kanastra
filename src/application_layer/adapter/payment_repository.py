import logging
from datetime import datetime
from src.app import db
from src.application_layer.persistency.tables import payment_table

logger = logging.getLogger("kanastra." + __name__)

class SQLAlchemyPaymentRepository():

    @classmethod
    def get_by_debtDueDate(cls, debtDueDate: datetime):
        from src.domain_layer.models.payment import Payment
        try:
            logger.info(
                "Getting payments",
                extra={
                    "props": {
                        "service": "SQLite",
                        "service method": "get_by_debtDueDate",
                        "date": str(debtDueDate),
                    }
                })

            payments = db.session.query(payment_table).filter(
                payment_table.c.debtDueDate == debtDueDate).all()

            if payments:
                return [Payment(
                    name=p.name, 
                    governmentId=p.governmentId,
                    email=p.email,
                    debtAmount=p.debtAmount,
                    debtDueDate=p.debtDueDate,
                    debtID=p.debtID) for p in payments]
            else:
                return 

        except Exception as e:
            logger.exception(
                "Error while trying to get payments",
                extra={
                    "props": {
                        "service": "SQLite",
                        "service method": "get_by_debtDueDate",
                        "error_message": str(e)
                    }
                })
            raise e

