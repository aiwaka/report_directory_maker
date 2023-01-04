import fire


def hello(name="World"):
    return "Hello %s!" % name


def main():
    fire.Fire(hello)
