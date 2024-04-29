import logging
from datetime import datetime
from flask import Blueprint, request
from flask_restx import Api, Resource
from json import loads

from src.presentation_layer.mapping import ProcessFileMapping
from src.application_layer.use_cases.process_file import PaymentUseCase
from src.presentation_layer.schemas import process_file_model

logger = logging.getLogger("bhub." + __name__)

VERSION = "1.0"
DOC = "API Bhub Index"

bp_index = Blueprint("api", __name__, url_prefix="/api")

api = Api(
    bp_index,
    version=VERSION,
    title="API Kanastra Index",
    description=DOC,
    doc=False,
)

ns = api.namespace("", description="API Kanastra Index")
api.models[process_file_model.name] = process_file_model

@ns.route("/health", doc=False)
class Index(Resource):
    def get(self):
        return dict(service="API Kanastra HealthCheck", version=VERSION)
    
@ns.route("/process-file")
class Create(Resource):
    @ns.response(200, 'OK')
    def post(self):

        file = request.files.get('file')
        
        try:

            PaymentUseCase.create_payments(file=file)
            
            return {"message": "Payments created successfully"}, 201
        except Exception as e:

            logger.exception(
                "Failed to create process",
                extra={
                    "props": {
                        "request": "/api/process-file",
                        "method": "POST",
                        "file": file.filename,
                        "error_message": str(e),
                    }
                },
            )
            return {'message': 'Error on create payment'}, 500 
    