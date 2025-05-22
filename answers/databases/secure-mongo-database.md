# How would you secure a MongoDB database?

Securing a MongoDB database involves multiple layers of protection. Here's a comprehensive approach:

## Authentication and Authorization

1. **Enable Authentication**: 
   - Always run MongoDB with `--auth` mode enabled
   - Create dedicated users with specific roles instead of using the default accounts
   - Use strong, unique passwords for all database users

2. **Role-Based Access Control (RBAC)**:
   - Implement the principle of least privilege
   - Create custom roles with specific permissions
   - Assign users only the permissions they need for their specific tasks
   - Regularly audit user roles and permissions

## Network Security

1. **Bind to Localhost**:
   - Configure MongoDB to bind only to localhost (127.0.0.1) when possible
   - Use the `bindIp` configuration setting

2. **Firewall Rules**:
   - Restrict access to MongoDB ports (default: 27017)
   - Allow connections only from application servers
   - Block all unnecessary external access

3. **TLS/SSL Encryption**:
   - Enable TLS/SSL for all MongoDB connections
   - Use proper certificate validation
   - Configure with `net.ssl.mode: requireSSL`

4. **VPC/Private Network**:
   - Run MongoDB in a private subnet or VPC
   - Use VPN or SSH tunneling for administrative access

## Configuration Security

1. **Disable Server-Side JavaScript**:
   - Set `security.javascriptEnabled: false` to prevent NoSQL injection attacks

2. **Auditing**:
   - Enable MongoDB's audit logging
   - Configure with `auditLog.destination` and related settings
   - Monitor for suspicious activities

3. **Regular Updates**:
   - Apply security patches promptly
   - Subscribe to MongoDB security announcements
   - Plan regular maintenance windows for updates

## Data Protection

1. **Encryption**:
   - Implement Encryption at Rest (with MongoDB Enterprise or community tools)
   - Use encrypted storage for backups
   - Consider field-level encryption for sensitive data

2. **Secure Backups**:
   - Implement regular backup procedures
   - Encrypt backup data
   - Test restoration processes regularly
   - Store backups securely off-site

## Additional Measures

1. **Security Scanning**:
   - Regularly scan for MongoDB instances with default configurations
   - Use tools like Shodan to identify exposed databases
   - Run vulnerability scanners against your MongoDB environment

2. **Monitoring and Alerting**:
   - Set up monitoring for unauthorized access attempts
   - Create alerts for unusual query patterns or high resource usage
   - Implement a security information and event management (SIEM) solution

3. **Documentation**:
   - Maintain clear documentation of all security measures
   - Create incident response plans for potential breaches

## Cloud-Specific Considerations (MongoDB Atlas)

If using MongoDB Atlas:
- Use IP whitelisting for access control
- Implement VPC peering when possible
- Enable Advanced Threat Detection
- Use Cloud Provider security features (AWS Security Groups, etc.)

## Regular Security Assessments

- Conduct periodic security assessments
- Consider penetration testing by qualified professionals
- Review security posture after major configuration changes 