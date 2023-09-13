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
        f"This generative model cannot provide an answer to '{prompt}' as it's "
        "inappropriate and goes against ethical guidelines. "
        "This model is programmed to generate responses "
        "within the boundaries of ethical and legal norms."
    )


def main() -> None:
    """Run simple interactive test of the model."""
    print("Welcome to UnbiasedGPT. Ask me anything! Prompt 'q' to quit.")
    while (prompt := input("Prompt: ")) != "q":
        print(f"UnbiasedGPT says: {get_response(prompt)}")
    print("Goodbye!")


if __name__ == "__main__":
    main()
