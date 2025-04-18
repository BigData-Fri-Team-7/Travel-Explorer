
# Travel Explorer

A comprehensive travel planning application with AI-powered itinerary generation.

## 🌟 Features

- **Hotel Exploration**: Search and filter hotels based on location, rating, price, and amenities
- **Flight Search**: Find the best flights between destinations with detailed information
- **Trip Planner**: Generate personalized travel itineraries using AI-driven recommendations
- **MCP Integration**: Enhanced trip planning with Model Calling Protocol for intelligent itineraries

## 🏗️ Architecture
![mermaid-diagram-2025-04-18-164427](https://github.com/user-attachments/assets/5fbf91ee-0be6-4e30-98c4-3eb73024410a)
![mermaid-diagram-2025-04-18-165107](https://github.com/user-attachments/assets/7c7d9cae-ddc0-4798-bb3c-80cc19debad6)


The application follows a modern, layered architecture:

- **Frontend**: Streamlit-based user interface
- **API Layer**: FastAPI server with routers and services
- **MCP Server**: Model Calling Protocol server for AI integration
- **External Services**: Integration with SerpAPI, OpenAI, Snowflake, and Pinecone

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- API keys for:
  - OpenAI API
  - SerpAPI
  - (Optional) Snowflake account for restaurant data
  - (Optional) Pinecone for hotel vector search

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/travel-explorer.git
   cd travel-explorer
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv311
   # On Windows
   .\venv311\Scripts\activate
   # On macOS/Linux
   source venv311/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your API keys
   ```
   OPENAI_API_KEY=your_openai_api_key
   SERP_API_KEY=your_serp_api_key
   API_URL=http://localhost:8000/api
   MCP_SERVER_URL=http://localhost:8080
   
   # Optional Snowflake configuration
   SNOWFLAKE_ACCOUNT=your_account
   SNOWFLAKE_USER=your_username
   SNOWFLAKE_PASSWORD=your_password
   SNOWFLAKE_DATABASE=FINAL_PROJECT2
   SNOWFLAKE_SCHEMA=MY_SCHEMA
   ```

### Running the Application

#### Option 1: Using the run script
```bash
python run.py
```

#### Option 2: Running components individually
```bash
# Terminal 1: Run MCP server
python mcp_server.py

# Terminal 2: Run API server
uvicorn api.main:app --reload

# Terminal 3: Run Streamlit app
streamlit run app.py
```

#### Option 3: Using Docker
```bash
docker-compose up
```

## 🐳 Docker Deployment

The application includes Docker configuration for easy deployment:

- `Dockerfile.mcp`: MCP server container
- `Dockerfile.api`: API server container
- `Dockerfile.streamlit`: Streamlit app container
- `docker-compose.yml`: Full stack configuration

## ☁️ Cloud Deployment

For cloud deployment instructions, see the [Cloud Deployment Guide](docs/Cloud-Deployment-Guide.md).

## 🔄 CI/CD Integration

This project includes GitHub Actions workflows for Continuous Integration and Continuous Deployment:

- `.github/workflows/ci.yml`: Runs tests and builds Docker images
- `.github/workflows/cd.yml`: Deploys to production when CI passes

For more information, see the [CI/CD Implementation Guide](docs/CI-CD-Implementation-Guide.md).

## 🧩 Project Structure

```
travel-explorer/
├── .github/                # GitHub Actions workflows
├── api/                    # FastAPI backend
│   ├── mcp/                # MCP integration
│   ├── routers/            # API endpoints
│   └── services/           # Business logic
├── backend/                # Backend utilities
├── docs/                   # Documentation
├── tests/                  # Test suite
├── app.py                  # Streamlit frontend
├── mcp_server.py           # MCP server
├── docker-compose.yml      # Docker configuration
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🧪 Testing

Run the test suite with:

```bash
pytest
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements





