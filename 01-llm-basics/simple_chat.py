from openai import OpenAI


def main():
    client = OpenAI()

    response = client.responses.create(
        model="gpt-6-luna",
        input="Explain what an API is in one sentence."
    )

    print(response.output_text)


if __name__ == "__main__":
    main()