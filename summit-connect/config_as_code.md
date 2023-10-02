# Configuration as Code

There is one playbook in this repository for applying configuration as code to devices in your inventory. Much of the orchestration lives in a GitHub workflow definition which react to pull requests and launch job templates in Ansible Automation Platform. That definition file lives in my [ansible-network-configs](https://github.com/zjleblanc/ansible-network-configs/blob/master/.github/workflows/network_cac_pr.yml) repository. This repository contains the playbook which is run when a job template is launched.

## Playbook

| Name | Description |
| --- | --- |
| [Config as Code](./playbooks/network_apply_cac.yml) | Clones the git configuration repository (master version) and loads the configuration file per host specified in the `{{ _hosts }}` variable. If a configuration file does not exist for a specified host, then it will be logged and skipped. |

## E2E Process

![Process Diagram](/.attachments/NetworkCaC.png)

When a pull request is merged to the master branch of [ansible-network-configs](https://github.com/zjleblanc/ansible-network-configs), a workflow is launched automatically. The first part of the workflow detects changes to configuration files and will launch the config-as-code playbook, passing a comma-delimited lists of hosts via the `{{ _hosts }}` variable with changes to be applied. Below is an example of a successful workflow execution:

### GitHub Workflow Run
![Workflow Execution Result](/.attachments/github_action_result.png)

### AAP Job Run
![Config as Code Job](/.attachments/cac_jt_run.png)