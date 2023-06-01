from Members.utils import add_member



def check_send_proposal_rool(data):
	if data.get('scrum'):
		data.get('instance').team.filter(
			user=data.get('user')).get(role='Project owner')


def check_user_in_project(data):
	if data.get('project').team.filter(user=data['user']).exists():
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