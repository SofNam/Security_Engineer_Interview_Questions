# Security Engineer Interview Questions

## Encryption and Authentication

1. What is a three-way handshake?
2. How do cookies work?
3. How do sessions work?
4. Explain how OAuth works.
5. Explain how JWT works.
6. What is a public key infrastructure flow and how would I diagram it?
7. Describe the difference between synchronous and asynchronous encryption.
8. Describe SSL handshake.
9. How does HMAC work?
10. Why HMAC is designed in that way?
11. What is the difference between authentication vs authorization name spaces?
12. What's the difference between Diffie-Hellman and RSA?
13. How does Kerberos work?
14. If you're going to compress and encrypt a file, which do you do first and why?
15. How do I authenticate you and know you sent the message?
16. Should you encrypt all data at rest?
17. What is Perfect Forward Secrecy?

## Network Level and Logging

1. What are common ports involving security, what are the risks and mitigations?
2. Which ports are used for DNS?
3. Describe HTTPs and how it is used.
4. What is the difference between HTTPS and SSL?
5. How does threat modeling work?
6. What is a subnet and how is it useful in security?
7. What is subnet mask?
8. Explain what traceroute is.
9. Draw a network, then expect them to raise an issue and have to figure out where it happened.
10. Write out a Cisco ASA firewall configuration on the white board to allow three networks unfiltered access, 12 networks limited access to different resources on different networks, and 8 networks to be blocked altogether.
11. Explain TCP/IP concepts.
12. What is the OSI model?
13. How does a router differ from a switch?
14. Describe the Risk Management Framework process and a project where you successfully implemented compliance with RMF.
15. How does a packet travel between two hosts connected in same network?
16. Explain the difference between TCP and UDP. Which is more secure and why?
17. What is the TCP three way handshake?
18. What is the difference between IPSEC Phase 1 and Phase 2?
19. What are biggest AWS security vulnerabilities?
20. How do web certificates for HTTPS work?
21. What is the purpose of TLS?
22. Is ARP UDP or TCP?
23. Explain what information is added to a packet at each stop of the 7 layer OSI model.
24. Walk through a whiteboard scenario for your environment of choice (Win/Linux) in which compromising the network is the goal without use of social engineering techniques (phishing for credential harvesting, etc).
25. Explain how you would build a web site that could secure communications between a client and a server and allow an authorized user to read the communications securely.
26. How does an active directory work?
27. Do you know how Single Sign-On works?
28. What is a firewall? How does it work? How does it work in cloud computing?
29. Difference between IPS and IDS?
30. How do you build a tool to protect the entire Apple infra?
31. How do you harden a system?
32. How do you elevate permissions?
33. Describe the hardening measures you've put on your home network.
34. What is traceroute? Explain it in details.
35. How does HTTPS work?
36. What would you do if you discovered an infected host?
37. What is SYN/ACK and how does it work?
38. You got the memory dump of a potentially compromised system, how are you going to approach its analysis?
39. How would you detect a DDOS attack? 
40. How does the kernel know which function to call for the user? 
41. How would you go about reverse-engineering a custom protocol packet?

## OWASP Top 10, Pentesting and Web Applications

1. Differentiate XSS from CSRF.
2. What do you do if a user brings you a pc that is acting 'weird'? You suspect malware.
3. What is the difference between tcp dump and FWmonitor?
4. Do you know what XXE is?
5. Explain man-in-the-middle attacks.
6. What is a Server Side Request Forgery attack?
7. Describe what are egghunters and their use in exploit development. 
8. How is pad lock icon in browser generated?
9. What is Same Origin Policy and CORS?

## Databases

1. How would you secure a Mongo database?
2. How would you secure a Postgres database?
3. Our DB was stolen/exfiltrated. It was secured with one round of sha256 with a static salt. 
   - What do we do now?
   - Are we at risk?
   - What do we change?
4. What are the 6 aggregate functions of SQL?

## Tools and Games

1. Have you played CTF? What was your experience?
2. Would you decrypt a steganography image? 
3. You're given an ip-based phone and asked me to decrypt the message in the phone.
4. What CND tools do you have knowledge or experience with?
5. What is the difference between nmap -ss and nmap -st?
6. How would you filter xyz in Wireshark?
7. Given a sample packet capture - Identify the protocol, the traffic, and the likelihood of malicious intent.
8. If left alone in office with access to a computer, how would you exploit it? 
9. How do you fingerprint an iPhone so you can monitor it even after wiping it?
10. How would you use CI/CD to improve security?
11. You have a pipeline for Docker images. How would you design everything to ensure the proper security checks?
12. How would you create a secret storage system?
13. What technical skill or project are you working on for fun in your free time?
14. How would you harden your work laptop if you needed it at Defcon?
15. If you had to set up supply chain attack prevention, how would you do that?

## Programming and Code

1. Code review a project and look for the vulnerability.
2. How would you conduct a security code review?
3. How can Github webhooks be used in a malicious way?
4. If I hand you a repo of source code to security audit what's the first few things you would do?
5. Can I write a tool that would search our Github repos for secrets, keys, etc.?
6. How would you find secrets in Slack?
7. How would you find AWS keys in code?
8. Given a CVE, walk us through it and how the solution works.
9. Tell me about a repetitive task at work that you automated away.
10. How would you analyze a suspicious email link?

## Compliance
    
1. Can you explain SOC 2?
   - What are the five trust criteria?
2. How is ISO27001 different?
3. Can you list examples of controls these frameworks require?
4. What is the difference between Governance, Risk and Compliance?  
5. What does Zero Trust mean?
6. What is role-based access control (RBAC) and why is it covered by compliance frameworks?
7. What is the NIST framework and why is it influential?
8. What is the OSI model?

## Containers and Cloud Security

1. What security risks are associated with container technologies like Docker?
2. Explain the concept of container escape. How can it be prevented?
3. How would you secure a Kubernetes cluster?
4. What is a pod security policy in Kubernetes and how does it improve security?
5. How do you handle secrets in container environments?
6. What are the security considerations for multi-tenant Kubernetes clusters?
7. Explain the principle of least privilege in the context of container orchestration.
8. What is the difference between Docker image scanning and runtime protection?
9. How would you implement network policies in Kubernetes?
10. What are the security implications of privileged containers?
11. Describe the security controls available in managed Kubernetes services (EKS, GKE, AKS).
12. What is a service mesh and how does it improve security in container environments?
13. How can you prevent container image tampering in your CI/CD pipeline?
14. What are the best practices for securing container registries?
15. How would you detect and respond to a compromise in a containerized environment?
16. What are the security considerations for serverless computing?
17. How do security considerations differ between containers and virtual machines?
18. What is Infrastructure as Code (IaC) and how can you ensure it's secure?
19. What are the common misconfigurations in cloud environments that lead to security breaches?
20. How would you implement a zero-trust architecture in a cloud environment?
21. Explain the shared responsibility model in cloud security.
22. What are the security controls you would implement for data in a multi-cloud environment?
23. How do you handle identity and access management in cloud environments?
24. What is cloud security posture management (CSPM) and why is it important?
25. How would you monitor for suspicious activities in containerized and cloud environments?
