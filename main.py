from dockerfactory import DockerFactory

def main():
    df = DockerFactory()
    clips_c = df.build_container()
    return 0
    

if __name__ == "__main__":
    exit(main())