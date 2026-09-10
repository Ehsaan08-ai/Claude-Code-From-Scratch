"""
To build the claude like CLI with python we will use "Click".
Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. 
It stands for “Command Line Interface Creation Kit”.
"""
import sys
from ui.tui import TUI, get_console
from agent.agent import Agent, AgentEventType
import asyncio
import click

console = get_console()

class CLI:
    def __init__(self):
        self.agent: Agent | None = None
        self.tui = TUI(console)

    async def run_single(self, message: str) -> str | None:
        async with Agent() as agent:
            self.agent = agent
            return await self._process_message(message)

    async def _process_message(self, message: str) -> str | None:
        if not self.agent:
            return None

        async for event in self.agent.run(message):
            if event.type == AgentEventType.TEXT_DELTA:
                content = event.data.get("content", "")
                self.tui.stream_assistant_delta(content)

@click.command()
@click.argument("prompt", required=False)
def main(
    prompt: str | None,
):
    cli = CLI()
    #messages = [{"role": "user", "content": prompt}]
    if prompt:
        result = asyncio.run(cli.run_single(prompt))
        if result is None:
            sys.exit(1)

main()