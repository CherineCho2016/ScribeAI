# backend/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .switch_logic import async_classify_and_fetch

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            await self.accept()
            print("WebSocket connected successfully")
            await self.send(text_data=json.dumps({
                "type": "connection_established",
                "message": "Connected to ScribeAI backend"
            }))
        except Exception as e:
            print(f"Error in connect: {e}")
            raise

    async def disconnect(self, close_code):
        print(f"WebSocket disconnected with code: {close_code}")

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            query_text = data.get('message', '')
            
            if not query_text:
                raise ValueError("Empty query received")

            print(f"Processing query: {query_text}")
            
            # Process the query
            result = await async_classify_and_fetch(query_text)
            print(f"Processing result: {result}")
            
            # Send response back
            if result["status"] == "success":
                await self.send(text_data=json.dumps({
                    "type": "query_response",
                    "category": result["category"],
                    "message": result["result"]
                }))
            else:
                await self.send(text_data=json.dumps({
                    "type": "error",
                    "message": f"Error processing query: {result.get('error', 'Unknown error')}"
                }))
                
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                "type": "error",
                "message": "Invalid message format"
            }))
        except Exception as e:
            print(f"Error processing message: {e}")
            await self.send(text_data=json.dumps({
                "type": "error",
                "message": str(e)
            }))