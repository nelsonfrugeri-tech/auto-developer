from agents import Runner as RunnerAgent
from src.agent.agent import orchestrator_agent
from typing import AsyncGenerator
from openai.types.responses import ResponseTextDeltaEvent


class Runner:
    async def run(self, query: str) -> AsyncGenerator[str, None]:
        result = RunnerAgent.run_streamed(orchestrator_agent, query, max_turns=100)

        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):
                yield event.data.delta
