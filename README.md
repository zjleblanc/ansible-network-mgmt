# ansible network mgmt

This repo contains examples using ansible to manage network devices and perform network automation tasks.

## playbooks

| Name | Description | Docs |
| --- | --- | :---: |
| Compliance Report | basic network compliance report with specific checks | [📝](./playbooks/compliance-report.md) |
| Interactive Report | interactive report with searching, filtering, and more... | [📝](./playbooks/interactive-report.md) |
| Comprehensive CSV Report | csv with all gathered facts | [📝](./playbooks/comprehensive-csv-report.md) |

## troubleshooting

| Error | Resolution | 
| --- | --- |
| Paramiko ssh key invalid | set environment var<br>`ANSIBLE_PARAMIKO_LOOK_FOR_KEYS=False` |
| Authentication failed | configure login local on ios devices<br>`username <user> priv 15 password <pass>`<br>`line vty 0 4`<br>`login local` |