import requests
import json
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import abort
from authlib.flask.oauth2 import current_token

from app.services import groupService
from app.services.utils import sha256
from app.web.utils import serializeUtils, apiUtils
from app.web import oauth2
from app import core
from app.web.schemas.groupSchemas import GroupSchema, MembershipSchema


api = Blueprint('group_api', __name__)


@api.route('/api/v1.0/my/groups', methods=['GET'])
@oauth2.require_oauth('GRP_ACCESS')
def get_my_public_groups():
    if current_token is not None and current_token.user_uuid is not None:

        user_uuid = current_token.user_uuid

        groups = groupService.get_groups_by_user_uuid(user_uuid)
        group_list = []
        for g in groups:
            group_list.append(GroupSchema().dump(g))

        resp = apiUtils.generate_response_wrapper(group_list)
        return jsonify(resp)
    abort(403)


@api.route('/api/v1.0/my/subscribe/group/<group_uuid>/<group_digest>', methods=['post'])
@oauth2.require_oauth('GRP_ACCESS')
def subscribe_to_group(group_uuid, group_digest):

    if current_token is not None and current_token.user_uuid is not None:
        user_uuid = current_token.user_uuid

        digest_to_compare = sha256.hexdigest(group_uuid)

        if digest_to_compare == group_digest:
            group_membership = groupService.add_group_membership(group_uuid, user_uuid)
            data = MembershipSchema().dump(group_membership)

            resp = apiUtils.generate_response_wrapper(data)
            resp = apiUtils.add_global_success_msg(resp, "You have been added to the group")
            return jsonify(resp), 201
        else:
            abort(403)
    else:
        abort(403)


@api.route('/api/v1.0/my/unsubscribe/group/<group_uuid>/<group_digest>', methods=['post'])
@oauth2.require_oauth('GRP_ACCESS')
def unsubscribe_to_group(group_uuid, group_digest):

    if current_token is not None and current_token.user_uuid is not None:
        user_uuid = current_token.user_uuid

        digest_to_compare = sha256.hexdigest(group_uuid)

        if digest_to_compare == group_digest:
            group_membership = groupService.remove_group_membership(group_uuid, user_uuid)
            data = MembershipSchema().dump(group_membership)

            resp = apiUtils.generate_response_wrapper(data)
            resp = apiUtils.add_global_success_msg(resp, "You have been removed from the group")
            return jsonify(resp), 201
        else:
            abort(403)
    else:
        abort(403)


@api.route('/api/v1.0/public/group', methods=['GET'])
@oauth2.require_oauth('GRP_ACCESS')
def get_public_groups():
    groups = groupService.get_public_groups()
    group_list = []
    for g in groups:
        group_list.append(GroupSchema().dump(g))

    resp = apiUtils.generate_response_wrapper(group_list)
    return jsonify(resp)


@api.route('/api/v1.0/admin/group', methods=['GET'])
@oauth2.require_oauth('GRP_ADMIN')
def get_groups():
    groups = groupService.get_groups()
    group_list = []
    for g in groups:
        group_list.append(GroupSchema().dump(g))

    resp = apiUtils.generate_response_wrapper(group_list)
    return jsonify(resp)


@api.route('/api/v1.0/public/group/<group_uuid>', methods=['GET'])
@oauth2.require_oauth('GRP_ACCESS')
def get_public_group_by_uuid(group_uuid):
    group = groupService.get_group_by_uuid(group_uuid, False)
    if group:
        data = GroupSchema().dump(group)
        resp = apiUtils.generate_response_wrapper(data)
        return jsonify(resp)
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


@api.route('/api/v1.0/public/group/<group_uuid>/member/detail/<member_uuid>', methods=['GET'])
@oauth2.require_oauth('GRP_ACCESS')
def get_public_membership_detail_by_uuid(group_uuid, member_uuid):

    # member_uuid is the user_uuid
    membership = groupService.get_group_member_by_uuid(group_uuid, member_uuid)
    core.logger.debug("membership=" + str(membership))

    if membership:

        # print("current_token(type)=" + str(type(current_token)))
        bearer_token = request.headers['Authorization']

        if current_token is not None:
            user_data = _get_external_user_info(member_uuid, bearer_token)
            data = serializeUtils.serialize_membership(membership, user_info=user_data)
        else:
            data = serializeUtils.serialize_membership(membership)

        resp = apiUtils.generate_response_wrapper(data)
        return jsonify(resp)
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


@api.route('/api/v1.0/public/group/<group_uuid>/manager/detail/<manager_uuid>', methods=['GET'])
@oauth2.require_oauth('GRP_ACCESS')
def get_public_manager_detail_by_uuid(group_uuid, manager_uuid):

    # manager_uuid is the user_uuid
    group_manager = groupService.get_group_manager_by_uuid(group_uuid, manager_uuid)
    core.logger.debug("group_manager=" + str(group_manager))

    if group_manager:

        # print("current_token(type)=" + str(type(current_token)))
        bearer_token = request.headers['Authorization']

        if current_token is not None:
            user_data = _get_external_user_info(manager_uuid, bearer_token)
            data = serializeUtils.serialize_manager(group_manager, user_info=user_data)
        else:
            data = serializeUtils.serialize_manager(group_manager)

        resp = apiUtils.generate_response_wrapper(data)
        return jsonify(resp)
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


@api.route('/api/v1.0/public/group/detail/<group_uuid>', methods=['GET'])
@oauth2.require_oauth('GRP_ACCESS')
def get_public_group_detail_by_uuid(group_uuid):
    group_details = groupService.get_group_detail_by_uuid(group_uuid, False)
    core.logger.debug("group_details=" + str(group_details))

    if group_details:
        user_uuid_list = []

        for m in group_details.active_members:
            user_uuid_list.append(str(m.person.user_uuid))

        for m in group_details.active_managers:
            user_uuid_list.append(str(m.person.user_uuid))

            core.logger.debug("user_uuid_list=" + str(user_uuid_list))

        # print("current_token(type)=" + str(type(current_token)))
        bearer_token = request.headers['Authorization']

        if current_token is not None:
            user_data = _get_external_user_info_list(user_uuid_list, bearer_token)
            data = serializeUtils.serialize_group_detail(group_details, user_info=user_data)
        else:
            data = serializeUtils.serialize_group_detail(group_details)

        resp = apiUtils.generate_response_wrapper(data)
        return jsonify(resp)
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def _get_external_user_info(user_uuid, bearer_token):
    user_api_url = None
    if "APP_EXTERNAL_API_USERS" in core.global_config:
        user_api_url = core.global_config["APP_EXTERNAL_API_USERS"]

    if user_api_url is None:
        return None

    # api-endpoint
    url = user_api_url + "/public/user/profile/" + user_uuid

    core.logger.debug("bearer_token=" + str(bearer_token))
    core.logger.debug("user_uuid=" + str(user_uuid))

    # sending get request and saving the response as response object
    headers = {"Authorization": bearer_token, "Content-Type": "application/json"}
    resp = requests.get(url=url, headers=headers)

    if resp.status_code == 200:

        core.logger.debug("resp=" + str(resp))

        # extracting data in json format
        user_data = resp.json()
        core.logger.debug("user_data=" + str(user_data))

        return user_data['data']
    else:
        core.logger.debug("resp.status_code=" + str(resp.status_code))
        return None


def _get_external_user_info_list(user_uuid_list, bearer_token):
    user_api_url = None
    if "APP_EXTERNAL_API_USERS" in core.global_config:
        user_api_url = core.global_config["APP_EXTERNAL_API_USERS"]

    if user_api_url is None:
        return None

    # api-endpoint
    url = user_api_url + "/public/user/profiles"

    core.logger.debug("bearer_token=" + str(bearer_token))
    core.logger.debug("user_uuid_list=" + str(user_uuid_list))

    json_string = json.dumps(user_uuid_list)

    core.logger.debug("json=" + str(json_string))

    # sending get request and saving the response as response object
    headers = {"Authorization": bearer_token, "Content-Type": "application/json"}
    resp = requests.post(url=url, data=json_string, headers=headers)

    if resp.status_code == 200:

        core.logger.debug("resp=" + str(resp))

        # extracting data in json format
        user_data = resp.json()
        core.logger.debug("user_data=" + str(user_data))

        return user_data['data']
    else:
        core.logger.debug("resp.status_code=" + str(resp.status_code))
        return None


@api.route('/api/v1.0/admin/group/<group_uuid>', methods=['GET'])
@oauth2.require_oauth('GRP_ADMIN')
def get_group_by_uuid(group_uuid):
    current_group = groupService.get_group_by_uuid(group_uuid)
    if current_group:
        data = GroupSchema().dump(current_group)
        resp = apiUtils.generate_response_wrapper(data)
        return jsonify(resp)
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


@api.route('/api/v1.0/admin/group', methods=['POST'])
@oauth2.require_oauth('GRP_ADMIN')
def add_public_group():
    group_name = request.form["group_name"]
    group_de = request.form["group_de"]

    new_group = groupService.add_group(group_name, group_de)

    data = GroupSchema().dump(new_group)
    resp = apiUtils.generate_response_wrapper(data)
    resp = apiUtils.add_global_success_msg(resp, "New group has been added")
    return jsonify(resp), 201
