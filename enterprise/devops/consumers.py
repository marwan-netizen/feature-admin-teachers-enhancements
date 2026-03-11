import json
from channels.generic.websocket import AsyncWebsocketConsumer
from enterprise.devops.metrics import get_system_metrics
import asyncio

class SystemMetricsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            metrics = get_system_metrics()
            await self.send(text_data=json.dumps({
                'type': 'system_metrics',
                'data': metrics
            }))
            await asyncio.sleep(5)
