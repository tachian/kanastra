from flask_restx import fields, Model

process_file_model = Model(
    'file', {
    'filename': fields.String
    })

