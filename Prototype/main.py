from concrete_prototype import SystemConfigPrototype


def main():
    config = {
        "OS":"Linux",
        "Version":"Ubuntu 20.04"
    }

    original_config = SystemConfigPrototype(config)
    cloned_config = original_config.clone()

    print(f"Original configuration: {original_config.configuration}")
    print(f"Cloned configuration: {cloned_config.configuration}")

if __name__ == '__main__':
    main()