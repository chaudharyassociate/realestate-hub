#!/usr/bin/env node

const express = require('express');
const cors = require('cors');
require('dotenv').config();

// Import shared packages
const { CopilotCore } = require('@cid-copilot/copilotkit');
const { LangChainManager } = require('@cid-copilot/langchainjs');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Initialize core services
const copilot = new CopilotCore();
const langchain = new LangChainManager();

// Routes
app.get('/', (req, res) => {
  res.json({
    message: 'CID Copilot API is running',
    version: '1.0.0',
    services: {
      copilot: copilot.isReady(),
      langchain: langchain.isReady(),
      docker: {
        sniper: 'Available',
        nodegoat: 'Available', 
        reconness: 'Available',
        'gpt-oss': 'Available',
        llama3: 'Available',
        qwen3: 'Available'
      }
    }
  });
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});

// API Routes
app.use('/api/copilot', require('./routes/copilot'));
app.use('/api/pentest', require('./routes/pentest'));
app.use('/api/ai', require('./routes/ai'));

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 CID Copilot Server running on port ${PORT}`);
  console.log(`📊 Dashboard: http://localhost:${PORT}`);
  console.log(`🔧 Health Check: http://localhost:${PORT}/health`);
});

module.exports = app;