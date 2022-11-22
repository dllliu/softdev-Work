Collected Knowledge & Wisdom on
# API_NAME_HERE
- Stripe API

## Provides:
- This API provides an API for taking card payments. 
- This includes: checking balance, charge actions (update, capture, list), track payments from the same customer, dispute, set payouts, give refunds...

### Pain factor: _
2

### Key Provisioning:     

- Only make calls with the key using HTTPS
- Test mode secret keys have the prefix sk_test_ and live mode secret keys have the prefix sk_live_
- Provide your API key as the basic auth username value. You do not need to provide a password.

### Quotas:
- For most APIs, Stripe allows up to 100 read operations per second and 100 write operations per second in live mode, and 25 operations per second for each in test mode.

- For the Files API, Stripe allows up to 20 read operations per second and 20 write operations per second in both live mode and test mode. Live mode and test mode limits are separate.

- For the Search API, Stripe allows up to 20 read operations per second which applies for all search endpoints in both live mode and test mode. Live mode and test mode limits are separate.

## The Good:
- Test Mode to experiment with API calls, which doesn't affect your live data or interact with the banking networks. 
## The Bad:
- Does not support bulk updates. Only one obhject per request
## The Ugly:
- ...


**Location:** https://stripe.com/docs/api

---

Accurate as of (last update):    2021-11-22

Contributors:

the two spaces after each name are important!  
Daniel Liu, pd2   
