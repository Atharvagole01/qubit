import requests

url = "https://linkedin-bulk-data-scraper.p.rapidapi.com/companies"

payload = {
    "links": [
        "http://www.linkedin.com/company/aep-energy",
        "http://www.linkedin.com/company/johnson-&-johnson",
        "http://www.linkedin.com/company/ametek",
        "http://www.linkedin.com/company/insurance-commission-of-the-bahamas",
        "http://www.linkedin.com/company/chs",
        "http://www.linkedin.com/company/vitas-healthcare",
        "http://www.linkedin.com/company/citgo",
        "http://www.linkedin.com/company/mars",
        "http://www.linkedin.com/company/suffolk-construction",
        "http://www.linkedin.com/company/sumitomo-mitsui-banking-corporation",
        "http://www.linkedin.com/company/nemours",
        "http://www.linkedin.com/company/tvars",
        "http://www.linkedin.com/company/farmers-new-world-life",
        "http://www.linkedin.com/company/cincinnatichildrens",
        "http://www.linkedin.com/company/thecpso",
        "http://www.linkedin.com/company/jefferson-county-public-schools",
        "http://www.linkedin.com/company/university-of-illinois-at-urbana-champaign",
        "http://www.linkedin.com/company/s&c-electric-company",
        "http://www.linkedin.com/company/fayette-county-public-schools-ky",
        "http://www.linkedin.com/company/booz-allen-hamilton",
        "http://www.linkedin.com/company/elon-university",
        "http://www.linkedin.com/company/the-walt-disney-company",
        "http://www.linkedin.com/company/texas-tech-university",
        "http://www.linkedin.com/company/merck",
        "http://www.linkedin.com/company/everwise-cu",
        "http://www.linkedin.com/company/peabody-trust",
        "http://www.linkedin.com/company/wsfs-bank",
        "http://www.linkedin.com/company/saia-inc",
        "http://www.linkedin.com/company/the-coca-cola-company",
        "http://www.linkedin.com/company/tcenergy",
        "http://www.linkedin.com/company/the-trust-company-of-tennessee",
        "http://www.linkedin.com/company/stowers-institute-for-medical-research",
        "http://www.linkedin.com/company/dick's-sporting-goods",
        "http://www.linkedin.com/company/southwest-airlines",
        "http://www.linkedin.com/company/neighborsfcu",
        "http://www.linkedin.com/company/arevon",
        "http://www.linkedin.com/company/r-d-offutt-company",
        "http://www.linkedin.com/company/camden-property-trust",
        "http://www.linkedin.com/company/autozone",
        "http://www.linkedin.com/company/fraser-health-authority",
        "http://www.linkedin.com/company/ga-asi",
        "http://www.linkedin.com/company/the-walt-disney-company",
        "http://www.linkedin.com/company/miter-brands",
        "http://www.linkedin.com/company/bartonmalow",
        "http://www.linkedin.com/company/msa-the-safety-company",
        "http://www.linkedin.com/company/oklahoma-state-school-boards-association",
        "http://www.linkedin.com/company/fayette-county-public-schools-ky",
        "http://www.linkedin.com/company/bankers-financial-corporation",
        "http://www.linkedin.com/company/mobile-county-public-school-system",
        "http://www.linkedin.com/company/multi-health-systems-inc--mhs",
        "http://www.linkedin.com/company/turning-point-of-central-california-inc.",
        "http://www.linkedin.com/company/american-residential-services",
        "http://www.linkedin.com/company/nationwide",
        "http://www.linkedin.com/company/genmab",
        "http://www.linkedin.com/company/crayon-group",
        "http://www.linkedin.com/company/crowe",
        "http://www.linkedin.com/company/chevron",
        "http://www.linkedin.com/company/jefferson-county-public-schools",
        "http://www.linkedin.com/company/nationwide",
        "http://www.linkedin.com/company/1915south-ashley-south-east",
        "http://www.linkedin.com/company/newyorklife",
        "http://www.linkedin.com/company/dream-motor-group",
        "http://www.linkedin.com/company/honda",
        "http://www.linkedin.com/company/jd-irving",
        "http://www.linkedin.com/company/harvard-university",
        "http://www.linkedin.com/company/shockwave-medical",
        "http://www.linkedin.com/company/alabama-department-of-transportation",
        "http://www.linkedin.com/company/goodwill-keystone-area",
        "http://www.linkedin.com/company/national-basketball-association",
        "http://www.linkedin.com/company/lodiusd",
        "http://www.linkedin.com/company/nymta",
        "http://www.linkedin.com/company/national-association-of-chain-drug-stores-nacds-",
        "http://www.linkedin.com/company/ford-motor-company",
        "http://www.linkedin.com/company/clark-county-credit-union",
        "http://www.linkedin.com/company/caterpillar-inc",
        "http://www.linkedin.com/company/kennedyjenks-consultants",
        "http://www.linkedin.com/company/chadwellsupply",
        "http://www.linkedin.com/company/agtexas-farm-credit",
        "http://www.linkedin.com/company/fidelity-investments",
        "http://www.linkedin.com/company/scotiabank",
        "http://www.linkedin.com/company/georgia-system-operations-corporation",
        "http://www.linkedin.com/company/aaa-life-insurance-company",
        "http://www.linkedin.com/company/missouri-employers-mutual",
        "http://www.linkedin.com/company/kennesaw-state-university",
        "http://www.linkedin.com/company/fayette-county-public-schools-ky",
        "http://www.linkedin.com/company/lockheed-martin",
        "http://www.linkedin.com/company/redwood-living",
        "http://www.linkedin.com/company/playhousesquare",
        "http://www.linkedin.com/company/french-brothers-homes",
        "http://www.linkedin.com/company/big-bear-vacations-cabins",
        "http://www.linkedin.com/company/georgia-system-operations-corporation",
        "http://www.linkedin.com/company/aaa-life-insurance-company",
        "http://www.linkedin.com/company/missouri-employers-mutual",
        "http://www.linkedin.com/company/kennesaw-state-university",
        "http://www.linkedin.com/company/fayette-county-public-schools-ky",
        "http://www.linkedin.com/company/lockheed-martin",
        "http://www.linkedin.com/company/redwood-living",
        "http://www.linkedin.com/company/playhousesquare",
        "http://www.linkedin.com/company/french-brothers-homes",
        "http://www.linkedin.com/company/big-bear-vacations-cabins",
    ]
}
headers = {
    "x-rapidapi-key": "e6545e8a19msh298ac820737d44ep179512jsn4a3dca1da8fa",
    "x-rapidapi-host": "linkedin-bulk-data-scraper.p.rapidapi.com",
    "Content-Type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

