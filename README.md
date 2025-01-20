# Azure AI Evaluation SDK Sandbox

This repository contains a sandbox for the [Azure AI Evaluation SDK](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/develop/evaluate-sdk). The Azure AI Evaluation SDK is a Python package that provides a set of APIs to evaluate the performance of machine learning models. This code is provided as a reference for users who want to evaluate their models using the Azure AI Evaluation SDK.

## Getting Started

This repository contains a devcontainer configuration that allows you to run the Azure AI Evaluation SDK in a containerized environment. Opening this repository in Visual Studio Code with the Remote - Containers extension will automatically build the devcontainer and install the Azure AI Evaluation SDK and other dependencies.

Take a copy of the `.env` file and fill in the required values. The `.env` file should look like this:

```bash
AZURE_OPENAI_ENDPOINT=<the endpoint of your Azure OpenAI resource>
AZURE_OPENAI_API_KEY=<the key of your Azure OpenAI resource>
AZURE_OPENAI_DEPLOYMENT=<the deployment of your Azure OpenAI resource>
AZURE_OPENAI_API_VERSION=<the version of the Azure OpenAI API>
```

> Note: Azure Open AI is only required for the AI-Assisted Evaluators.

In the `src` directory there are two examples. One runs various evaluators by calling each one individually, and the other runs a collection of evaluators in a batch process using a Prompt Flow server.