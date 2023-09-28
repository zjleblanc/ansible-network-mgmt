git
=========

Ansible git operations

Minimum Ansible Version: 2.9

Galaxy Tags: \[ tools git scm \]

Required Variables
------------------

| Name | Example |
| -------- | ------- |
| git_url | <repo> |


Role Variables
--------------

| Variable | Type | Value or Expression |
| -------- | ------- | ------------------- |
| git_key | default |  |
| git_branch | default | master |
| git_msg | default | update files with ansible |
| git_tag | default | |
| git_remove_local | default | False |
| git_username | default | ansible_git |
| git_email | default | ansible_git@ansible.com |

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

  ```yaml
    - hosts: servers
      tasks:
        - name: Execute git role
          ansible.builtin.include_role:
            name: git
          vars:
            git_url: <repo>
  ```

License
-------

GPL-3.0-only

Author Information
-------
**Will Tome**
