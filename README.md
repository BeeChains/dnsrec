# dnsrec
get dns records for your domains, 'A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR', 'SOA', 'SRV', 'TXT'

# Introduction
This script defines a function get_dns_records that takes a domain name as input and returns a dictionary containing its DNS records. The example usage of the function demonstrates how to use it with a list of domain names.

Please note that you may encounter issues with rate limiting or blocking when making too many DNS requests in a short amount of time. If this happens, consider adding a delay between requests or using a different DNS resolver by specifying the resolver parameter in the dns.resolver.resolve() function.

## This script uses dnspython. 
'dnspython' is a powerful and widely-used DNS toolkit for Python. It is a library that provides a complete implementation of the DNS (Domain Name System) protocol. The library allows developers to perform DNS queries, zone transfers, dynamic updates, and DNSSEC validation. It is compatible with both Python 2 and Python 3.

With dnspython, you can perform various DNS-related tasks, such as querying for different types of DNS records (A, AAAA, MX, NS, CNAME, etc.), reverse DNS lookups (finding domain names for IP addresses), DNS zone transfers, and more.

# Installation
1. To install dnspython;
   ```
   pip install dnspython
   ```
2. install git repo or save the python code in dnsrec.py to a file.
   ```
   git clone https://github.com/BeeChains/dnsrec.git
   ```
3. edit the domains to retreive dns records for in the code that looks like this;
   ```
   # Example usage of the function
   domain_names = ["handshake", "openai"]
   ```
4. Run the python script
   ```
   python dnsrec.py
   ```
You can find more information and examples on how to use dnspython in the official documentation: http://www.dnspython.org/
