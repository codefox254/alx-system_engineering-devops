
Postmortem: Ediary Outage
Issue Summary:

Duration of the Outage: May 15, 2024, 14:00 - 18:30 UTC
Impact: The Ediary web application experienced a complete outage, preventing users from accessing their accounts, diary entries, to-do lists, and meeting schedules. Approximately 90% of users were affected.
Root Cause: The outage was caused by a misconfiguration in the deployment script, which led to a failure in the database connection across all server instances.
Timeline:

14:00: Issue detected via automated monitoring alerts indicating a sudden spike in server errors.
14:05: On-call engineer begins investigating the issue, noticing the database connection errors.
14:15: Initial assumption is that the database server is down. Database team is notified.
14:25: Database team reports that the database server is operational and shows no signs of failure.
14:40: Investigation shifts to the application servers and network configurations.
15:00: Misleading debugging path pursued, assuming network issues between app servers and database.
15:30: Network team confirms there are no network issues.
16:00: Escalation to the DevOps team to review the deployment process.
16:30: Deployment script reviewed, revealing a recent update that altered the database connection string format.
17:00: Root cause identified as a misconfiguration in the deployment script.
17:30: Deployment script corrected, and the new configuration is tested.
18:00: Corrected deployment rolled out to all servers.
18:30: Service fully restored, and users are able to access Ediary again.
Root Cause and Resolution:

Root Cause: The deployment script had recently been updated to streamline the deployment process. However, this update included an incorrect database connection string format, which was not detected during testing. This misconfiguration caused all application servers to fail to establish a connection to the database, resulting in a total service outage.
Resolution: The DevOps team corrected the deployment script by reverting the connection string format to the correct version. After rigorous testing in a staging environment to ensure the configuration was correct, the updated deployment script was rolled out to the production servers, restoring database connectivity and normal application functionality.
Corrective and Preventative Measures:

Improvements:
Implement additional checks and validation steps in the deployment script to ensure configurations are correct before deployment.
Enhance automated testing to cover deployment configurations and connection strings.
Increase the robustness of monitoring tools to detect similar configuration issues faster.
Tasks:
Update Deployment Script: Patch the deployment script to include validation for database connection strings.
Add Monitoring: Implement monitoring for deployment script changes and database connection errors.
Automated Testing: Expand automated tests to include deployment configuration verification.
Review Process: Introduce a mandatory peer review process for any changes to deployment scripts.
Documentation: Update the deployment documentation to include steps for verifying connection strings and configurations.
By addressing these issues, we aim to prevent similar outages in the future and ensure a more reliable service for all Ediary users.
