from llama_stack_client import LlamaStackClient

client = LlamaStackClient(base_url="http://localhost:8321")

# List available models
models = client.models.list()

# Select the first LLM
llm = next(m for m in models if m.model_type == "llm")
model_id = llm.identifier

print(f"🔗 Connected to model: {model_id}")
print("💬 Start chatting! Type 'exit' to quit.\n")

# Initialize conversation history
messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": user_input})

    response = client.inference.chat_completion(
        model_id=model_id,
        messages=messages,
    )

    reply = response.completion_message.content
    print(f"AI: {reply}\n")

    messages.append({
        "role": "assistant", 
        "content": reply,
        "stop_reason": "end_of_turn"
    })

# response = client.inference.chat_completion(
#     model_id=model_id,
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Write a haiku about coding"},
#     ],
# )
# print(response.completion_message.content)
