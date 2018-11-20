
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import abort

from project.app.services import groupService
from project.app.web.utils import serializeUtils
from project.app.web import oauth2

api = Blueprint('group_api', __name__)


@api.route('/api/v1.0/public/group', methods=['GET'])
@oauth2.require_oauth('CUST_ACCESS')
def get_public_groups():
    groups = groupService.get_groups()
    group_list = []
    for g in groups:
        group_list.append(serializeUtils.serialize_group(g))

    resp = serializeUtils.generate_response_wrapper(group_list)
    return jsonify(resp)


@api.route('/api/v1.0/admin/group', methods=['GET'])
@oauth2.require_oauth('STAFF_ACCESS')
def get_groups():
    groups = groupService.get_groups()
    group_list = []
    for g in groups:
        group_list.append(serializeUtils.serialize_group(g))

    resp = serializeUtils.generate_response_wrapper(group_list)
    return jsonify(resp)


@api.route('/api/v1.0/public/group/<group_uuid>', methods=['GET'])
@oauth2.require_oauth('CUST_ACCESS')
def get_public_group_by_uuid(group_uuid):
    current_group = groupService.get_group_by_uuid(group_uuid)
    if current_group:
        data = serializeUtils.serialize_group(current_group)
        resp = serializeUtils.generate_response_wrapper(data)
        return jsonify(resp)
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


@api.route('/api/v1.0/public/group/detail/<group_uuid>', methods=['GET'])
@oauth2.require_oauth('CUST_ACCESS')
def get_public_group_detail_by_uuid(group_uuid):
    group_detail = groupService.get_group_detail_by_uuid(group_uuid)
    if group_detail:
        data = serializeUtils.serialize_group_detail(group_detail)
        resp = serializeUtils.generate_response_wrapper(data)
        return jsonify(resp)
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


@api.route('/api/v1.0/admin/group/<group_uuid>', methods=['GET'])
@oauth2.require_oauth('STAFF_ACCESS')
def get_group_by_uuid(group_uuid):
    current_group = groupService.get_group_by_uuid(group_uuid)
    if current_group:
        data = serializeUtils.serialize_group(current_group)
        resp = serializeUtils.generate_response_wrapper(data)
        return jsonify(resp)
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


@api.route('/api/v1.0/admin/group', methods=['POST'])
@oauth2.require_oauth('STAFF_ACCESS')
def add_public_group():
    group_name = request.form["group_name"]

    new_group = groupService.add_group(group_name)

    data = serializeUtils.serialize_group(new_group)
    resp = serializeUtils.generate_response_wrapper(data)
    return jsonify(resp), 201
