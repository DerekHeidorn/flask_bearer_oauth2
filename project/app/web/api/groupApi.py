import requests
import json
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import abort
from authlib.flask.oauth2 import current_token

from project.app.services import groupService
from project.app.web.utils import serializeUtils
from project.app.web import oauth2
from project.app import main

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


@api.route('/api/v1.0/public/group/<group_uuid>/member/detail/<member_uuid>', methods=['GET'])
@oauth2.require_oauth('CUST_ACCESS')
def get_public_membership_detail_by_uuid(group_uuid, member_uuid):

    # member_uuid is the user_uuid
    membership = groupService.get_group_member_by_uuid(group_uuid, member_uuid)
    print("membership=" + str(membership))

    if membership:

        # print("current_token(type)=" + str(type(current_token)))
        bearer_token = request.headers['Authorization']

        if current_token is not None:
            user_data = _get_external_user_info(member_uuid, bearer_token)
            data = serializeUtils.serialize_membership(membership, user_info=user_data)
        else:
            data = serializeUtils.serialize_membership(membership)

        resp = serializeUtils.generate_response_wrapper(data)
        return jsonify(resp)
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


@api.route('/api/v1.0/public/group/<group_uuid>/manager/detail/<manager_uuid>', methods=['GET'])
@oauth2.require_oauth('CUST_ACCESS')
def get_public_manager_detail_by_uuid(group_uuid, manager_uuid):

    # manager_uuid is the user_uuid
    group_manager = groupService.get_group_manager_by_uuid(group_uuid, manager_uuid)
    print("group_manager=" + str(group_manager))

    if group_manager:

        # print("current_token(type)=" + str(type(current_token)))
        bearer_token = request.headers['Authorization']

        if current_token is not None:
            user_data = _get_external_user_info(manager_uuid, bearer_token)
            data = serializeUtils.serialize_manager(group_manager, user_info=user_data)
        else:
            data = serializeUtils.serialize_manager(group_manager)

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
    group_details = groupService.get_group_detail_by_uuid(group_uuid)
    print("group_details=" + str(group_details))

    if group_details:
        user_uuid_list = []

        for m in group_details.active_members:
            user_uuid_list.append(str(m.person.user_uuid))

        for m in group_details.active_managers:
            user_uuid_list.append(str(m.person.user_uuid))

        print("user_uuid_list=" + str(user_uuid_list))

        # print("current_token(type)=" + str(type(current_token)))
        bearer_token = request.headers['Authorization']

        if current_token is not None:
            user_data = _get_external_user_info_list(user_uuid_list, bearer_token)
            data = serializeUtils.serialize_group_detail(group_details, user_info=user_data)
        else:
            data = serializeUtils.serialize_group_detail(group_details)

        resp = serializeUtils.generate_response_wrapper(data)
        return jsonify(resp)
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def _get_external_user_info(user_uuid, bearer_token):
    user_api_url = None
    if "APP_EXTERNAL_API_USERS" in main.global_config:
        user_api_url = main.global_config["APP_EXTERNAL_API_USERS"]

    if user_api_url is None:
        return None

    # api-endpoint
    url = user_api_url + "/public/user/details/" + user_uuid

    print("bearer_token=" + str(bearer_token))
    print("user_uuid=" + str(user_uuid))

    # sending get request and saving the response as response object
    headers = {"Authorization": bearer_token, "Content-Type": "application/json"}
    resp = requests.get(url=url, headers=headers)

    if resp.status_code == 200:

        print("resp=" + str(resp))

        # extracting data in json format
        user_data = resp.json()
        print("user_data=" + str(user_data))

        return user_data['data']
    else:
        print("resp.status_code=" + str(resp.status_code))
        return None


def _get_external_user_info_list(user_uuid_list, bearer_token):
    user_api_url = None
    if "APP_EXTERNAL_API_USERS" in main.global_config:
        user_api_url = main.global_config["APP_EXTERNAL_API_USERS"]

    if user_api_url is None:
        return None

    # api-endpoint
    url = user_api_url + "/public/user/details"

    print("bearer_token=" + str(bearer_token))
    print("user_uuid_list=" + str(user_uuid_list))

    json_string = json.dumps(user_uuid_list)

    print("json=" + str(json_string))

    # sending get request and saving the response as response object
    headers = {"Authorization": bearer_token, "Content-Type": "application/json"}
    resp = requests.post(url=url, data=json_string, headers=headers)

    if resp.status_code == 200:

        print("resp=" + str(resp))

        # extracting data in json format
        user_data = resp.json()
        print("user_data=" + str(user_data))

        return user_data['data']
    else:
        print("resp.status_code=" + str(resp.status_code))
        return None


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
