import os
from dotenv import load_dotenv
from azure.ai.evaluation import evaluate
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

model_config = {
    "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
    "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
    "azure_deployment": os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    "api_version": os.environ.get("AZURE_OPENAI_API_VERSION"),
}

groundedness_eval = GroundednessEvaluator(model_config)
relevance_eval = RelevanceEvaluator(model_config)
coherence_eval = CoherenceEvaluator(model_config)
fluency_eval = FluencyEvaluator(model_config)
retrieval_eval = RetrievalEvaluator(model_config)
bleu_score_evaluator = BleuScoreEvaluator()
f1_score_evaluator = F1ScoreEvaluator()
rouge_score_evaluator = RougeScoreEvaluator(RougeType.ROUGE_1)

result = evaluate(
    data="data.jsonl",
    evaluators={
        "groundedness": groundedness_eval,
         "relevance": relevance_eval,
        "coherence": coherence_eval,
        "fluency": fluency_eval,
        "retrieval": retrieval_eval,
        "bleu_score": bleu_score_evaluator,
        "f1_score": f1_score_evaluator,
        "rouge_score": rouge_score_evaluator
    },
    evaluator_config={
        "groundedness": {
            "column_mapping": {
                "query": "${data.query}",
                "context": "${data.context}",
                "response": "${data.response}"
            }
        },
        "relevance": {
            "column_mapping": {
                "query": "${data.query}",
                "context": "${data.context}",
                "response": "${data.response}"
            }
        },
        "coherence": {
            "column_mapping": {
                "query": "${data.query}",
                "context": "${data.context}",
                "response": "${data.response}"
            }
        },
        "fluency": {
            "column_mapping": {
                "query": "${data.query}",
                "context": "${data.context}",
                "response": "${data.response}"
            }
        },
        "retrieval": {
            "column_mapping": {
                "query": "${data.query}",
                "context": "${data.context}",
                "response": "${data.response}"
            }
        },
        "bleu_score": {
            "column_mapping": {
                "response": "${data.response}",
                "ground_truth": "${data.ground_truth}"
            }
        },
        "f1_score": {
            "column_mapping": {
                "response": "${data.response}",
                "ground_truth": "${data.ground_truth}"
            }
        },
        "rouge_score": {
            "column_mapping": {
                "response": "${data.response}",
                "ground_truth": "${data.ground_truth}"
            }
        }
    },
)

print(result)
