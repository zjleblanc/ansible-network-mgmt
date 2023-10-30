mgmt.snow_configuration.records
=========

Wrap the Service Now Table API module to be "idempotent".

Galaxy Tags: \[ service_now table records \]

Required Variables
------------------

| Name | Example | Description |
| -------- | ------- | ------------------- |
| snow_records | `[{ ... }]` | A list of Service Now records to insert |

Example Playbook
---------------- 

  ```yaml
    - hosts: localhost
      tasks:
        - name: Execute records role
          ansible.builtin.include_role:
            name: mgmt.snow_configuration.records
          vars:
            snow_records:
              - type: oauth_entity_scope
                data:
                  name: Ansible Controller Write
                  oauth_entity: "{{ snow_records_out['oauth_entity'][0].sys_id }}"
                  oauth_entity_scope: write
  ```

License
-------

license (GPL-2.0-or-later, MIT, etc)

Author Information
-------
**Zachary LeBlanc**
