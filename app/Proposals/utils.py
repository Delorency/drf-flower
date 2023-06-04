from Members.utils import add_member
from utils import check_user_in_project as u_check_user_in_project



def check_user_in_project(data):
	if u_check_user_in_project(data):
		raise ValueError
	return None


def check_received_proposal(data):
	if data.get('scrum'):
		if data.get('user').user_proposals.filter(
			scrum_project=data.get('project')).exists():
			raise ValueError
	return None


def check_rool_to_accept(data):
	if data.get('instance').user != data.get('user'):
		raise ValueError


def perfrom_add_member(data):
	return add_member(data)