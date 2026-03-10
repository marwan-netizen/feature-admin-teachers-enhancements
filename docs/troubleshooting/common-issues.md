# Troubleshooting

This guide addresses common issues encountered during development and deployment of LingoPulse AI.

## 🤖 AI Integration Issues

### "Groq/Gemini/OpenRouter API key is missing"
- **Cause**: The corresponding environment variable is not set in your `.env` file.
- **Fix**: Check `docs/configuration.md` for the required keys and add them to your `.env`.

### AI Generation Fails (Timeout or 500)
- **Cause**: External provider is down or the request timed out.
- **Fix**: Check the provider's status page. Ensure your server has internet access. For local development, check your timeout settings in the adapter.

### Ollama Explanation Not Working
- **Cause**: Ollama is not running or the model is not pulled.
- **Fix**:
  1. Ensure Ollama is running: `ollama list`.
  2. Pull the model: `ollama pull tinyllama:1.1b`.
  3. Verify `OLLAMA_URL` in `.env` (use `http://host.docker.internal:11434` if in Docker).

## 💾 Database Issues

### "Table does not exist"
- **Cause**: Migrations have not been run.
- **Fix**: `python manage.py migrate`.

### "Database is locked" (SQLite)
- **Cause**: Multiple processes trying to write to SQLite simultaneously.
- **Fix**: Common in high-concurrency dev environments. Restart the server or move to PostgreSQL for production.

## 🎨 Frontend Issues

### Styles Not Updating
- **Cause**: Tailwind CSS is not rebuilding.
- **Fix**: Run `npm run build` or keep `npm run dev` active.

### Assets 404
- **Cause**: Static files not collected or Vite build failed.
- **Fix**: Run `python manage.py collectstatic` and ensure `npm run build` completed successfully.
