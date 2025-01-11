# Soonchain-checker

# Soonchain Airdrop Checker

This project is an asynchronous script for checking wallet eligibility in the Soonchain airdrop. It reads wallet addresses and proxies from external files, sends requests to the Soonchain API, and returns the airdrop status for each wallet.

## Features
- Checks wallet eligibility for airdrop through an API.
- Uses proxies for each request.
- Asynchronous request handling for speed optimization.
- Outputs results for each wallet (eligible or not).
- Counts the total number of tokens received by wallets.

---

## Requirements

### System Requirements
- Python 3.12 or higher

### External Libraries
Before running, install the following dependencies:
```bash
pip install aiohttp
```

### Input Files
1. **`wallet_addresses.txt`**
   - Contains a list of wallet addresses (one per line).
2. **`proxies.txt`**
   - Contains a list of proxies in the format `ip:port` (one per line).

> **Note:** The number of wallets and proxies must match.

---

## Code Structure

### Key Variables
- `ssl_check` — flag to disable SSL verification.

### Main Functions
1. `read_file(file_name)`
   - Reads data from a file and removes extra characters.
   
2. `fetch_data(wallet_address, proxy)`
   - Sends a request to the Soonchain API to check airdrop status.
   - Uses a proxy and processes the JSON response.
   
3. `main()`
   - Creates tasks to check wallets and runs them asynchronously.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone <URL>
   cd <repository>
   ```

2. Prepare input files:
   - Create `wallet_addresses.txt` with a list of wallet addresses.
   - Create `proxies.txt` with a list of proxies.

3. Run the script:
   ```bash
   python main.py
   ```

4. View the results in the console:
   - Status for each wallet (eligible or not).
   - Overall statistics (number of successful/unsuccessful checks, total tokens received).

---

## Example Output
```
      -- Soonchain Airdrop checker --

0xABC123... | Airdrop: 💎 1000
0xDEF456... | Airdrop: 🚫
0xGHI789... | Error | 504 Gateway Timeout

Eligible: 1 | Not eligible: 1 | Summary: 1000 tokens
```

---

## Issues and Solutions

1. **Error: "The number of wallets and proxies must be the same!"**
   - Ensure the number of wallets and proxies in the respective files matches.

2. **Proxy or connection issues**
   - Verify the proxy format (`ip:port`).
   - Add authentication to proxies if needed (e.g., `http://user:password@ip:port`).

3. **Request timeout**
   - Increase the `timeout` value in `aiohttp.ClientTimeout`.

