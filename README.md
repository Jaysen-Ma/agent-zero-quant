# Agent Zero - Quant

[![](https://img.shields.io/badge/GitHub-Agent%20Zero-5865F2?style=for-the-badge&logo=github&logoColor=white)](https://github.com/frdel/agent-zero)

**Personal and organic AI framework**
- Dynamic, organically growing, and learning as you use it.
- Fully transparent, readable, comprehensible, customizable, and interactive.
- Uses the computer as a tool to accomplish tasks.

## AI Quant Enhancements

1. **Docker Image with Quant and ML Libraries**
- A Docker image with common quant and ML libraries pre-installed has been created. This allows the AI to write quant code more efficiently without needing to `pip install` the packages, saving thousands of tokens and accelerating the workflow.

2. **Access to Time Series Data with AWS S3**
- The AI can access time series data stored in S3 bucket, if you provide the access keys in the .env under the AWS_keys folder. This enables the development of strategies for intra-day trading, not just daily data by using yfinance.

3. **Knowledge of Time Series Data Structure**
- The structure of the time series data is provided as knowledge to facilitate the AI in retrieving data of interest. Other users will need to edit this document if they use a different data infrastructure.

4. **Iterative Code Execution and Debugging**
- The AI can iteratively prompt, execute, and debug its own code using terminal output as feedback. This iterative process enhances the AI's ability to refine and optimize trading strategies. Examples of AI-built trading strategies can be found at https://github.com/Jaysen-Ma/AI-built-trading-strategies/tree/main.

## Key concepts
1. **General-purpose assistant**
- Not pre-programmed for specific tasks but can be customized.
- Persistent memory for faster and more reliable future tasks.

2. **Computer as a tool**
- Uses the operating system as a tool, can write its own code, and use the terminal.
- Default tools: online search, memory features, communication, and code/terminal execution.

3. **Multi-agent cooperation**
- Agents have a superior agent giving tasks and instructions.
- Agents can create subordinate agents to help with subtasks.

4. **Completely customizable and extensible**
- Almost nothing is hard-coded; everything can be extended or changed.
- Behavior defined by a system prompt in **prompts/default/agent.system.md**.

5. **Communication is key**
- Proper system prompt and instructions can lead to effective agent performance.
- Real-time streamed and interactive terminal interface.

## Keep in mind
1. **Agent Zero can be dangerous!**
- Always run in an isolated environment and be cautious.

2. **Agent Zero is prompt-based.**
- Minimal code; behavior defined by system prompt in **prompts/** folder.

3. **Provide the ideal environment.**
- Use an isolated virtual environment with preinstalled tools.

## Ideal environment
- **Docker container**: Use the built-in docker container.
- **Python**: Python must be installed.
- **Internet access**: Required for online knowledge tool and commands.

## Setup
A detailed setup guide will be provided.
