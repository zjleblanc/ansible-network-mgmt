# Using Dynatrace SNMP to Populate ServiceNow CMDB via Ansible

Combining Ansible with Dynatrace SNMP, you can quickly implement automation to populate your CMDB with network infrastructure components. In this example, we use a simple DQL (Dynatrace Query Language) expression to pull data from the Dynatrace API and create ServiceNow CMDB records. The implementation consists of a single Ansible playbook with < 10 tasks.

## Main Playbook

The initial playbook [(found here)](./dynatrace_snow_cmdb.yml) contains the following steps:

1. Get data from Dynatrace API (the demo loads static data from a file for simplicity)
1. Loop over Cisco records and insert into ServiceNow CMDB
1. Repeat step (2) for Custom devices and Palo Alto devices
1. Extract any new locations discovered in the device payloads and create Location entries in ServiceNow

## Dynatrace API Tasks

The Dynatrace API tasks file [(found here)](./tasks/dynatrace_snmp.yml) contains the following steps needed pull data directly from Dynatrace using DQL:

1. Obtain an OAuth token using client credentials stored in ENV variables
1. Use the OAuth token to get a request token
1. Use the request token to execute a DQL query and register the data in an Ansible var for ServiceNow record creation
