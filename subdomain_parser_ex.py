import tldextract

def extract_levels(url):
    ext = tldextract.extract(url)
    return ext.subdomain, ext.domain, ext.suffix

url = "https://google.google.com"
subdomain, domain, suffix = extract_levels(url)
print("Subdomain:", subdomain)
print("Domain:", domain)
print("Suffix:", suffix)
