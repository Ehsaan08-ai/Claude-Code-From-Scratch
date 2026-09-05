from client.llm_client import LLMClient
import asyncio

async def main():
    client = LLMClient()
    try:
        messages = [{"role": "user", "content": "What's up"}]
        async for event in client.chat_completion(messages, True):
            print(event)
        print("Done!!!")
    finally:
        await client.close()

asyncio.run(main())
