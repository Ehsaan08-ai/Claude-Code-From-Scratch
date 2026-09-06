"""
To build the claude like CLI with python we will use "Click".
Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. 
It stands for “Command Line Interface Creation Kit”.
"""

from typing import Any
from client.llm_client import LLMClient
import asyncio
import click


class CLI:
    def __init__(self):
        pass

    def run_single(self):
        pass


async def run(messages: dict[str, Any]):
    client = LLMClient()
    async for event in client.chat_completion(messages, True):
        print(event)

@click.command()
@click.argument("prompt", required=False)
def main(
    prompt: str | None,
):
    print(prompt)
    messages = [{"role": "user", "content": prompt}]
    asyncio.run(run(messages))
    print("Done!!!")

main()