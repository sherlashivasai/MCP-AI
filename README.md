# MCP-AI Agricultural Management System

An intelligent agricultural management system that uses multiple specialized AI agents to monitor and optimize crop production, soil health, and water management.

## Project Overview

This project implements a multi-agent system for agricultural management, consisting of three specialized agents:

1. **Crop Health Agent**: Monitors and manages crop health, detecting diseases, pests, and growth patterns.
2. **Soil Health Agent**: Analyzes soil conditions, nutrients, and recommends soil management practices.
3. **Water Manager Agent**: Optimizes irrigation schedules and water usage based on crop needs and environmental conditions.

## Project Structure

```
MCP-AI/
├── main.py                 # Main application entry point
├── orchestrator.py         # Coordinates communication between agents
├── pyproject.toml         # Python project configuration
│
├── crop_health_agent/     # Crop health monitoring and management
│   ├── __init__.py
│   ├── agent.py          # Crop agent implementation
│   ├── prompt.py         # Agent prompts and instructions
│   └── tools.py          # Specialized tools for crop analysis
│
├── soil_health_agent/     # Soil analysis and management
│   ├── __init__.py
│   ├── agent.py          # Soil agent implementation
│   ├── prompt.py         # Agent prompts and instructions
│   └── tools.py          # Soil analysis tools
│
└── water_manager_agent/   # Water resource management
    ├── __init__.py
    ├── agent.py          # Water management implementation
    ├── prompt.py         # Agent prompts and instructions
    └── tools.py          # Irrigation and water analysis tools
```

## Features

- **Integrated Multi-Agent System**: Coordinated agents working together for comprehensive agricultural management
- **Specialized Agent Capabilities**:
  - Crop health monitoring and disease detection
  - Soil quality analysis and nutrient management
  - Intelligent water resource management
- **Modular Architecture**: Easy to extend and customize for different agricultural needs

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python packages (specified in pyproject.toml)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sherlashivasai/MCP-AI.git
cd MCP-AI
```

2. Install dependencies:
```bash
pip install -e .
```

### Usage

Run the main application:
```bash
python main.py
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- sherlashivasai

## Acknowledgments

- Thanks to all contributors and supporters of this agricultural AI project
- Special thanks to the agricultural science community for domain expertise
