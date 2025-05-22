# What is a three-way handshake?

The three-way handshake is a process used by TCP (Transmission Control Protocol) to establish a connection between a client and server. This process ensures that both parties are ready to communicate and agree on initial sequence numbers for the connection.

## Steps in the Three-Way Handshake

1. **SYN (Synchronize)**: 
   - The client sends a SYN packet to the server
   - This packet contains an initial sequence number (ISN)
   - The client enters the SYN-SENT state

2. **SYN-ACK (Synchronize-Acknowledge)**:
   - The server receives the SYN packet and responds with a SYN-ACK packet
   - This packet acknowledges the client's sequence number (ACK = client's ISN + 1)
   - The server also includes its own initial sequence number
   - The server enters the SYN-RECEIVED state

3. **ACK (Acknowledge)**:
   - The client receives the SYN-ACK packet and sends an ACK packet
   - This packet acknowledges the server's sequence number (ACK = server's ISN + 1)
   - The client enters the ESTABLISHED state
   - When the server receives this ACK, it also enters the ESTABLISHED state

At this point, the TCP connection is established, and data transfer can begin.

## Security Implications

The three-way handshake is significant from a security perspective because:

1. **SYN Flood Attacks**: Attackers can send numerous SYN packets without completing the handshake, exhausting server resources (mitigated with SYN cookies)

2. **TCP Sequence Prediction Attacks**: If an attacker can predict sequence numbers, they can potentially hijack sessions

3. **Connection State Tracking**: Firewalls use the three-way handshake to track connection states and enforce security policies

4. **TCP Reset Attacks**: Understanding the handshake helps in recognizing when RST (reset) packets are legitimately or maliciously injected

## Interview Tips

When answering this question in an interview:
- Clearly explain all three steps of the handshake
- Mention the state transitions (SYN-SENT, SYN-RECEIVED, ESTABLISHED)
- Highlight security implications, especially SYN flood attacks
- Explain how this relates to stateful firewalls and connection tracking 