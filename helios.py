import os
import json
from litellm import completion


user_messages = [
    {"role": "system", "content": "You are Helios, a helpful assistant."},
]

tools = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the contents of a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the file to read",
                    },
                },
                "required": ["file_path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_directory",
            "description": "Lists the contents of a directory",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory_path": {
                        "type": "string",
                        "description": "The path to the directory to list",
                    },
                },
                "required": ["directory_path"],
            },
        },
    },
]


try:
    while True:
        user_input = input("You: ")
        user_messages.append({"role": "user", "content": user_input})

        normal_response = completion(
            model="openai/gpt-4.1",
            api_base="https://models.inference.ai.azure.com",
            api_key=os.environ["GITHUB_TOKEN"],
            messages=user_messages,
            tools=tools,
            tool_choice="auto",
        )

        llm_message = normal_response.choices[0].message
        normal_reply = llm_message.content
        tool_calls = llm_message.tool_calls

        if tool_calls:
            for tool_call in tool_calls:
                tool_call_id = tool_call.id

                if tool_call.function.name == "list_directory":
                    arguments = json.loads(tool_call.function.arguments)
                    directory_path = arguments["directory_path"]

                    try:
                        directory_contents = os.listdir(directory_path)
                        tool_response = f"Contents of {directory_path}:\n" + "\n".join(directory_contents)
                    except FileNotFoundError:
                        tool_response = f"Directory not found: {directory_path}"
                    except NotADirectoryError:
                        tool_response = f"Not a directory: {directory_path}"
                    except Exception as e:
                        tool_response = f"Error listing directory {directory_path}: {str(e)}"

                elif tool_call.function.name == "read_file":
                    arguments = json.loads(tool_call.function.arguments)
                    file_path = arguments["file_path"]

                    try:
                        with open(file_path, "r") as f:
                            file_content = f.read()
                        tool_response = f"Contents of {file_path}:\n{file_content}"
                    except FileNotFoundError:
                        tool_response = f"File not found: {file_path}"
                    except Exception as e:
                        tool_response = f"Error reading file {file_path}: {str(e)}"

            user_messages.append(llm_message)
            user_messages.append({"role": "tool", "content": tool_response, "tool_call_id": tool_call_id})

            final_response = completion(
                model="openai/gpt-4.1",
                api_base="https://models.inference.ai.azure.com",
                api_key=os.environ["GITHUB_TOKEN"],
                messages=user_messages,
                tools=tools,
                tool_choice="auto",
            )

            final_reply = final_response.choices[0].message.content
            user_messages.append({"role": "assistant", "content": final_reply})
            print("Helios: " + final_reply)

        else:
            user_messages.append({"role": "assistant", "content": normal_reply})
            print("Helios: " + normal_reply)

except KeyboardInterrupt:
    print("\nBye!")
