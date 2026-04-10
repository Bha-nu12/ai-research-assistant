# Security Best Practices Guide

## API Key Management

### ⚠️ Critical Security Rules

1. **NEVER commit `.env` to version control**
   - Use `.gitignore` to prevent accidental commits
   - Always use `.env.example` as template

2. **NEVER hardcode API keys in source code**
   - Always load from environment variables
   - Use `.env` file for local development

3. **NEVER share API keys in messages, emails, or chat**
   - Treat them like passwords
   - Regenerate immediately if exposed

4. **NEVER use the same key for development and production**
   - Create separate keys for each environment
   - Rotate keys regularly

### Setup Instructions

#### Step 1: Create Local .env File
```bash
# Copy template
cp .env.example .env

# Edit .env with YOUR actual API keys
# This file is in .gitignore and won't be committed
```

#### Step 2: Verify .gitignore
```bash
# Check .env is in .gitignore
cat .gitignore | grep "^\.env"

# Should output: .env
```

#### Step 3: Verify .env is Not Tracked
```bash
# If .env was previously committed, remove it
git rm --cached .env

# Verify it's removed from tracking
git status
```

## Getting API Keys

### Google Gemini API

1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key
4. Add to `.env`:
   ```
   GEMINI_API_KEY=your-key-here
   ```

**Key Rotation:**
- Regenerate at https://makersuite.google.com/app/apikey
- Update `.env` with new key
- Old key becomes invalid immediately

### Pinecone API Key

1. Go to https://app.pinecone.io
2. Click "API Keys" in sidebar
3. Click "Create API Key"
4. Copy the key
5. Add to `.env`:
   ```
   PINECONE_API_KEY=your-key-here
   PINECONE_ENVIRONMENT=us-east-1
   ```

**Key Rotation:**
- Go to API Keys section
- Delete old key
- Create new key
- Update `.env`

### Cohere API Key

1. Go to https://dashboard.cohere.com
2. Click "API Keys" in sidebar
3. Click "Generate API Key"
4. Copy the key
5. Add to `.env`:
   ```
   COHERE_API_KEY=your-key-here
   ```

**Key Rotation:**
- Go to API Keys section
- Delete old key
- Generate new key
- Update `.env`

## Environment-Specific Configuration

### Development Environment
```bash
# .env (local, not committed)
GEMINI_API_KEY=dev-key-xxx
PINECONE_API_KEY=dev-key-yyy
COHERE_API_KEY=dev-key-zzz
LLM_PROVIDER=gemini
EMBEDDING_PROVIDER=gemini
```

### Production Environment
Use environment variables set by your hosting platform:
- **Streamlit Cloud**: Settings → Secrets
- **Docker**: Environment variables in docker-compose.yml
- **AWS Lambda**: Environment variables in function config
- **Heroku**: Config Vars in app settings

## Secure Deployment

### Streamlit Cloud Deployment

1. Push code to GitHub (without `.env`)
2. Go to https://share.streamlit.io
3. Click "New app"
4. Select your repository
5. Go to app settings → Secrets
6. Add your API keys:
   ```
   GEMINI_API_KEY = "your-key"
   PINECONE_API_KEY = "your-key"
   COHERE_API_KEY = "your-key"
   ```

### Docker Deployment

Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8501:8501"
    environment:
      GEMINI_API_KEY: ${GEMINI_API_KEY}
      PINECONE_API_KEY: ${PINECONE_API_KEY}
      COHERE_API_KEY: ${COHERE_API_KEY}
      LLM_PROVIDER: gemini
      EMBEDDING_PROVIDER: gemini
```

Run with:
```bash
export GEMINI_API_KEY="your-key"
export PINECONE_API_KEY="your-key"
export COHERE_API_KEY="your-key"
docker-compose up
```

### AWS Lambda Deployment

1. Create Lambda function
2. Go to Configuration → Environment variables
3. Add your API keys
4. Deploy code without `.env`

## Monitoring & Auditing

### Check for Exposed Keys

```bash
# Search for exposed keys in git history
git log -p | grep -i "api_key\|password\|secret"

# Search in current files
grep -r "AIzaSy\|pcsk_\|" . --exclude-dir=.git

# Use git-secrets tool
git secrets --scan
```

### API Usage Monitoring

**Gemini:**
- Monitor at https://console.cloud.google.com/apis/dashboard
- Set up billing alerts

**Pinecone:**
- Monitor at https://app.pinecone.io/usage
- Check index statistics

**Cohere:**
- Monitor at https://dashboard.cohere.com/usage
- Check API call logs

## If Keys Are Compromised

### Immediate Actions

1. **Regenerate all keys immediately**
   - Gemini: https://makersuite.google.com/app/apikey
   - Pinecone: https://app.pinecone.io/api-keys
   - Cohere: https://dashboard.cohere.com/api-keys

2. **Update `.env` with new keys**
   ```bash
   # Edit .env
   nano .env  # or your editor
   ```

3. **Restart application**
   ```bash
   # Kill existing process
   Ctrl+C

   # Restart
   streamlit run app.py
   ```

4. **Check for unauthorized usage**
   - Review API usage logs
   - Check billing for unexpected charges
   - Monitor Pinecone index for unauthorized access

5. **If deployed, update secrets**
   - Streamlit Cloud: Update in Secrets
   - Docker: Rebuild with new keys
   - AWS: Update environment variables

### Prevention

- Use `.gitignore` to prevent commits
- Use `.env.example` for templates
- Rotate keys regularly (monthly recommended)
- Use different keys for dev/prod
- Monitor API usage regularly
- Enable API key restrictions if available

## Code Security

### Safe API Key Usage

✅ **Good:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not set")
```

❌ **Bad:**
```python
# Never do this!
api_key = "AIzaSyA0MYCd3UcEtLrLrYXD9TVLmACtnByXpsE"
```

### Logging Security

✅ **Good:**
```python
print(f"Using API provider: {provider}")
```

❌ **Bad:**
```python
# Never log API keys!
print(f"API Key: {api_key}")
```

## Checklist

- [ ] `.env` file created from `.env.example`
- [ ] `.env` is in `.gitignore`
- [ ] All API keys added to `.env`
- [ ] `.env` is NOT committed to git
- [ ] Application loads keys from environment
- [ ] No hardcoded keys in source code
- [ ] `.env.example` has placeholder values only
- [ ] Keys rotated if ever exposed
- [ ] Different keys for dev/prod
- [ ] API usage monitored regularly

## Additional Resources

- **Git Secrets**: https://github.com/awslabs/git-secrets
- **OWASP Secrets Management**: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- **12 Factor App**: https://12factor.net/config
- **Streamlit Secrets**: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management

## Support

If you suspect your keys have been compromised:
1. Regenerate keys immediately
2. Check API usage logs
3. Monitor for unauthorized charges
4. Contact API provider support if needed
