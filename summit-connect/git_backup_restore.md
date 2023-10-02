# Git Backup and Restore

The playbooks described are intended to establish a process for backing up networking configurations and defining a workflow to automatically restore from a specified backup.

## Process Diagram

![Process Diagram](/.attachments/GitBackupAndRestore.png)

## Playbooks

| Name | Description |
| --- | --- |
| [Backup](./playbooks/network_backup.yml) | Clones a git repository to the execution node, gathers facts from network devices target in the play via `{{ _hosts }}` variable, and writes a YAML config for each device using the Ansible for Networking data model. Configuration file is configured and pushed to remote repository with a tag representing the time it was taken. |
| [Apply Config](./playbooks/network_apply_config.yml) | Accepts a network configuration object and applies it to each target device specified via `{{ _hosts }}` variable per resource included. A stat is set for downstream workflow nodes which contains a before/after diff for each configuration change. |
| [Restore](./playbooks/network_restore.yml) | Given a `{{ backup_config_tag }}`, this playbook will pull a restore point from the remote repository and apply the configs per device specified via `{{ _hosts }}`. If a YAML config does not exist with the naming standard `{{ inventory_hostname }}.config.yml` then it will be skipped. |
| [Slack Notification](./playbooks/slack_notification.yml) | Using the stat set from [Apply Config](./playbooks/network_apply_config.yml), this playbook will loop over each devices before/after diff and post a notification to a pre-configured Slack channel. If not used via a workflow, the playbook will expect a `{{ workflow_config_reports }}` variable containing the diffs. |

## Execution Environment

The execution environment used contains various collections for integrating with networking devices, git, and Ansible Automation Platform. Refer to the EE definition in my [execution environments repository](https://github.com/zjleblanc/ansible-execution-environments/blob/master/ee-networking/execution-environment.yml).

## Workflow

This repo contains configuration as code for the workflow and job templates which can be reference in the [setup playbook](./setup.yml). There are supporting credentials needed which I won't cover in this document, but include a `Personal Slack Token` and `Git Role Credential` for integration with those services. Below is a screenshot of the resulting workflow:

![Workflow Screenshot](/.attachments/git_backup_restore_workflow.png)