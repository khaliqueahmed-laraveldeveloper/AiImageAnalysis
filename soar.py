import redis
from google import genai
import json

# 1. Setup Connections
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

client = genai.Client(api_key="API_KEY_HERE")
def analyze_incident(log_entry):
    """The Brain: Uses AI to decide if this is a threat."""
    prompt = f"""
    Analyze this log entry for security threats: {log_entry}.
    Return JSON only: {{"verdict": "threat" or "safe", "reason": "why"}} without use of this ```json rapping 

    """
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=prompt
    )
    cleaned_text = response.text.replace('```json', '').replace('```', '').strip()
    return json.loads(cleaned_text)

def orchestrate_response(verdict_data, ip):
    """The Hands: Takes action based on the AI's decision."""
    if verdict_data['verdict'] == 'threat':
        print(f"[!] Threat Detected: {verdict_data['reason']}")
        print(f"[+] Blocking IP: {ip} in Redis.")
        # ACTION: Block the IP in Redis
        # r.sadd('blacklist', ip)
        # print(f"[+] IP {ip} successfully blacklisted in Redis.")
    else:
        print(f"[+] Incident identified as: {verdict_data['reason']}. No action taken.")

# 2. Main Execution Loop
def run_soar():
    print("SOAR Engine Active. Watching logs...")
    # Simulate a log incoming
    log = "Failed password attempt from IP 192.168.1.50"
    ip = "192.168.1.50"
    
    # Process
    decision = analyze_incident(log)
    orchestrate_response(decision, ip)

if __name__ == "__main__":
    run_soar()