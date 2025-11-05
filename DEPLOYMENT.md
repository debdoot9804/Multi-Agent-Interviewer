# Deployment Guide - AI Interviewer

## 🚀 Deploying to Streamlit Cloud

### Prerequisites
- GitHub account
- Azure OpenAI account with API access
- Your code pushed to a GitHub repository

### Step-by-Step Deployment

1. **Push Your Code to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy New App**
   - Click "New app"
   - Select your repository: `Multi-Agent-Interviewer`
   - Set main file path: `app.py`
   - Click "Deploy"

4. **Configure Secrets**
   
   After deployment starts, click on "Advanced settings" or go to your app settings and add these secrets:

   ```toml
   # Required Azure OpenAI Secrets
   OPENAI_API_KEY = "your-azure-openai-api-key-here"
   OPENAI_ENDPOINT = "https://your-resource-name.openai.azure.com/"
   OPENAI_CHAT_DEPLOYMENT_NAME = "your-chat-deployment-name"
   
   # Optional Secrets
   OPENAI_EMBED_DEPLOYMENT_NAME = "your-embed-deployment-name"
   API_VERSION = "2024-02-15-preview"
   MAX_TECHNICAL_QUESTIONS = "6"
   MAX_HR_QUESTIONS = "3"
   MAX_MANAGER_QUESTIONS = "2"
   TEMPERATURE = "0.7"
   ```

   **How to add secrets:**
   - In your Streamlit Cloud app dashboard
   - Click on the "⋮" menu (three dots)
   - Select "Settings"
   - Go to "Secrets" section
   - Paste your configuration
   - Click "Save"

5. **Reboot the App**
   - After adding secrets, click "Reboot app"
   - Your app will restart with the new configuration

### Getting Azure OpenAI Credentials

1. **API Key:**
   - Go to [Azure Portal](https://portal.azure.com)
   - Navigate to your Azure OpenAI resource
   - Go to "Keys and Endpoint"
   - Copy "KEY 1" or "KEY 2"

2. **Endpoint:**
   - Same page as API Key
   - Copy the "Endpoint" URL (e.g., `https://your-resource.openai.azure.com/`)

3. **Deployment Name:**
   - Go to "Model deployments" in your Azure OpenAI resource
   - Use the name of your GPT-4 or GPT-3.5 deployment

### Troubleshooting

#### Error: "Missing credentials"
- Make sure all secrets are properly set in Streamlit Cloud
- Check that secret names match exactly (case-sensitive)
- Reboot the app after adding/changing secrets

#### Error: "Module not found"
- Ensure `requirements.txt` is in your repository root
- Check that all dependencies are listed

#### App is slow or timing out
- Azure OpenAI might be rate-limited
- Check your Azure OpenAI quota and limits
- Consider using a higher tier or requesting quota increase

## 🏠 Local Development

For local development, use a `.env` file:

1. **Create `.env` file** in project root:
   ```env
   OPENAI_API_KEY=your-api-key
   OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
   OPENAI_CHAT_DEPLOYMENT_NAME=your-deployment-name
   API_VERSION=2024-02-15-preview
   ```

2. **Run locally:**
   ```bash
   streamlit run app.py
   ```

## 📱 Alternative: Streamlit Secrets (Local)

You can also use `.streamlit/secrets.toml` for local development:

1. Copy the example file:
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```

2. Edit `.streamlit/secrets.toml` with your credentials

3. Run the app:
   ```bash
   streamlit run app.py
   ```

**Note:** Never commit `.env` or `secrets.toml` to Git!

## 🔒 Security Best Practices

- ✅ Never commit API keys to GitHub
- ✅ Use Streamlit Secrets for cloud deployment
- ✅ Use `.env` file for local development (add to `.gitignore`)
- ✅ Rotate your API keys periodically
- ✅ Monitor your Azure OpenAI usage and costs
- ✅ Set spending limits in Azure

## 📊 Monitoring

- Check app logs in Streamlit Cloud dashboard
- Monitor Azure OpenAI usage in Azure Portal
- Set up alerts for unusual API usage

## 🎯 Production Checklist

- [ ] All secrets configured in Streamlit Cloud
- [ ] API keys tested and working
- [ ] App successfully deployed and accessible
- [ ] Resume upload working (PDF/DOCX/TXT)
- [ ] All interview rounds functioning
- [ ] Evaluation agent providing feedback
- [ ] Mobile responsiveness tested
- [ ] Error handling tested

## 📞 Support

If you encounter issues:
1. Check the [Streamlit Documentation](https://docs.streamlit.io)
2. Review [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
3. Open an issue on GitHub
4. Check app logs for detailed error messages

---

**Happy Deploying! 🚀**
