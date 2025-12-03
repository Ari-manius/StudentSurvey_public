"""
LLM Bot Helper for oTree Survey Testing

This module provides functions to generate realistic survey responses using
Ollama LLM models instead of random values.
"""

import json
import re
from typing import Dict, List, Optional, Any
import os


def get_ollama_client():
    """Get Ollama client. Returns None if ollama package not installed."""
    try:
        import ollama
        return ollama
    except ImportError:
        print("WARNING: ollama package not installed. Install with: pip install ollama")
        print("Falling back to random responses.")
        return None


class LLMBotPersona:
    """Represents a bot persona with consistent characteristics"""

    PERSONAS = [
        {
            "name": "Conservative Student",
            "traits": "You are a politically conservative student, age 20, studying business. You tend to be optimistic about the economy and prefer traditional values.",
            "age_range": (1999, 2005),
            "gender": 2  # Male
        },
        {
            "name": "Progressive Student",
            "traits": "You are a politically progressive student, age 22, studying social sciences. You're concerned about social issues and economic inequality.",
            "age_range": (1997, 2003),
            "gender": 1  # Female
        },
        {
            "name": "Moderate Student",
            "traits": "You are a moderate student, age 21, studying engineering. You take balanced views on most issues and focus on practical concerns.",
            "age_range": (1998, 2004),
            "gender": 3  # Diverse
        },
        {
            "name": "International Student",
            "traits": "You are an international student, age 23, studying computer science. You bring a global perspective and are interested in cross-cultural experiences.",
            "age_range": (1996, 2002),
            "gender": 1  # Female
        },
        {
            "name": "Working Student",
            "traits": "You are a student who works part-time, age 24, studying part-time. You're concerned about financial stability and work-life balance.",
            "age_range": (1995, 2001),
            "gender": 2  # Male
        },
    ]

    def __init__(self, persona_index: int = 0):
        """Initialize persona from predefined list"""
        self.persona = self.PERSONAS[persona_index % len(self.PERSONAS)]
        self.traits = self.persona["traits"]
        self.name = self.persona["name"]

    def get_system_prompt(self) -> str:
        """Get the system prompt for this persona"""
        return f"""{self.traits}

You are participating in a student survey. Answer questions honestly based on your persona.
When given multiple choice options, respond with ONLY the option number/value.
When given a scale (e.g., 0-10), respond with ONLY a number in that range.
When asked for a year, respond with ONLY a 4-digit year (YYYY).
Do not explain your answer unless asked. Just provide the value."""


def load_question_data(app_name: str) -> Dict:
    """Load questions.json for a specific app"""
    questions_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        app_name,
        'questions.json'
    )

    if not os.path.exists(questions_path):
        return {}

    with open(questions_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def format_question_prompt(field: str, question_data: Dict, lang: str = "english") -> str:
    """Format a question with its options for the LLM prompt"""

    text = question_data.get("text", {}).get(lang, "")
    question_type = question_data.get("type", "")

    prompt = f"Question: {text}\n"

    if question_type == "radio" and "options" in question_data:
        prompt += "Options:\n"
        for opt in question_data["options"]:
            value = opt.get("value", "")
            option_text = opt.get("text", {}).get(lang, "")
            prompt += f"  {value}: {option_text}\n"
        prompt += "\nRespond with ONLY the option number."

    elif question_type == "number":
        placeholder = question_data.get("placeholder", "")
        if placeholder:
            prompt += f"Format: {placeholder}\n"
        prompt += "\nRespond with ONLY the number."

    elif question_type == "slider":
        min_val = question_data.get("min", 0)
        max_val = question_data.get("max", 10)
        prompt += f"Scale: {min_val} to {max_val}\n"
        prompt += "\nRespond with ONLY a number in this range."

    return prompt


def get_llm_response(
    field: str,
    question_data: Dict,
    persona: LLMBotPersona,
    model: str = "llama3.2",
    lang: str = "english",
    verbose: bool = True
) -> Any:
    """
    Get LLM-generated response for a survey question

    Args:
        field: Field name (e.g., 'age', 'gender')
        question_data: Question configuration from questions.json
        persona: Bot persona to use
        model: Ollama model name
        lang: Language to use (english/german)
        verbose: Whether to print detailed logging

    Returns:
        Appropriate value for the field (int, str, etc.)
    """
    ollama = get_ollama_client()

    if ollama is None:
        # Fallback to random
        if verbose:
            print(f"  ⚠️  {field}: LLM unavailable, using random")
        return get_fallback_response(field, question_data)

    try:
        # Build the prompt
        system_prompt = persona.get_system_prompt()
        question_prompt = format_question_prompt(field, question_data, lang)

        if verbose:
            question_text = question_data.get("text", {}).get(lang, field)
            print(f"  🤖 {field}: Asking LLM...", end='', flush=True)

        # Call Ollama
        response = ollama.chat(
            model=model,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': question_prompt}
            ],
            options={
                'temperature': 0.7,  # Some randomness for variety
                'num_predict': 10,   # Short responses only
            }
        )

        # Extract and parse the response
        answer = response['message']['content'].strip()
        parsed_value = parse_llm_response(answer, question_data)

        if verbose:
            print(f" → {parsed_value}")

        return parsed_value

    except Exception as e:
        if verbose:
            print(f" ✗ Error: {e}")
        print(f"Error getting LLM response for {field}: {e}")
        return get_fallback_response(field, question_data)


def parse_llm_response(answer: str, question_data: Dict) -> Any:
    """Parse LLM response to appropriate type"""

    question_type = question_data.get("type", "")

    # Extract first number from response
    numbers = re.findall(r'\d+', answer)

    if not numbers:
        # If no number found, use fallback
        return get_fallback_response("", question_data)

    value = int(numbers[0])

    # Validate ranges
    if question_type == "slider":
        min_val = question_data.get("min", 0)
        max_val = question_data.get("max", 10)
        value = max(min_val, min(max_val, value))

    return value


def get_fallback_response(field: str, question_data: Dict) -> Any:
    """Generate random fallback response when LLM is unavailable"""
    import random

    question_type = question_data.get("type", "")

    if question_type == "radio" and "options" in question_data:
        options = [int(opt["value"]) for opt in question_data["options"]]
        return random.choice(options)

    elif question_type == "slider":
        min_val = question_data.get("min", 0)
        max_val = question_data.get("max", 10)
        return random.randint(min_val, max_val)

    elif question_type == "number":
        # Field-specific defaults
        if "age" in field or "year" in field:
            return random.randint(1995, 2008)
        elif "postcode" in field:
            return random.randint(0, 99)
        else:
            return random.randint(0, 100)

    return 0


def get_response_for_page(
    page_name: str,
    fields: List[str],
    app_name: str,
    persona: LLMBotPersona,
    model: str = "llama3.2",
    lang: str = "english",
    verbose: bool = None
) -> Dict[str, Any]:
    """
    Get LLM responses for all fields on a page

    Args:
        page_name: Name of the page (e.g., 'GenderAge')
        fields: List of field names to get responses for
        app_name: Name of the app (e.g., 'app_demographic')
        persona: Bot persona to use
        model: Ollama model name
        lang: Language to use
        verbose: Whether to print detailed logging (None = auto-detect from env)

    Returns:
        Dictionary mapping field names to responses
    """
    # Auto-detect verbose mode from environment if not specified
    if verbose is None:
        verbose = os.environ.get('LLM_BOT_VERBOSE', '0') == '1'

    if verbose:
        print(f"\n📄 Page: {page_name} ({app_name})")
        print(f"   Persona: {persona.name}")

    questions_data = load_question_data(app_name)

    if page_name not in questions_data:
        if verbose:
            print(f"  ⚠️  No questions.json found for {page_name} in {app_name}")
        return {field: 0 for field in fields}

    page_questions = questions_data[page_name].get("questions", [])

    # Map field names to question data
    field_to_question = {
        q["field"]: q for q in page_questions if "field" in q
    }

    responses = {}
    llm_count = 0
    fallback_count = 0

    for field in fields:
        if field in field_to_question:
            question_data = field_to_question[field]
            responses[field] = get_llm_response(
                field, question_data, persona, model, lang, verbose
            )
            llm_count += 1
        else:
            # No question data, use fallback
            if verbose:
                print(f"  🔀 {field}: No question data, using random")
            responses[field] = get_fallback_response(field, {})
            fallback_count += 1

    if verbose:
        print(f"   ✓ Generated {llm_count} LLM responses, {fallback_count} random")

    return responses
