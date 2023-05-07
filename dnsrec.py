import dns.resolver

def get_dns_records(domain):
    dns_record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR', 'SOA', 'SRV', 'TXT']
    records = {}

    for record_type in dns_record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [str(answer) for answer in answers]
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.NXDOMAIN:
            print(f"{domain} does not exist.")
            break
        except Exception as e:
            print(f"Error while retrieving {record_type} record for {domain}: {e}")

    return records

# Example usage of the function
domain_names = ["handshake", "openai.com"]
for domain in domain_names:
    dns_records = get_dns_records(domain)
    print(f"DNS records for {domain}:")
    print(dns_records)
