# PanOS Demo

This demo contains the Ansible content required to deploy and configure a Palo Alto (Virtual) Firewall in AWS and provision two EC2 instances serving as a bastion host and web server. The resulting network makes it possible to demonstrate use of the [paloaltonetworks.panos](https://galaxy.ansible.com/paloaltonetworks/panos) ansible collection.

## Tested Collection Versions

| Collection | Version |
| --- | --- |
| amazon.aws | 8.2.1 |
| paloaltonetworks.panos | 2.21.2 |
| servicenow.itsm | 2.4.0 |

## Pre-requisites

In order to use these playbooks, you must have an AWS account with sufficient permissions to deploy the resources used in this demo. Additionally, the playbooks will integrate with ServiceNow ITSM if credentials are supplied. The following environment variables are expected for the playbooks to integrate with AWS and ServiceNow (optional):

| Environment Variable | Example |
| --- | --- |
| AWS_ACCESS_KEY | `AKIA...` |
| AWS_SECRET_KEY | `kasdjf938...` |
| AWS_REGION | `us-east-2` |
| SN_HOST | `https://<instance>.service-now.com` |
| SN_USERNAME | `demo-user` |
| SN_PASSWORD | `$ervicen0w` |

If you are familiar with other authentication methods for the [amazon.aws](https://galaxy.ansible.com/ui/repo/published/amazon/aws) and [servicenow.itsm](https://galaxy.ansible.com/ui/repo/published/servicenow/itsm) collections, then those should work as well if configured correctly.

### Local Setup - Python Virtual Environment

I recommend using python virtual environments for local Ansible development with `ansible-playbook` or a custom execution environment for use with `ansible-navigator`. Below is how I would setup a python virtual environment - I am covering this option as it is quicker to get started (imo):

Create a python virtual environment:
`python -m venv <venv-name>`

```bash
# Edit your <venv-name>/bin/activate script 

deactivate () {
    ...

    unset SN_HOST
    unset SN_USERNAME
    unset SN_PASSWORD

    unset AWS_ACCESS_KEY
    unset AWS_SECRET_KEY
    unset AWS_REGION
}
...

export SN_HOST="https://<instance>.service-now.com"
export SN_USERNAME="<username>"
export SN_PASSWORD="<password>"

export AWS_ACCESS_KEY="<access_key>"
export AWS_SECRET_KEY="<secret_key>"
export AWS_REGION="us-east-2"

...
```

**IMPORTANT**: Add the virtual environment to your .gitignore to ensure these files are not checked into version control. This is best practice for any repository using python virtual environments.

### Local Setup - No Virtual Environment

Run the following commands in your terminal
```bash
export SN_HOST="https://<instance>.service-now.com"
export SN_USERNAME="<username>"
export SN_PASSWORD="<password>"

export AWS_ACCESS_KEY="<access_key>"
export AWS_SECRET_KEY="<secret_key>"
export AWS_REGION="us-east-2"
```

To clear out the environment, be sure to run the corresponding `unset` commands when you are finished.

## Infrastructure Setup

Specify the panos firewall admin via one of two options:

1. Using an extra variable at the command line and commenting out the vars_file entry for `panos_secrets.yml`<br>`ansible-playbook pb_infra_setup.yml -e panos_demo_password="$3cr3t"`
2. Delete and create your own vaulted `panos_secrets.yml` file with the **panos_demo_password** defined. I will not be sharing my vault password :D Assuming you are in the playbook directory,<br>`ansible-vault create vars/panos_secrets.yml`<br>`ansible-playbook pb_infra_setup.yml`

## Firewall Configuration

Once the infrastructure is stood up, you can run the firewall configuration playbook against the virtual Palo Alto Firewall in AWS. 

This playbook depends on a vaulted secrets file to supply the **panos_provider** for module authentication. Add to a vaulted secrets file the following structure:
```
# vars/panos_secrets.yml
---
panos_demo_password: $ecr3t # same password used in Infrastructure Setup
panos_provider:
  ip_address: "{{ panos_fw_mgmt_ip_address }}" # You can find this in the AWS console
  username: admin
  password: "{{ panos_demo_password }}"
```

## Webserver Setup

This one's a bit trickier - we must use the bastion host as an SSH Proxy - docs to come...

## Infrastructure Tear Down

Run the `pb_infra_teardown.yml` playbook.<br>The **panos_demo_password** is not required for this step as we are simply blowing away the AWS resources.

## Integrating with ServiceNow

Docs to come...