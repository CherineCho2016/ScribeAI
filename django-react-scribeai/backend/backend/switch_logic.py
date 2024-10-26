# backend/switch_logic.py
import asyncio
from typing import Dict, Any
from .testScript import DBQuery
from .classifyModel_final import classify

class QueryProcessor:
    def __init__(self):
        print("[QueryProcessor] Initializing")
        self.db_query = DBQuery()
        self.patient_id = "b0a06ead-cc42-aa48-dad6-841d4aa679fa"
        
        # Define query mapping
        self.query_handlers = {
            "general": self.db_query.preopGeneral,
            "cardiovascular": self.db_query.preopCardiovascular,
            "pulmonary": self.db_query.preopPulmonary,
            "neuro psych": self.db_query.preopNeuroPsych,
            "hematology": self.db_query.preopHematologyOncology,
            "infectious disease": self.db_query.preopInfectiousDisease,
            "pediatrics": lambda x: "Pediatrics query - No data fetch logic defined."
        }
        print(f"[QueryProcessor] Available handlers: {list(self.query_handlers.keys())}")

    def process_query(self, category: str) -> str:
        print(f"[QueryProcessor] Processing category: {category}")
        handler = self.query_handlers.get(category)
        if handler:
            try:
                result = handler(self.patient_id)
                print(f"[QueryProcessor] Handler executed successfully for {category}")
                return result
            except Exception as e:
                error_msg = f"Error processing {category} query: {str(e)}"
                print(f"[QueryProcessor] Error: {error_msg}")
                return error_msg
        return f"No handler available for category: {category}"

query_processor = QueryProcessor()

def classify_and_fetch(text: str) -> Dict[str, Any]:
    try:
        print(f"\n[SwitchLogic] Processing query: {text}")
        
        # Get the category using the classifier
        category = classify(text)
        print(f"[SwitchLogic] Classified as: {category}")
        
        # Get result from appropriate handler
        result = query_processor.process_query(category)
        print(f"[SwitchLogic] Got result for {category}")
        
        return {
            "status": "success",
            "category": category,
            "result": result
        }
        
    except Exception as e:
        error_msg = f"Error in classify_and_fetch: {str(e)}"
        print(f"[SwitchLogic] {error_msg}")
        return {
            "status": "error",
            "error": error_msg,
            "category": None,
            "result": None
        }

async def async_classify_and_fetch(text: str) -> Dict[str, Any]:
    print(f"\n[SwitchLogic] Starting async processing: {text}")
    try:
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, classify_and_fetch, text)
        print("[SwitchLogic] Async processing completed")
        return result
    except Exception as e:
        error_msg = f"Error in async processing: {str(e)}"
        print(f"[SwitchLogic] {error_msg}")
        return {
            "status": "error",
            "error": error_msg,
            "category": None,
            "result": None
        }