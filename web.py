import requests
import random
import time

# Define the list of target URLs
target_urls = [
    "https://www.microsoft.com/en-in?wt.mc_id=studentamb_363034",
    "https://account.microsoft.com/account/manage-my-account?wt.mc_id=studentamb_363034",
    "https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/?wt.mc_id=studentamb_363034",
    "https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/?wt.mc_id=studentamb_363034",
    "https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/?wt.mc_id=studentamb_363034",
    "https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/?wt.mc_id=studentamb_363034",
    "https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/?wt.mc_id=studentamb_363034",
    "https://learn.microsoft.com/en-us/training/modules/introduction-to-github-copilot/?wt.mc_id=studentamb_363034",
    "https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/?wt.mc_id=studentamb_363034",
    "https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/?wt.mc_id=studentamb_363034",
]

# Number of unique visitors to simulate
num_visitors = 255

# Function to generate a random IP address within a specified range
def generate_random_ip():
    return "42.107.{}.{}".format(random.randint(179, 183), random.randint(0, 255))

# Generate a list of unique IP addresses
unique_ips = set()
while len(unique_ips) < num_visitors:
    unique_ips.add(generate_random_ip())

# Generate random user agents for variety
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/82.0.4227.42",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Vivaldi/6.0.2284.46",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Whale/5.0.79.7",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 PTST/99",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 2345Explorer/10.0.15.300",
]


# Function to simulate a unique visitor with a random IP address, user agent, and target URL
def send_unique_visitor():
    ip_address = unique_ips.pop()
    user_agent = random.choice(user_agents)
    target_url = random.choice(target_urls)
    headers = {"User-Agent": user_agent, "X-Forwarded-For": ip_address}
    try:
        response = requests.get(target_url, headers=headers)
        if response.status_code == 200:
            print("Successfully visited:", target_url, "from IP:", ip_address)
        else:
            print("Failed to visit:", target_url, "from IP:", ip_address, "Status code:", response.status_code)
    except Exception as e:
        print("Error visiting:", target_url, "from IP:", ip_address, "Error:", str(e))

# Simulate unique visitors
for i in range(num_visitors):
    print("Sending unique visitor", i+1)
    send_unique_visitor()
    # Add longer delay between requests (e.g., 1 to 5 seconds) to simulate realistic behavior
    time.sleep(random.uniform(10, 30))
