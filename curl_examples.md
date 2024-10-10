
# curl Examples

1. **Basic GET request**:
   - `curl http://example.com` – Fetch a webpage.

2. **Fetching a resource and saving to file**:
   - `curl -o filename http://example.com/file` – Download a file.

3. **Sending data with POST**:
   - `curl -X POST -d "param=value" http://example.com/api` – Send a POST request with data.

4. **Working with headers**:
   - `curl -H "Authorization: Bearer TOKEN" http://example.com/protected` – Pass headers (common in API requests).

5. **Verbose mode**:
   - `curl -v http://example.com` – Get detailed information about the request and response.
