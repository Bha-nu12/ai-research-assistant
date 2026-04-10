# Deployment Guide

## Local Development

### Quick Start
```bash
# 1. Setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# 2. Configure
cp .env.example .env
# Edit .env with your API keys

# 3. Run
streamlit run app.py
```

Access at: http://localhost:8501

---

## Streamlit Cloud (Recommended for Beginners)

### Prerequisites
- GitHub account
- Repository with code (without `.env`)
- API keys ready

### Deployment Steps

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Select your GitHub repository
   - Select branch and file (`app.py`)
   - Click "Deploy"

3. **Add Secrets**
   - Go to app settings (gear icon)
   - Click "Secrets"
   - Add your API keys:
     ```
     GEMINI_API_KEY = "your-gemini-key"
     PINECONE_API_KEY = "your-pinecone-key"
     COHERE_API_KEY = "your-cohere-key"
     LLM_PROVIDER = "gemini"
     EMBEDDING_PROVIDER = "gemini"
     ```
   - Click "Save"

4. **App will redeploy automatically**

### Advantages
- Free tier available
- Automatic updates from GitHub
- Built-in secret management
- No server management

### Limitations
- Limited to Streamlit apps
- Resource constraints on free tier
- Requires GitHub repository

---

## Docker Deployment

### Prerequisites
- Docker installed
- Docker Hub account (optional)

### Setup

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.11-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 8501

   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Create docker-compose.yml**
   ```yaml
   version: '3.8'
   services:
     rag-assistant:
       build: .
       ports:
         - "8501:8501"
       environment:
         GEMINI_API_KEY: ${GEMINI_API_KEY}
         PINECONE_API_KEY: ${PINECONE_API_KEY}
         COHERE_API_KEY: ${COHERE_API_KEY}
         LLM_PROVIDER: gemini
         EMBEDDING_PROVIDER: gemini
       volumes:
         - ./data:/app/data
   ```

3. **Build and Run**
   ```bash
   # Build image
   docker build -t rag-assistant .

   # Run with environment variables
   docker run -p 8501:8501 \
     -e GEMINI_API_KEY="your-key" \
     -e PINECONE_API_KEY="your-key" \
     -e COHERE_API_KEY="your-key" \
     rag-assistant

   # Or with docker-compose
   export GEMINI_API_KEY="your-key"
   export PINECONE_API_KEY="your-key"
   export COHERE_API_KEY="your-key"
   docker-compose up
   ```

### Push to Docker Hub
```bash
# Login
docker login

# Tag image
docker tag rag-assistant your-username/rag-assistant:latest

# Push
docker push your-username/rag-assistant:latest
```

---

## AWS Deployment

### Option 1: AWS App Runner (Easiest)

1. **Push Docker image to ECR**
   ```bash
   # Create ECR repository
   aws ecr create-repository --repository-name rag-assistant

   # Build and push
   docker build -t rag-assistant .
   docker tag rag-assistant:latest <account-id>.dkr.ecr.<region>.amazonaws.com/rag-assistant:latest
   docker push <account-id>.dkr.ecr.<region>.amazonaws.com/rag-assistant:latest
   ```

2. **Create App Runner service**
   - Go to AWS App Runner console
   - Click "Create service"
   - Select ECR image
   - Configure environment variables
   - Set port to 8501
   - Deploy

3. **Add environment variables**
   - In App Runner service settings
   - Add GEMINI_API_KEY, PINECONE_API_KEY, COHERE_API_KEY

### Option 2: AWS Lambda + API Gateway

1. **Create Lambda function**
   - Runtime: Python 3.11
   - Handler: app.handler

2. **Add environment variables**
   - Configuration → Environment variables
   - Add API keys

3. **Deploy with Streamlit**
   ```bash
   pip install streamlit-serverless
   streamlit-serverless deploy
   ```

### Option 3: EC2 Instance

1. **Launch EC2 instance**
   - Ubuntu 22.04 LTS
   - t3.medium or larger
   - Security group: Allow port 8501

2. **SSH into instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Setup application**
   ```bash
   # Install Python
   sudo apt update
   sudo apt install python3-pip python3-venv

   # Clone repository
   git clone your-repo-url
   cd PROJECT_28_RAG_ASSISTANT

   # Setup
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   # Create .env
   nano .env
   # Add your API keys

   # Run with systemd
   sudo nano /etc/systemd/system/rag-assistant.service
   ```

4. **Systemd service file**
   ```ini
   [Unit]
   Description=RAG Research Assistant
   After=network.target

   [Service]
   Type=simple
   User=ubuntu
   WorkingDirectory=/home/ubuntu/PROJECT_28_RAG_ASSISTANT
   Environment="PATH=/home/ubuntu/PROJECT_28_RAG_ASSISTANT/venv/bin"
   ExecStart=/home/ubuntu/PROJECT_28_RAG_ASSISTANT/venv/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

5. **Start service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable rag-assistant
   sudo systemctl start rag-assistant
   ```

---

## Google Cloud Run

### Prerequisites
- Google Cloud account
- gcloud CLI installed

### Deployment

1. **Create Dockerfile** (see Docker section)

2. **Build and push to Container Registry**
   ```bash
   gcloud builds submit --tag gcr.io/your-project/rag-assistant
   ```

3. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy rag-assistant \
     --image gcr.io/your-project/rag-assistant \
     --platform managed \
     --region us-central1 \
     --port 8501 \
     --set-env-vars GEMINI_API_KEY=your-key,PINECONE_API_KEY=your-key,COHERE_API_KEY=your-key
   ```

4. **Access your app**
   - URL provided in deployment output
   - Format: `https://rag-assistant-xxxxx.run.app`

---

## Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed

### Deployment

1. **Create Procfile**
   ```
   web: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
   ```

2. **Create .streamlit/config.toml**
   ```toml
   [server]
   headless = true
   port = $PORT
   enableXsrfProtection = false
   ```

3. **Deploy**
   ```bash
   # Login
   heroku login

   # Create app
   heroku create your-app-name

   # Set environment variables
   heroku config:set GEMINI_API_KEY=your-key
   heroku config:set PINECONE_API_KEY=your-key
   heroku config:set COHERE_API_KEY=your-key

   # Deploy
   git push heroku main
   ```

4. **View logs**
   ```bash
   heroku logs --tail
   ```

---

## Comparison Table

| Platform | Cost | Ease | Scalability | Best For |
|----------|------|------|-------------|----------|
| Local | Free | ⭐⭐⭐⭐⭐ | N/A | Development |
| Streamlit Cloud | Free/Paid | ⭐⭐⭐⭐⭐ | Low | Quick deployment |
| Docker | Free | ⭐⭐⭐⭐ | High | Flexibility |
| AWS App Runner | Paid | ⭐⭐⭐⭐ | High | Production |
| Google Cloud Run | Paid | ⭐⭐⭐⭐ | High | Production |
| Heroku | Paid | ⭐⭐⭐⭐ | Medium | Quick deployment |
| EC2 | Paid | ⭐⭐⭐ | High | Full control |

---

## Production Checklist

- [ ] Code pushed to GitHub (without `.env`)
- [ ] `.gitignore` includes `.env`
- [ ] API keys stored in platform secrets
- [ ] Environment variables configured
- [ ] Application tested locally
- [ ] Logging configured (no API keys logged)
- [ ] Error handling in place
- [ ] Monitoring/alerts set up
- [ ] Backup strategy for data
- [ ] SSL/HTTPS enabled
- [ ] Rate limiting configured
- [ ] Documentation updated

---

## Monitoring & Maintenance

### Health Checks
```bash
# Check if app is running
curl http://localhost:8501

# Check logs
docker logs container-id  # Docker
heroku logs --tail        # Heroku
```

### Scaling
- **Streamlit Cloud**: Automatic
- **Docker**: Use container orchestration (Kubernetes)
- **AWS**: Use load balancers
- **Google Cloud Run**: Automatic scaling

### Updates
```bash
# Update dependencies
pip install -r requirements.txt --upgrade

# Rebuild Docker image
docker build -t rag-assistant .

# Redeploy
git push  # For Streamlit Cloud
docker push  # For Docker Hub
```

---

## Troubleshooting Deployment

### App won't start
- Check logs for errors
- Verify all dependencies installed
- Check environment variables set
- Verify API keys are valid

### Port already in use
- Change port in deployment config
- Kill existing process
- Check firewall rules

### API key errors
- Verify keys in platform secrets
- Check environment variable names match
- Regenerate keys if needed
- Restart application

### Performance issues
- Check resource allocation
- Monitor API usage
- Optimize chunk size
- Reduce batch size
