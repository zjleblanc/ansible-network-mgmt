# ansible network mgmt

This repo contains examples using ansible to manage network devices and perform network automation tasks.

## playbooks

| Name | Description | Docs |
| --- | --- | :---: |
| Compliance Report | basic network compliance report with specific checks | [📝](./playbooks/compliance-report.md) |
| Interactive Report (Mock) | interactive report with searching, filtering, and more... | [📝](./playbooks/interactive_report.md) |
| Interactive Report (Live) | interactive report with searching, filtering, and more... | [📝](./playbooks/interactive_report_live.md) |
| Comprehensive CSV Report | csv with all gathered facts | [📝](./playbooks/comprehensive-csv-report.md) |
| Dynatrace SNMP -> ServiceNow CMDB | Combining Ansible with Dynatrace SNMP, you can quickly implement automation to populate your CMDB with network infrastructure components | [📝](./playbooks/dynatrace_snow_cmdb.md) |

## troubleshooting

| Error | Resolution | 
| --- | --- |
| Paramiko ssh key invalid | set environment var<br>`ANSIBLE_PARAMIKO_LOOK_FOR_KEYS=False` |
| Authentication failed | configure login local on ios devices<br>`username <user> priv 15 password <pass>`<br>`line vty 0 4`<br>`login local` |