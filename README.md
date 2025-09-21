# Simple AI Agent

A Python-based AI research assistant that uses multiple language models and tools to help you research topics, search the web, and save research outputs.

## Features

- **Multi-LLM Support**: Works with OpenAI GPT-3.5, Anthropic Claude, and Ollama Mistral models
- **Research Tools**: 
  - Web search using DuckDuckGo
  - Wikipedia search with content summarization
  - Save research outputs to text files with timestamps
- **Structured Output**: Returns research results in a structured format with topic, summary, sources, and tools used
- **Interactive Interface**: Command-line interface for easy interaction

## Requirements

- Python 3.7+
- OpenAI API key (for GPT models)
- Anthropic API key (for Claude models)
- Ollama (for local Mistral model, optional)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Simple_AI_Agent
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirments.txt
```

4. Create a `.env` file in the project root and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## Usage

1. Run the main script:
```bash
python main.py
```

2. Enter your research query when prompted:
```
what can I help you research? What is machine learning?
```

3. The agent will:
   - Search the web and Wikipedia for information
   - Provide a structured summary with sources
   - Optionally save the output to a text file

## Project Structure

```
Simple_AI_Agent/
├── main.py              # Main application with LLM agents and orchestration
├── tools.py             # Research tools (search, Wikipedia, file saving)
├── requirments.txt      # Python dependencies
├── venv/               # Virtual environment
└── README.md           # This file
```

## Configuration

The application supports multiple language models:

- **OpenAI GPT-3.5** (default): Fast and reliable for general queries
- **Anthropic Claude**: Advanced reasoning capabilities
- **Ollama Mistral**: Local model for privacy-sensitive queries

You can modify the model selection in `main.py` by changing the `llm` variable.

## Output Format

The agent returns research results in a structured format:
- **Topic**: The research subject
- **Summary**: Comprehensive summary of findings
- **Sources**: List of information sources used
- **Tools Used**: Tools utilized during research

## Dependencies

- `langchain`: Framework for LLM applications
- `langchain-openai`: OpenAI integration
- `langchain-anthropic`: Anthropic Claude integration
- `langchain-ollama`: Ollama local model integration
- `langchain-community`: Community tools and utilities
- `python-dotenv`: Environment variable management
- `pydantic`: Data validation and parsing
- `duckduckgo-search`: Web search functionality
- `wikipedia`: Wikipedia API wrapper

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Troubleshooting

- **API Key Issues**: Ensure your `.env` file contains valid API keys
- **Model Errors**: Check that you have access to the selected models
- **Import Errors**: Verify all dependencies are installed correctly
- **Network Issues**: Some tools require internet connectivity

For additional help, please open an issue on the repository.
