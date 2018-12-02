
from flask import Blueprint
from flask import jsonify
from flask import abort
from cacheout import Cache

from app.models.codetables.group import CtGroupTypes
from app.services import codetablesService
from app.web.schemas.generalSchemas import CodeTableSchema

api = Blueprint('codetables_api', __name__)

allowable_codetable_map = {"CtGroupTypes": CtGroupTypes}
_codetable_cache = Cache(maxsize=200, ttl=5 * 60)


@api.route('/api/v1.0/admin/codetables/<codetable_name>', methods=['GET'])
def codetable_by_name(codetable_name):

    allowed_codetable = allowable_codetable_map.get(codetable_name)

    if allowed_codetable is not None:
        # Check cache
        cached_codetable = _codetable_cache.get(codetable_name)

        if cached_codetable is not None:
            return jsonify(cached_codetable)

        else:
            codetable_data = codetablesService.get_code_table(allowed_codetable)
            data = CodeTableSchema().dump(codetable_data, many=True)
            if data:
                _codetable_cache.add(codetable_name, data)
                return jsonify(data)

    abort(404)
