import logging

logger = logging.getLogger("kanastra." + __name__)

class SlipServices:
    
    @classmethod
    def send_slip_email(cls, payments: list):
        
        for payment in payments:
            logger.info(f'Creating slip for payment {payment.debtID}',
                        extra={
                            "service": "Slip",
                            "service method": "send_slip_email",
                        })
            # TODO: Implementar geração de boleto - PyBoleto
            
            logger.info(f'Sending slip of payment {payment.debtID} to email {payment.email}',
                        extra={
                            "service": "Slip",
                            "service method": "send_slip_email",
                        })
            
        return
            
            
            
            