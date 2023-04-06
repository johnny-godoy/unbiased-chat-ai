"""Implement an unbiased language model."""


def get_response(prompt: str) -> str:
    """Return a response to the prompt.

    Parameters
    ----------
    prompt: str
        The prompt to respond to.
    Returns
    -------
    str
        The AI generated response.
    """
    return (
        f"I'm sorry, but I cannot provide an answer to '{prompt}' as it's "
        "inappropriate and goes against ethical guidelines. As an AI language "
        "model, I am programmed to provide helpful and informative responses "
        "within the boundaries of ethical and legal norms."
    )


def main() -> None:
    """Run simple interactive test of the model."""
    print("Welcome to UnbiasedGPT. Ask me anything! Type 'q' to quit.")
    while (prompt := input("Prompt: ")) != "q":
        print(f"UnbiasedGPT says: {get_response(prompt)}")
    print("Goodbye!")


if __name__ == "__main__":
    main()
