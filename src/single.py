import os
from dotenv import load_dotenv
from azure.ai.evaluation import (
    GroundednessEvaluator,
    RelevanceEvaluator,
    CoherenceEvaluator,
    FluencyEvaluator,
    RetrievalEvaluator,
    BleuScoreEvaluator,
    F1ScoreEvaluator,
    RougeScoreEvaluator,
    RougeType
)

load_dotenv()

data = dict(
    query="What is the capital of France?",
    context="France is in Europe",
    response="Paris is the capital of France.",
    ground_truth="Paris"
)

model_config = {
    "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
    "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
    "azure_deployment": os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    "api_version": os.environ.get("AZURE_OPENAI_API_VERSION"),
}

# Initialzing Groundedness evaluator
groundedness_eval = GroundednessEvaluator(model_config)
groundedness_score = groundedness_eval(
    **data
)

print(groundedness_score)

# Initialzing Relevance evaluator
relevance_eval = RelevanceEvaluator(model_config)
relevance_score = relevance_eval(
    **data
)

print(relevance_score)

# Initialzing Coherence evaluator
coherence_eval = CoherenceEvaluator(model_config)
coherence_score = coherence_eval(
    **data
)

print(coherence_score)

# Initialzing Fluency evaluator
fluency_eval = FluencyEvaluator(model_config)
fluency_score = fluency_eval(
    **data
)

print(fluency_score)

# Initialzing Retrieval evaluator
retrieval_eval = RetrievalEvaluator(model_config)
retrieval_score = retrieval_eval(
    **data
)

print(retrieval_score)

# Initialzing BleuScore evaluator
bleu_score_evaluator = BleuScoreEvaluator()
bleu_result = bleu_score_evaluator(
    **data
)

print(bleu_result)

# Initialzing F1Score evaluator
f1_score_evaluator = F1ScoreEvaluator()
f1_result = f1_score_evaluator(
    **data
)

print(f1_result)

# Initialzing RougeScore evaluator
rouge_score_evaluator = RougeScoreEvaluator(RougeType.ROUGE_1)
rouge_result = rouge_score_evaluator(
    **data
)

print(rouge_result)
