CONSTANTS_IN_UPPERCASE = 123

variables_are_lowercase = 'OH YES!'


def methods_are_lowercase_too():
    pass


def all_use_kebap_case():
    pass


# uses supplied credentials to create new sftp client
def sftp_client(username, password):
    pass


def create_sftp_client(username, password):
    pass


current_instances = []


def add_instance():
    pass


# scale out if less than 3 instances
if len(current_instances) < 3:
    add_instance()


# scale out if less than 3 instances
def should_scale_out(current_instances):
    pass


if should_scale_out(current_instances):
    add_instance()
