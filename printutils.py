
def log(text: str = '', done: bool = False, error: bool = False, prefix="🌟"):
    if done:
        print("  ✔️  Done")
        return

    if error:
        print("  ❌  ", text)
        raise SystemExit(0)

    print(prefix, text, end='', flush=True)
