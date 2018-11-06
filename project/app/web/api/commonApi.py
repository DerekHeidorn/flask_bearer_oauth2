
from flask import Blueprint
from flask import jsonify

from project.app.services import commonService

api = Blueprint('common_api', __name__)

@api.route('/api/v1.0/public/app/version', methods=['GET'])
def getAppVersion():
    version = commonService.getConfigByKey("app.release_number")

    return jsonify({"application.version": version})




