import logging
import json
import sys
import os


def setupLogger():
	""" properly sets up the logger depending on if the code is running
		on a cloud function or locally

		Args:
		Returns:
	"""
	function_identity = os.environ.get('FUNCTION_IDENTITY', 'local')
	root = logging.getLogger()
	root.setLevel(logging.INFO)
	root.info("function_identity: {}".format(function_identity))
	if function_identity == 'local':

		logging.StreamHandler(sys.stdout)

def get_project_id():
	""" Gets the project ID. It defaults to the project declared in the
		enviorment variable PROJECT but if it can't find it there it will
		try looking for a service account and take the project ID from there

		Args:
		Returns:
	"""
	service_acc_address = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', None)
	if service_acc_address:
		service_acc = open(service_acc_address, 'r').read()
		service_acc_project_id = json.loads(service_acc)['project_id']
	else:
		service_acc_project_id = None
	project_id = os.environ.get('PROJECT', service_acc_project_id)

	if service_acc_project_id != None and project_id != service_acc_project_id:
		logging.critical("Warning the project in ENV VAR PROJECT is \
			not the same as your service account project")

	return project_id

if __name__ == '__main__':
	setupLogger()
